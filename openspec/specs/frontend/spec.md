# frontend Specification

## Purpose
TBD - created by archiving change add-reading-result-ui. Update Purpose after archive.
## Requirements
### Requirement: Reading Result Page

The system SHALL provide a dedicated page for displaying reading results at /reading/[session_id].

#### Scenario: Page loads with valid session

- **WHEN** a user navigates to /reading/{session_id} with a valid session ID
- **THEN** the page fetches reading data from the API
- **AND** displays the SpreadBoard component

#### Scenario: Page loads with invalid session

- **WHEN** a user navigates to /reading/{invalid_session_id}
- **THEN** an error message is displayed
- **AND** a link back to home is provided

### Requirement: ReadingText Markdown Rendering

The system SHALL render the LLM interpretation text as beautifully formatted Markdown.

#### Scenario: Markdown sections rendered

- **WHEN** interpretation text is provided
- **THEN** the component renders Markdown with proper headings, paragraphs, lists
- **AND** each major section has a soft background card for readability

#### Scenario: Text fades in after cards

- **WHEN** the last card flip animation completes
- **THEN** the ReadingText component fades in with a smooth transition
- **AND** uses Svelte's transition:fade directive

### Requirement: Minimalist Aesthetic

The UI SHALL follow a minimalist, elegant design suitable for the target audience (Japanese women 20-45).

#### Scenario: Design follows guidelines

- **WHEN** the reading result page is rendered
- **THEN** plenty of whitespace is used
- **AND** refined typography (Mincho fonts for Japanese) is applied
- **AND** soft transitions are used throughout

#### Scenario: No dark/heavy styling

- **WHEN** the design is rendered
- **THEN** dark, heavy, or overly occult aesthetics are avoided
- **AND** colors are soft and calming

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

### Requirement: API Service Integration

The frontend SHALL provide a standardized API service layer (`src/lib/api.ts`) for communicating with the backend.

#### Scenario: Generate Reading Request
- **WHEN** `api.generateReading()` is called with a spread type and optional session ID
- **THEN** it sends a POST request to `$PUBLIC_API_BASE_URL/readings/generate`
- **AND** it handles network or 500 errors gracefully by returning an error state so the UI doesn't crash

### Requirement: Test UI for Reading Generation

The system SHALL provide a temporary test route (`/test-reading`) to verify end-to-end integration without final styling.

#### Scenario: Generating a test reading
- **WHEN** a user selects a spread type and clicks "Generate Reading"
- **THEN** a loading indicator "サーバーと通信中..." is displayed
- **AND** upon success, the drawn cards and formatted Markdown interpretation are displayed
- **AND** upon failure, an error message is displayed

### Requirement: SvelteKit Foundation Theming and Structure
The frontend SHALL implement a cohesive design system and provide a reliable API client interface for backend communication.

#### Scenario: Global Layout and Theming
- **WHEN** the user accesses any page
- **THEN** they see an elegant, mobile-first design with the "縁しるべ" header, using the defined charcoal text, off-white background, and serif typography.

#### Scenario: API Communication
- **WHEN** the frontend needs to request a reading
- **THEN** it uses the unified API client to abstract the network request, applying global environment variables for the base URL and handling errors consistently.

### Requirement: AI Science Explainer Section
The frontend SHALL display a section explaining the AI × Psychology methodology to build authority and differentiation.

#### Scenario: User views the AI Science section
- **WHEN** the user scrolls past Social Proof
- **THEN** they see a two-column layout with heading "AIと心理学の融合" and a description of the 感情分析エンジン methodology.

### Requirement: FAQ Accordion Component
The frontend SHALL provide an accordion FAQ section that addresses common objections with smooth slide animations.

#### Scenario: User expands a FAQ item
- **WHEN** the user clicks on a FAQ question
- **THEN** the answer expands with a smooth slide transition, and only one item is open at a time.

### Requirement: Testimonials Data Module
The frontend SHALL maintain testimonials in a dedicated typed data module separate from view components.

#### Scenario: Testimonial data is imported into a component
- **WHEN** `TestimonialsCarousel` is rendered
- **THEN** it imports all testimonials from `$lib/data/testimonials` and renders each one.

### Requirement: Animated Testimonials Carousel
The frontend SHALL replace the static testimonials grid with a single-card auto-rotating carousel that preserves the Dark Elegance visual style.

#### Scenario: Auto-advance on idle
- **WHEN** the testimonials section is visible and the user has not interacted
- **THEN** the active testimonial changes every 5 seconds with a fade transition.

#### Scenario: Pause on hover
- **WHEN** the user hovers over the carousel
- **THEN** auto-advance is suspended until the pointer leaves.

#### Scenario: Manual navigation via dots or arrows
- **WHEN** the user clicks a dot indicator or prev/next arrow
- **THEN** the carousel immediately fades to the selected testimonial and resets the auto-advance timer.

#### Scenario: Reduced motion
- **WHEN** `prefers-reduced-motion: reduce` is set in the OS
- **THEN** auto-advance is disabled and transitions are instant.

### Requirement: Home Page (Landing Page) Structure
The frontend SHALL provide a compelling, single-page scrolling landing page at the root route that clearly communicates the value proposition and pricing.

#### Scenario: User visits the root URL
- **WHEN** the user navigates to `/`
- **THEN** they see the Hero section, Empathy section, Method section, Pricing cards, and Social Proof reviews, styled with the cohesive "Japanese Minimalist" design system.

#### Scenario: User selects a reading package
- **WHEN** the user clicks a CTA button in the pricing section
- **THEN** they are directed to the corresponding Stripe Checkout URL for either the 7-card or 12-card reading.

### Requirement: Editorial Footer Component
The system SHALL provide a 3-column responsive footer component with brand identity, navigation, and legal links.

#### Scenario: Footer displays on all pages
- **WHEN** the user views any page
- **THEN** the footer appears at the bottom with a 3-column grid layout (stacked on mobile)
- **AND** the background color is #1A1918 (darker than main content)

#### Scenario: Brand column displays correctly
- **WHEN** the footer renders
- **THEN** Column 1 shows "縁しるべ" in large serif font
- **AND** displays the tagline "AIと心理学が紡ぐ、あなただけの心の羅針盤。"
- **AND** shows Threads and LINE social icons

#### Scenario: Navigation column links work
- **WHEN** the user clicks a link in the Menu section
- **THEN** they navigate to the corresponding page (Home, Library, About)

#### Scenario: Support column displays legal links
- **WHEN** the footer renders
- **THEN** Column 3 shows Contact, Tokushoho, Privacy Policy, and Terms links
- **AND** each link has proper href attributes

#### Scenario: Bottom bar shows language toggle
- **WHEN** the footer renders
- **THEN** the bottom bar shows JP | EN language toggle with gold underline on active language
- **AND** displays copyright "© 2026 縁しるべ. All rights reserved."

#### Scenario: Responsive behavior
- **WHEN** the viewport is mobile (<768px)
- **THEN** the 3 columns stack vertically with reduced padding
- **AND** content remains centered and readable

