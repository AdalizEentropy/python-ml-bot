import re


def filter_text(text):
    text = text.lower()
    text = text.strip()

    pattern = r"[^\w\s]"
    text = re.sub(pattern, "", text)
    return text