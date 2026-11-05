import csv
import json
import re
from pathlib import Path
import json


FIELDS = ["Term", "Definition", "Source"]


def parse_terms(output_text: str) -> list[dict]:
    """Parse the model's JSON, tolerating ```json fences."""
    text = re.sub(r"^```(?:json)?\s*|\s*```$", "", output_text.strip())
    return json.loads(text)["terms"]


def save_terms_csv(terms: list[dict], path: str = "terms.csv") -> int:
    file = Path(path)
    is_new = not file.exists()
    with file.open("a", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        if is_new:
            writer.writerow(FIELDS)
        for t in terms:
            writer.writerow([t["term"], t["definition"], t["source"]])
    return len(terms)