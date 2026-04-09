import re


def extract_receipt_data(ocr_result: dict) -> dict:
    top_text = ocr_result["top_text"]
    sales_text = ocr_result["sales_text"]

    top_lines = [line.strip() for line in top_text.splitlines() if line.strip()]
    sales_lines = [line.strip() for line in sales_text.splitlines() if line.strip()]

    date_match = re.search(r"営業日\s*(\d{4}/\d{2}/\d{2})", top_text)
    business_date = date_match.group(1) if date_match else None

    group_count = None
    group_match = re.search(r"組数\s*(\d+)組", top_text)
    if group_match:
        group_count = int(group_match.group(1))
    else:
        group_match = re.search(r"組\s*(\d+)組", top_text)
        if group_match:
            group_count = int(group_match.group(1))

    adult_count = None

    match = re.search(r"大人人数\s*(\d+)人", top_text)
    if match:
        adult_count = int(match.group(1))

    if adult_count is None:
        match = re.search(r"大人男性\s*(\d+)人", top_text)
        if match:
            adult_count = int(match.group(1))

    if adult_count is None:
        for i, line in enumerate(top_lines):
            if re.search(r"組数?\s*\d+組", line):
                for j in range(i + 1, min(i + 4, len(top_lines))):
                    match = re.search(r"(\d+)人", top_lines[j])
                    if match:
                        adult_count = int(match.group(1))
                        break
                break

    sales_value = None
    in_tax_excluded_block = False

    for line in sales_lines:
        if "売上(税抜)" in line:
            in_tax_excluded_block = True
            continue

        if "売上(税込)" in line and in_tax_excluded_block:
            break

        if in_tax_excluded_block:
            candidates = re.findall(r"[\d][\d,\.]{4,}", line)
            if candidates:
                cleaned_candidates = [re.sub(r"[^\d]", "", c) for c in candidates]
                cleaned_candidates = [c for c in cleaned_candidates if len(c) >= 5]
                if cleaned_candidates:
                    sales_value = int(cleaned_candidates[0])
                    break

    if sales_value is None:
        candidates = re.findall(r"[\d][\d,\.]{4,}", sales_text)
        cleaned_candidates = [re.sub(r"[^\d]", "", c) for c in candidates]
        cleaned_candidates = [c for c in cleaned_candidates if len(c) >= 5]
        if cleaned_candidates:
            sales_value = int(cleaned_candidates[0])

    return {
        "business_date": business_date,
        "group_count": group_count,
        "adult_count": adult_count,
        "sales_value": sales_value,
    }
