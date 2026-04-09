import re

def extract_sales(text):
    match = re.search(r"\d+", text)
    return match.group() if match else None
