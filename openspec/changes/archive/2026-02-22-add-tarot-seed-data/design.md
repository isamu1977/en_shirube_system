## Context
The Tarot reading functionality mandates 78 discrete cards containing standard definitions plus highly specific romance/psychology orientations (upright and reversed). A JSON seed manifest securely governs this static truth.

## Goals / Non-Goals
- **Goals**: Define the unalterable JSON contract for the tarot cards list. Instruct the generation of the final 78-card `tarot_cards.json` file.
- **Non-Goals**: Editing the PostgreSQL schema or Alembic configuration (abstracted separately).

## Decisions
- **Decision**: The JSON payload maps exactly to the `Card` model. It acts as the single source of truth for the physical seeding procedure. 
- **Language Binding**: Data will initially target Japanese (`name_jp`), mapping fallback english nomenclatures natively into `name_en`. This satisfies early production goals for a Japanese-speaking audience focused on romantic reconciliations.

## Risks / Trade-offs
- **Generation Scale**: Creating 78 dense, psychologically nuanced interpretation strings at once is heavy. 
  - **Mitigation**: We will delegate the full creation of the 78 items to a dedicated LLM script or iterative generation during the implementation (apply) phase.
