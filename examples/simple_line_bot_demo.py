import os
from flask import Flask, request, jsonify

app = Flask(__name__)

LINE_CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", "demo_token")


def process_text_command(user_text: str) -> str:
    text = user_text.strip().lower()

    if text == "start":
        return (
            "Available commands:\n"
            "- start\n"
            "- month <number>\n"
            "- send an image to process OCR"
        )

    if text.startswith("month "):
        parts = text.split()
        if len(parts) == 2 and parts[1].isdigit():
            return f"Active month changed to {parts[1]}."
        return "Usage: month 5"

    return "Command received."


def simulate_ocr_result() -> dict:
    return {
        "business_date": "2026/04/05",
        "group_count": 12,
        "adult_count": 28,
        "sales_value": 123456,
    }


@app.route("/callback", methods=["POST"])
def callback():
    data = request.get_json(silent=True) or {}
    events = data.get("events", [])

    results = []

    for event in events:
        if event.get("type") != "message":
            continue

        message = event.get("message", {})
        message_type = message.get("type")

        if message_type == "text":
            user_text = message.get("text", "")
            reply_text = process_text_command(user_text)
            results.append({
                "type": "text",
                "reply": reply_text
            })

        elif message_type == "image":
            ocr_result = simulate_ocr_result()
            reply_text = (
                "OCR processing completed.\n"
                f"Date: {ocr_result['business_date']}\n"
                f"Groups: {ocr_result['group_count']}\n"
                f"Customers: {ocr_result['adult_count']}\n"
                f"Sales: {ocr_result['sales_value']}"
            )
            results.append({
                "type": "image",
                "reply": reply_text
            })

        else:
            results.append({
                "type": message_type,
                "reply": f"Unsupported message type: {message_type}"
            })

    return jsonify({
        "status": "ok",
        "results": results
    })


if __name__ == "__main__":
    app.run(port=5000, debug=True)
