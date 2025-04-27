from flask import Flask, request, render_template, redirect, session
from ai_assistant import chat_with_assistant
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "supersecretkey")  # для сессий

@app.route("/", methods=["GET", "POST"])
def chat():
    if 'chat_history' not in session:
        session['chat_history'] = []

    if request.method == "POST":
        user_message = request.form["message"]
        result = chat_with_assistant(user_message)
        session['chat_history'] = result['chat_history']
        return redirect("/")

    # ⚡ Если GET-запрос, а переписки нет => сгенерировать приветствие
    if not session['chat_history']:
        result = chat_with_assistant(None)
        session['chat_history'] = result['chat_history']

    return render_template("chat.html", chat_history=session.get('chat_history', []))


@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        return "Webhook is active", 200
    elif request.method == "POST":
        data = request.json
        if 'chat_history' not in session:
            session['chat_history'] = []
        session['chat_history'].append(("Webhook", str(data)))
        return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005)

