## ADDED Requirements
### Requirement: Sales Landing Page
The system SHALL provide a high-converting Sales Landing Page to transition users from the free lead magnet to paid readings.

#### Scenario: Visual and Aesthetic Adherence
- **WHEN** the sales page is rendered
- **THEN** it strictly uses soft, calming tones (off-white backgrounds, soft charcoal/deep brown text, muted gold or dusty rose accents)
- **AND** headings utilize a refined Serif font (e.g., Noto Serif JP)
- **AND** there is abundant whitespace to reduce cognitive load
- **AND** elements feature subtle fade-in animations on scroll

#### Scenario: Page Structure and Flow
- **WHEN** a user navigates to the sales page
- **THEN** they are presented with a 6-section vertical flow: Hero, Empathy/Problem Block, Method Explanation, Pricing Cards, Social Proof, and FAQ/Footer
- **AND** the Hero section contains a primary CTA that scrolls to the Pricing section
- **AND** the Empathy block mirrors relationship anxieties
- **AND** the Method section highlights Emotional Analysis, Specific Action, and Total Privacy

#### Scenario: Pricing and Conversion
- **WHEN** the user reaches the Pricing section
- **THEN** they see two distinct options: Standard (7 Cards, ¥4,980) and Premium (12 Cards, ¥12,800)
- **AND** the Premium option includes a "Most Popular" or "Deepest Insight" visual badge
- **AND** clicking the CTA buttons triggers the Stripe Checkout process
