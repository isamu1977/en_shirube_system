# Change: Add Emotional Weight & Draw Algorithm for Spread 7

## Why
In the 恋愛/復縁 (Love/Reconciliation) niche, readings that are 100% negative cause churn, and 100% positive stop the retention loop. The current spread 7 (Standard Reading) lacks emotional balance logic, potentially producing unrealistic readings that hurt user retention.

## What Changes
- Create new `services/draw_service.py` with `draw_balanced_spread_7()` function implementing:
  - Random selection of 7 unique cards with random reversed status
  - Challenge Score calculation (hard cards + reversed = higher challenge)
  - Equilibrium filter: re-roll if Challenge Score > 3, force at least 1 reversed if score = 0
- Add emotional weight mapping for all 7 positions in `services/prompt_builder.py`:
  - Position 1 (現在の状況): Neutral
  - Position 2 (彼女の感情): Empathetic/Validating
  - Position 3 (彼の感情): Neutral/Analytical
  - Position 4 (障害・ブロック): Challenging
  - Position 5 (ターニングポイント): Neutral/Positive
  - Position 6 (次のアクション): Positive/Actionable
  - Position 7 (最終結果・未来): Lightly Positive + Open-ended
- Append retention trigger to System Prompt for LLM: mandatory closing paragraph about energy fluidity and 14-day action window

## Impact
- Affected specs: `card-management`, `ai-interpretation`
- Affected code: `backend/app/services/draw_service.py` (new), `backend/app/services/prompt_builder.py` (modified)
