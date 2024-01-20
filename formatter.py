import re


def format_text(text):
    text = text.lower()
    text = text.strip()

    pattern = r"[^\w\s]"
    text = re.sub(pattern, "", text)
    return text
