from flask import Flask, request, render_template, redirect, url_for, session
from ai_assistant import chat_with_assistant
import os


app = Flask(__name__)
app.secret_key = os.environ.get('supersecretkey123', 'supersecretkey')

# Список для хранения переписки
chat_history = []


@app.route("/", methods=["GET", "POST"])
def chat():
    if 'chat_history' not in session:
        session['chat_history'] = []

    if request.method == "POST":
        user_message = request.form["message"]
        assistant_reply = chat_with_assistant(user_message)
        session['chat_history'] = assistant_reply['chat_history']  # Обновляем в сессии

        return redirect("/")

    return render_template("chat.html", chat_history=session.get('chat_history', []))


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
