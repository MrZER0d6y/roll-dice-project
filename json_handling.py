import json
from pathlib import Path

DB_FILE = Path(__file__).parent / "game_history.json"

def load_game_history():
    if not DB_FILE.exists():
        print("\nNo database file yet - starting empty")
        return []
    try:
        with open(DB_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("\nDatabase file is corrupted - starting empty")
        return []

def save_game_history(game):
    with open(DB_FILE, "w", encoding="utf-8") as file:
        json.dump(game, file, indent=2, ensure_ascii=False)
    print("\nGame saved successfully!")