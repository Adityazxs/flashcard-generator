import pandas as pd
import json

def export_to_csv(flashcards, path):
    df = pd.DataFrame(flashcards)
    df.to_csv(path, index=False)

def export_to_json(flashcards, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(flashcards, f, ensure_ascii=False, indent=4)
