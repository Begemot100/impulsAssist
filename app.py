from flask import Flask, request, render_template, redirect, session
from ai_assistant import chat_with_assistant
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "supersecretkey")  # для сессий

@app.route("/", methods=["GET", "POST"])
def chat():
    if request.method == "GET":
        # При новом заходе на страницу очищаем сессию
        session['chat_history'] = []
        session['waiting_for_language'] = True  # Снова спросить язык
        session['waiting_for_client_info'] = False
        session['client_data_temp'] = {}
        session['current_lang'] = None

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
        if 'chat_history' not in session:
            session['chat_history'] = []
        session['chat_history'].append(("Webhook", str(data)))
        return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005)

