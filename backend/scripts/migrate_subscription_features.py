"""
Migration script to add premium subscription features.

Adds:
- users table with subscription fields
- summary_for_memory column to readings table  
- user_id foreign key to readings table
"""

import psycopg2
import os
import sys
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

DB_USER = os.getenv("POSTGRES_USER", "postgres")
DB_PASS = os.getenv("POSTGRES_PASSWORD", "postgres")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
TARGET_DB = os.getenv("POSTGRES_DB", "en_shirube_system")


def run_migration():
    try:
        conn = psycopg2.connect(
            dbname=TARGET_DB,
            user=DB_USER,
            password=DB_PASS,
            host=DB_HOST,
            port=DB_PORT
        )
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = conn.cursor()

        print("Starting migration...")

        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                stripe_customer_id VARCHAR(100) UNIQUE,
                subscription_status VARCHAR(20) NOT NULL DEFAULT 'none',
                sos_credits INTEGER NOT NULL DEFAULT 0,
                emotional_profile VARCHAR(20),
                last_sos_reset TIMESTAMPTZ,
                created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
                updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
            )
        """)
        print("Created users table")

        cur.execute("""
            ALTER TABLE readings 
            ADD COLUMN IF NOT EXISTS summary_for_memory TEXT
        """)
        print("Added summary_for_memory column to readings")

        cur.execute("""
            ALTER TABLE readings 
            ADD COLUMN IF NOT EXISTS user_id UUID REFERENCES users(id)
        """)
        print("Added user_id column to readings")

        cur.close()
        conn.close()
        
        print("Migration completed successfully!")
        return True

    except Exception as e:
        print(f"Migration error: {e}")
        return False


if __name__ == "__main__":
    success = run_migration()
    if not success:
        sys.exit(1)
