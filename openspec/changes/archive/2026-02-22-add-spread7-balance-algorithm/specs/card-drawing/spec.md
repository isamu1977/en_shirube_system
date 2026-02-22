# card-drawing Specification

## ADDED Requirements

### Requirement: Balanced Spread 7 Draw Algorithm

The system SHALL provide a `draw_balanced_spread_7()` function that randomly selects 7 unique cards from the deck with random orientation (reversed/not reversed), validates the emotional balance using a Challenge Score, and returns a balanced hand or re-rolls if necessary.

#### Scenario: Random card selection
- **WHEN** `draw_balanced_spread_7(db_cards)` is called with a list of 78 Card objects
- **THEN** the function returns exactly 7 unique CardDraw objects
- **AND** each CardDraw has a randomly assigned `is_reversed` value (True/False)

#### Scenario: Challenge Score calculation
- **WHEN** a hand of 7 cards is drawn
- **THEN** the Challenge Score is calculated as:
  - +1 for each card where `is_reversed == True`
  - +1 for each Major Arcana card that is in the hard cards set (Tower, Death, Devil)
- **AND** the total Challenge Score is computed as the sum

#### Scenario: Equilibrium filter - too challenging
- **WHEN** the Challenge Score of a drawn hand is greater than 3
- **THEN** the function discards the hand and re-rolls all 7 cards
- **AND** continues until a hand with Challenge Score <= 3 is obtained

#### Scenario: Equilibrium filter - too perfect
- **WHEN** the Challenge Score of a drawn hand equals 0
- **THEN** the function modifies Position 4 (障害・ブロック/The Obstacle) to be reversed
- **AND** returns the modified hand

#### Scenario: Valid hand returned
- **WHEN** a valid hand (Challenge Score 1-3) is obtained
- **THEN** the function returns a list of 7 CardDraw objects with card_id and is_reversed

### Requirement: Emotional Weight Mapping for Spread 7

The system SHALL map each of the 7 drawn cards to specific positions with associated emotional weights that guide the LLM's tone for that card's interpretation.

#### Scenario: Position 1 - 現在の状況 (Current State)
- **WHEN** a card is assigned to Position 1
- **THEN** the prompt includes instruction: "Neutral. Report the facts of the energy without heavy judgment."

#### Scenario: Position 2 - 彼女の感情 (Her Emotion)
- **WHEN** a card is assigned to Position 2
- **THEN** the prompt includes instruction: "Empathetic/Validating. Focus on validating her anxiety or hope."

#### Scenario: Position 3 - 彼の感情 (His Emotion)
- **WHEN** a card is assigned to Position 3
- **THEN** the prompt includes instruction: "Neutral/Analytical. Explain his distance or confusion logically."

#### Scenario: Position 4 - 障害・ブロック (The Obstacle)
- **WHEN** a card is assigned to Position 4
- **THEN** the prompt includes instruction: "Challenging. Highlight the hard truth or the subconscious block preventing them from being together right now."

#### Scenario: Position 5 - ターニングポイント (Turning Point)
- **WHEN** a card is assigned to Position 5
- **THEN** the prompt includes instruction: "Neutral/Positive. Show where the energy can shift."

#### Scenario: Position 6 - 次のアクション (Next Action)
- **WHEN** a card is assigned to Position 6
- **THEN** the prompt includes instruction: "Positive/Actionable. Give her one highly specific, safe action to take."

#### Scenario: Position 7 - 最終結果・未来 (Probable Outcome)
- **WHEN** a card is assigned to Position 7
- **THEN** the prompt includes instruction: "Lightly Positive + Open-ended. Give hope, but state that energies are fluid."

### Requirement: Retention Trigger Injection

The system SHALL append a mandatory closing paragraph to the System Prompt for the LLM that encourages users to take action within a 14-day window.

#### Scenario: Retention text appended
- **WHEN** generating the system prompt for a standard (Spread 7) reading
- **THEN** the following text is appended at the end:
  "『タロットが示すエネルギーは絶対ではありません。特に行動を起こした場合、約14日間で状況や彼の心理は変化し始めます。焦らず、まずはこの2週間、今回のアドバイスを意識してみてください。』"

#### Scenario: PDF closing paragraph included
- **WHEN** the LLM generates a Spread 7 reading
- **THEN** the response includes the retention trigger paragraph
- **AND** it is positioned as the final closing of the reading
