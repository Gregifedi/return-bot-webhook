from flask import Flask, request
import requests
import os

app = Flask(__name__)

# Get bot token from environment variable
TOKEN = os.environ.get("BOT_TOKEN")
API = f"https://api.telegram.org/bot{TOKEN}"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        # This makes the bot reply "You said: <your message>"
        reply = f"You said: {text}"

        requests.post(
            f"{API}/sendMessage",
            json={
                "chat_id": chat_id,
                "text": reply
            }
        )

    return "ok"

if __name__ == "__main__":
    # Bind Flask to the port Render expects
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
