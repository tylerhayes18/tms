from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

GROUPME_BOT_ID = os.getenv("GROUPME_BOT_ID")

@app.route("/", methods=["GET"])
def home():
    return "GroupMe bot is running!"

@app.route("/groupme", methods=["POST"])
def groupme_webhook():
    data = request.json
    if data and "text" in data:
        message_text = data["text"]
        sender = data["name"]

        # Simple task detection (modify this logic to suit your needs)
        if "need" in message_text.lower() or "can someone" in message_text.lower():
            task = f"{sender} needs: {message_text}"
            print(task)

            # Send confirmation message to GroupMe
            send_message(f"Task added: {message_text}")

    return jsonify(success=True)

def send_message(text):
    url = "https://api.groupme.com/v3/bots/post"
    data = {"bot_id": GROUPME_BOT_ID, "text": text}
    requests.post(url, json=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
