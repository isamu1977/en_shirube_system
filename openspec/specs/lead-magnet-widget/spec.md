# lead-magnet-widget Specification

## Purpose
TBD - created by archiving change add-inline-lead-magnet-widget. Update Purpose after archive.
## Requirements
### Requirement: Widget Initial State

The FreeDrawWidget SHALL display an inviting initial state with a card back image and call-to-action text.

#### Scenario: Widget displays card back with invite text

- **WHEN** the widget is mounted
- **THEN** a card back image is displayed with a subtle glow effect
- **AND** the text "彼の本音を 1 枚占う" (Japanese) or "Consultar os sentimentos dele com 1 carta" (English) is shown below the card
- **AND** the widget is clickable (cursor: pointer)

#### Scenario: Widget hover state

- **WHEN** the user hovers over the widget
- **THEN** the glow effect intensifies slightly
- **AND** a subtle scale transform is applied (transform: scale(1.02))

### Requirement: Card Flip Animation on Click

The widget SHALL trigger the existing Card.svelte flip animation when clicked.

#### Scenario: User clicks widget

- **WHEN** the user clicks the card back
- **THEN** the Card.svelte flip animation is triggered (rotateY from 0deg to 180deg)
- **AND** the animation uses cubic-bezier(0.4, 0.0, 0.2, 1) easing with 700ms duration

#### Scenario: Keyboard accessibility

- **WHEN** the widget is focused and user presses Enter or Space
- **THEN** the flip animation is triggered (same as click)

### Requirement: Loading State Display

The widget SHALL show a loading state while fetching the reading from the backend.

#### Scenario: API request in progress

- **WHEN** the card flip completes and API request is pending
- **THEN** a minimalist pulse animation is displayed
- **AND** the text "AI が読み解いています..." (Japanese) or "AI is interpreting..." (English) is shown
- **AND** the pulse animation uses CSS opacity transition (0.5 ↔ 1.0) with 1s interval

### Requirement: Result Display with Text Truncation

The widget SHALL display only the first 2 sentences of the AI interpretation with a CSS fade-to-transparent mask.

#### Scenario: Reading result received

- **WHEN** the backend returns the interpretation text
- **THEN** the text is split by sentence delimiters (。or .)
- **AND** only the first 2 complete sentences are displayed
- **AND** a CSS fade mask is applied: `mask-image: linear-gradient(to bottom, black 50%, transparent 100%)`

#### Scenario: Japanese text truncation

- **WHEN** the interpretation is in Japanese
- **THEN** sentences are split by `。` character
- **AND** the first 2 sentences are shown (e.g., "あなたの彼は今、心の整理をつけている段階です。無理に連絡を取ろうと...")

#### Scenario: English text truncation

- **WHEN** the interpretation is in English
- **THEN** sentences are split by `.` character
- **AND** the first 2 sentences are shown

### Requirement: LINE CTA Button

The widget SHALL display a high-contrast CTA button to redirect users to LINE for the full reading.

#### Scenario: CTA button displayed

- **WHEN** the reading result is shown
- **THEN** a button with text "LINE で全文を無料で読む" (Japanese) or "Ler o texto completo gratuitamente no LINE" (English) is displayed below the faded text
- **AND** the button has high contrast styling (bg: #C5A880, text: #252321)
- **AND** clicking the button redirects to the LINE Official Account URL

#### Scenario: LINE URL placeholder

- **WHEN** the LINE Official Account URL is not yet configured
- **THEN** the button redirects to `https://line.me/` as a placeholder
- **AND** a code comment indicates where the actual URL will be added

### Requirement: Localization Support

The widget SHALL support Japanese (primary) and English (secondary) languages using the existing i18n system.

#### Scenario: Widget displays in Japanese

- **WHEN** the user's locale is set to `ja`
- **THEN** all widget labels (card back text, loading text, CTA text) are displayed in Japanese

#### Scenario: Widget displays in English

- **WHEN** the user's locale is set to `en`
- **THEN** all widget labels are displayed in English

#### Scenario: Language switch

- **WHEN** the user changes language while widget is mounted
- **THEN** all labels update reactively to the new language
- **AND** the current state (initial/loading/result) is preserved

### Requirement: Error Handling

The widget SHALL handle API errors gracefully with a user-friendly error message.

#### Scenario: API request fails

- **WHEN** the backend returns an error (e.g., 500, timeout)
- **THEN** the widget displays an error message: "鑑定に失敗しました。もう一度お試しください。" (Japanese) or "Failed to read. Please try again." (English)
- **AND** the widget resets to the initial state (card back visible)
- **AND** the user can retry by clicking again

### Requirement: Hero Section Integration

The widget SHALL be integrated into the homepage hero section without disrupting the existing design.

#### Scenario: Widget placement in hero

- **WHEN** the homepage (`+page.svelte`) loads
- **THEN** the widget is displayed below the main CTA button ("鑑定メニューを見る")
- **AND** the widget is centered horizontally in the hero section
- **AND** the widget maintains proper spacing on mobile (320px) and desktop viewports

#### Scenario: Mobile responsiveness

- **WHEN** the viewport width is 320px - 768px
- **THEN** the widget scales appropriately (max-width: 280px)
- **AND** the text remains readable

