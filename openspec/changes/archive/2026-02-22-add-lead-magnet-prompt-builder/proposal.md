# Change: Add Lead Magnet Prompt Builder

## Why
The LINE Bot lead magnet flow requires a highly specific, 1-card reading focused on "His true feelings" (今の彼の本音). To maintain brand integrity and drive conversions to the paid 7-card reading, the AI response must be empathetic, devoid of cheap occultism, extremely concise (200-300 characters), and always end on a psychological cliffhanger without a final conclusion.

## What Changes
- Introduce a distinct module/service (`services/prompt_builder.py` or equivalent).
- Implement the `build_lead_magnet_prompt` function to enforce strict Japanese formatting and behavioral rules for the LLM.
- Update the `ai-interpretation` spec to formally govern the structure and tone of the Lead Magnet prompt template.

## Impact
- Affected specs: `ai-interpretation`
- Affected code: Creates the new prompt building infrastructure to be called by the `ReadingService`.
