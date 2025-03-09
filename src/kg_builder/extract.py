def extract_entities(text: str) -> list[str]:
    words = [w.strip(".,") for w in text.split()]
    return [w for w in words if w.istitle()]
