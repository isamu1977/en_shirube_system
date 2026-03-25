## MODIFIED Requirements
### Requirement: Tarot Library Index Page
The system SHALL provide a browsable library page at `/library` displaying all 78 tarot cards with search and filter functionality, using the standardized Enshirube back image for unrevealed cards.

#### Scenario: Page loads with all cards
- **WHEN** a user navigates to `/library`
- **THEN** all 78 cards are displayed in a responsive grid (3 columns desktop, 2 columns mobile)
- **AND** cards show the standardized `back_cover.png` image as card backs
- **AND** cards fade in with a staggered wave animation

#### Scenario: Cards animate in sequence
- **WHEN** the library page loads
- **THEN** cards appear in sequence with a slight delay (50ms per card)
- **AND** the animation creates a wave-like effect across the grid

#### Scenario: Search filters cards
- **WHEN** a user types in the search input
- **THEN** cards are filtered in real-time by card name matching the search term
- **AND** results update without page reload

#### Scenario: Filter by arcana type
- **WHEN** a user clicks "Major" or "Minor" filter
- **THEN** only cards of the selected arcana type are displayed
- **AND** the filter state is visually indicated as active

#### Scenario: Filter by suit
- **WHEN** a user clicks a suit filter (Wands, Cups, Swords, Pentacles)
- **THEN** only cards of the selected suit are displayed

### Requirement: Individual Card Detail Page
The system SHALL provide a dedicated page at `/library/[slug]` for each card with full information and i18n support, using the standardized back image for loading states.

#### Scenario: Card page loads
- **WHEN** a user navigates to `/library/the-fool`
- **THEN** the page displays the card name, meanings (upright/reversed), love context, and keywords
- **AND** content is displayed in the user's selected language (JA/EN)
- **AND** the card visual uses `back_cover.png` while loading or if image fails

#### Scenario: Image load failure
- **WHEN** a card's front image fails to load
- **THEN** the standardized `back_cover.png` is displayed as fallback
- **AND** no broken image icons are shown

#### Scenario: Invalid slug shows 404
- **WHEN** a user navigates to `/library/invalid-card`
- **THEN** a 404 page is displayed with a link back to the library index

#### Scenario: SEO structured data
- **WHEN** a card detail page is rendered
- **THEN** JSON-LD structured data is included for rich search results
