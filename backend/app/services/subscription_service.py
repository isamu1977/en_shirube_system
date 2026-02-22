"""
Subscription Service - Stripe integration for premium subscriptions.

Provides functionality for managing Stripe customers, subscription status,
and SOS credits for premium users.
"""

import os
import uuid
from datetime import datetime, timezone
from typing import Optional

import stripe
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import User

stripe.api_key = os.getenv("STRIPE_SECRET_KEY", "")

DEFAULT_SOS_CREDITS = 3


class SubscriptionService:
    """Service for managing premium subscriptions via Stripe."""

    async def get_or_create_user(
        self, stripe_customer_id: Optional[str] = None, db: AsyncSession = None
    ) -> User:
        """
        Get existing user by Stripe customer ID or create new one.
        
        Args:
            stripe_customer_id: The Stripe customer ID
            db: Database session
            
        Returns:
            The User object
        """
        if stripe_customer_id:
            result = await db.execute(
                select(User).where(User.stripe_customer_id == stripe_customer_id)
            )
            existing_user = result.scalar_one_or_none()
            if existing_user:
                return existing_user

        new_user = User(
            stripe_customer_id=stripe_customer_id,
            subscription_status="none",
            sos_credits=0,
        )
        db.add(new_user)
        await db.commit()
        await db.refresh(new_user)
        return new_user

    async def create_stripe_customer(
        self, email: Optional[str] = None, name: Optional[str] = None
    ) -> str:
        """
        Create a new Stripe customer.
        
        Args:
            email: Customer email
            name: Customer name
            
        Returns:
            The Stripe customer ID
        """
        if not stripe.api_key:
            return f"mock_customer_{uuid.uuid4().hex[:8]}"

        customer = stripe.Customer.create(
            email=email,
            name=name,
        )
        return customer.id

    async def get_subscription_status(self, user: User) -> str:
        """
        Get current subscription status for a user.
        
        Args:
            user: The User object
            
        Returns:
            Subscription status: "active", "canceled", or "none"
        """
        if not user.stripe_customer_id or not stripe.api_key:
            return user.subscription_status

        try:
            customers = stripe.Customer.list(limit=1, email=user.stripe_customer_id)
            if not customers.data:
                return "none"
                
            customer = customers.data[0]
            subscriptions = stripe.Subscription.list(
                customer=customer.id, status="active", limit=1
            )
            
            if subscriptions.data:
                return "active"
            return "canceled"
        except stripe.error.StripeError:
            return user.subscription_status

    async def handle_subscription_created(
        self, user_id: uuid.UUID, db: AsyncSession
    ) -> User:
        """
        Handle subscription created webhook event.
        
        Args:
            user_id: The User UUID
            db: Database session
            
        Returns:
            Updated User object
        """
        result = await db.execute(select(User).where(User.id == user_id))
        user = result.scalar_one_or_none()
        
        if user:
            user.subscription_status = "active"
            user.sos_credits = DEFAULT_SOS_CREDITS
            await db.commit()
            await db.refresh(user)
        
        return user

    async def handle_subscription_canceled(
        self, user_id: uuid.UUID, db: AsyncSession
    ) -> User:
        """
        Handle subscription canceled webhook event.
        
        Args:
            user_id: The User UUID
            db: Database session
            
        Returns:
            Updated User object
        """
        result = await db.execute(select(User).where(User.id == user_id))
        user = result.scalar_one_or_none()
        
        if user:
            user.subscription_status = "canceled"
            await db.commit()
            await db.refresh(user)
        
        return user

    async def check_sos_credits(self, user: User) -> bool:
        """
        Check if user has available SOS credits.
        
        Args:
            user: The User object
            
        Returns:
            True if user has credits, False otherwise
        """
        return user.sos_credits > 0

    async def deduct_sos_credit(self, user: User, db: AsyncSession) -> bool:
        """
        Deduct one SOS credit from user.
        
        Args:
            user: The User object
            db: Database session
            
        Returns:
            True if deduction successful, False if no credits
        """
        if user.sos_credits <= 0:
            return False
            
        user.sos_credits -= 1
        await db.commit()
        await db.refresh(user)
        return True

    async def reset_sos_credits_if_needed(
        self, user: User, db: AsyncSession
    ) -> User:
        """
        Reset SOS credits if it's been a month since last reset.
        
        Args:
            user: The User object
            db: Database session
            
        Returns:
            Updated User object
        """
        if user.subscription_status != "active":
            return user
            
        now = datetime.now(timezone.utc)
        
        if user.last_sos_reset is None:
            user.sos_credits = DEFAULT_SOS_CREDITS
            user.last_sos_reset = now
        else:
            days_since_reset = (now - user.last_sos_reset).days
            if days_since_reset >= 30:
                user.sos_credits = DEFAULT_SOS_CREDITS
                user.last_sos_reset = now
        
        await db.commit()
        await db.refresh(user)
        return user

    async def update_emotional_profile(
        self, user: User, profile: str, db: AsyncSession
    ) -> User:
        """
        Update user's emotional profile.
        
        Args:
            user: The User object
            profile: Emotional profile ("anxious", "logical", "hopeful")
            db: Database session
            
        Returns:
            Updated User object
        """
        valid_profiles = ["anxious", "logical", "hopeful"]
        if profile.lower() in valid_profiles:
            user.emotional_profile = profile.lower()
            await db.commit()
            await db.refresh(user)
        return user
