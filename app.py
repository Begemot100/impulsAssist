from flask import Flask, request, render_template, redirect, url_for
from ai_assistant import chat_with_assistant

app = Flask(__name__)

# Список для хранения переписки
chat_history = []


@app.route("/", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        user_message = request.form.get("message")
        if user_message:
            chat_history.append(("Вы", user_message))
            assistant_reply = chat_with_assistant(user_message)
            chat_history.append(("Ассистент", assistant_reply))
        return redirect(url_for('chat'))

    return render_template("chat.html", chat_history=chat_history)


@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        return "Webhook is active", 200
    elif request.method == "POST":
        data = request.json
        print(f"Received data: {data}")
        # Можно добавить входящие данные в чат историю
        chat_history.append(("Webhook", str(data)))
        return {"status": "ok"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005)
