import re


def extract_location(text: str) -> str | None:
    match = re.search(r"thoi\s+tiet\s+(.+?)(?:\s+hom\s+nay|$)", text, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return None
