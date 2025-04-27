from flask import Flask, request

app = Flask(__name__)

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        return "Webhook is active", 200  # Добавляем обработку GET-запроса
    elif request.method == "POST":
        data = request.json
        print(f"Received data: {data}")
        return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)