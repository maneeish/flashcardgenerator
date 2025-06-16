import re
import pandas as pd
from collections import defaultdict

def parse_flashcards(raw_text):
    """
    Parses raw LLM output and groups flashcards under detected section headers.
    Now also includes difficulty levels.
    
    Expected format:
    # Section Title (optional)
    Q: Question
    A: Answer
    Difficulty: Easy | Medium | Hard
    """
    sections = defaultdict(list)
    current_section = "General"
    current_card = {}

    for line in raw_text.splitlines():
        line = line.strip()

        if not line:
            continue

        # Section Header
        if re.match(r"#+\s*", line):
            current_section = re.sub(r"#+\s*", "", line)

        elif line.startswith("Q:"):
            current_card["question"] = line[2:].strip()

        elif line.startswith("A:"):
            current_card["answer"] = line[2:].strip()

        elif line.startswith("Difficulty:"):
            current_card["difficulty"] = line[len("Difficulty:"):].strip().capitalize()

            # Only add if question and answer are present
            if "question" in current_card and "answer" in current_card:
                sections[current_section].append(current_card)
            current_card = {}

    return dict(sections)

def export_flashcards(cards_by_section, format="csv"):
    """
    Exports grouped flashcards into CSV or JSON format, including difficulty levels.
    """
    flat_cards = []
    for section, cards in cards_by_section.items():
        for card in cards:
            flat_cards.append({
                "section": section,
                "question": card.get("question", ""),
                "answer": card.get("answer", ""),
                "difficulty": card.get("difficulty", "Medium")  # default fallback
            })

    df = pd.DataFrame(flat_cards)

    if format == "csv":
        return df.to_csv(index=False).encode("utf-8")

    elif format == "json":
        return df.to_json(orient="records", indent=2).encode("utf-8")

    else:
        raise ValueError("Unsupported export format.")
