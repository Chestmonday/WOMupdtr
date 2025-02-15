import json
import os

# JSON file for storing player ranks
RANKS_FILE = "player_ranks.json"

def load_ranks():
    """Load ranks from a JSON file."""
    if os.path.exists(RANKS_FILE):
        try:
            with open(RANKS_FILE, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, ValueError):
            print(f"Error: {RANKS_FILE} is empty or corrupted. Resetting data.")
            return {}
    return {}

def save_ranks(data):
    """Save ranks to a JSON file."""
    with open(RANKS_FILE, 'w') as f:
        json.dump(data, f, indent=4)
