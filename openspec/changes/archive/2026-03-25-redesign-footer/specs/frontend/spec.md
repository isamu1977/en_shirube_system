## ADDED Requirements

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
