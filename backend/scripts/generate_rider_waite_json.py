import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]  # backend/
CARDS_DIR = BASE_DIR / "seeds" / "cards"
OUTPUT_FILE = BASE_DIR / "seeds" / "cards_data.json"

FILES_ORDER = ["major.json", "cups.json", "swords.json", "wands.json", "pentacles.json"]

REQUIRED_FIELDS = [
    "id",
    "arcana_type",
    "suit",
    "card_number",
    "image_url",
    "element",
    "logic_tags",
    "energy_type",
    "relationship_bias",
    "name",
    "keywords",
    "meanings"
]

def load_json(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)

def validate_card(card: dict, source: str):
    missing = [k for k in REQUIRED_FIELDS if k not in card]
    if missing:
        raise ValueError(f"[{source}] Card '{card.get('id')}' missing fields: {missing}")

    # Validar subcampos mínimos
    if not isinstance(card["name"], dict) or "jp" not in card["name"] or "en" not in card["name"] or "pt" not in card["name"]:
        raise ValueError(f"[{source}] Card '{card.get('id')}' invalid 'name' structure")

    if not isinstance(card["meanings"], dict) or "upright" not in card["meanings"] or "reversed" not in card["meanings"]:
        raise ValueError(f"[{source}] Card '{card.get('id')}' invalid 'meanings' structure")

    if not isinstance(card["relationship_bias"], dict):
        raise ValueError(f"[{source}] Card '{card.get('id')}' relationship_bias must be dict")

def main():
    all_cards = []
    seen_ids = set()

    for filename in FILES_ORDER:
        path = CARDS_DIR / filename
        data = load_json(path)

        if not isinstance(data, list):
            raise ValueError(f"{filename} must contain a JSON array")

        for card in data:
            validate_card(card, filename)
            cid = card["id"]
            if cid in seen_ids:
                raise ValueError(f"Duplicate card id '{cid}' found in {filename}")
            seen_ids.add(cid)
            all_cards.append(card)

    if len(all_cards) != 78:
        raise ValueError(f"Expected 78 cards, got {len(all_cards)}")

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_FILE.open("w", encoding="utf-8") as f:
        json.dump(all_cards, f, indent=2, ensure_ascii=False)

    print(f"OK: wrote {len(all_cards)} cards to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()