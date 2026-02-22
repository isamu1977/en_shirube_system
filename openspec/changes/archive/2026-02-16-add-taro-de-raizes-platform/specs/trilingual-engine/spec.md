## ADDED Requirements

### Requirement: Language Selection

The system SHALL allow the user to select their preferred language from PT-BR, Japanese (ja), or English (en) at the start of every session.

#### Scenario: User selects language on landing page

- **WHEN** the user opens the application
- **THEN** a language picker is displayed with three options: Português, 日本語, English
- **AND** the selected language is persisted for the duration of the session

#### Scenario: Default language detection

- **WHEN** the user opens the application without manually selecting a language
- **THEN** the system SHALL attempt to detect the browser's preferred language
- **AND** if the browser language matches PT-BR, JA, or EN, that language is pre-selected
- **AND** if no match is found, English is used as the default

### Requirement: UI Text Localization

The system SHALL render all user-facing interface text (buttons, labels, headings, placeholder text, error messages) in the user's selected language.

#### Scenario: UI renders in selected language

- **WHEN** the user has selected Japanese as their language
- **THEN** all UI elements (navigation, form labels, buttons, headings) are displayed in Japanese

#### Scenario: i18n fallback

- **WHEN** a translation key is missing for the selected language
- **THEN** the system SHALL fall back to the English translation

### Requirement: Trilingual Card Names

The system SHALL display card names in the user's selected language, sourced from the `name_pt`, `name_jp`, or `name_en` columns in the `cards` table.

#### Scenario: Card name in Portuguese

- **WHEN** the user's language is PT-BR
- **AND** the card "the-fool" is displayed
- **THEN** the card name renders as the value from `cards.name_pt`

### Requirement: AI Interpretation Language Routing

The system SHALL instruct the AI model to generate interpretations exclusively in the user's selected language, using culturally appropriate phrasing and tone for each language.

#### Scenario: Interpretation in Japanese

- **WHEN** a reading is requested with language `ja`
- **THEN** the AI prompt includes an instruction to respond in Japanese
- **AND** the returned interpretation text is entirely in Japanese

#### Scenario: Interpretation in Portuguese

- **WHEN** a reading is requested with language `pt-br`
- **THEN** the AI prompt includes an instruction to respond in Brazilian Portuguese
- **AND** the returned interpretation uses Brazilian Portuguese phrasing, not European Portuguese
