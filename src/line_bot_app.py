from flask import Flask, request
import os
import json
import requests
from datetime import datetime

from receipt_processor import process_receipt_image

app = Flask(__name__)

CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")

if not CHANNEL_ACCESS_TOKEN:
    raise ValueError("LINE_CHANNEL_ACCESS_TOKEN is not set.")

REPLY_API_URL = "https://api.line.me/v2/bot/message/reply"
CONTENT_API_BASE = "https://api-data.line.me/v2/bot/message"


def reply_message(reply_token: str, text: str) -> None:
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {CHANNEL_ACCESS_TOKEN}",
    }

    payload = {
        "replyToken": reply_token,
        "messages": [
            {
                "type": "text",
                "text": text
            }
        ]
    }

    requests.post(REPLY_API_URL, headers=headers, json=payload)


def save_image_from_line(message_id: str) -> str:
    headers = {
        "Authorization": f"Bearer {CHANNEL_ACCESS_TOKEN}"
    }

    url = f"{CONTENT_API_BASE}/{message_id}/content"
    response = requests.get(url, headers=headers, stream=True)

    if response.status_code != 200:
        raise ValueError(f"Failed to fetch image: {response.status_code}")

    images_dir = "images"
    os.makedirs(images_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(images_dir, f"line_image_{timestamp}.jpg")

    with open(file_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)

    return file_path


def handle_command(user_text: str) -> str:
    text = user_text.strip()

    if text.startswith("month "):
        parts = text.split()
        if len(parts) != 2 or not parts[1].isdigit():
            return "Usage: month 5"
        return f"Active month changed to {int(parts[1])}."

    if text == "start":
        return (
            "Available commands:\n"
            "- start\n"
            "- month <number>\n"
            "- send an image to process OCR"
        )

    return "Command received."


@app.route("/callback", methods=["POST"])
def callback():
    body = request.get_data(as_text=True)
    data = json.loads(body)
    events = data.get("events", [])

    for event in events:
        if event.get("type") != "message":
            continue

        reply_token = event.get("replyToken")
        message = event.get("message", {})
        message_type = message.get("type")

        if message_type == "text":
            user_text = message.get("text", "")
            reply_text = handle_command(user_text)
            reply_message(reply_token, reply_text)

        elif message_type == "image":
            try:
                message_id = message.get("id")
                saved_path = save_image_from_line(message_id)
                result = process_receipt_image(saved_path)

                reply_text = (
                    "OCR processing completed.\n"
                    f"Date: {result.get('business_date')}\n"
                    f"Groups: {result.get('group_count')}\n"
                    f"Customers: {result.get('adult_count')}\n"
                    f"Sales: {result.get('sales_value')}"
                )
                reply_message(reply_token, reply_text)

            except Exception as e:
                reply_message(reply_token, f"Processing failed: {str(e)}")

        else:
            reply_message(reply_token, f"Unsupported message type: {message_type}")

    return "OK"


if __name__ == "__main__":
    app.run(port=5000)
