import requests
import openai
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langdetect import detect
import re
import json
import unicodedata

# Если нет базы и модели, временно отключим их импорты
# from ai_assistant import ClientInquiry, session  # ❌ Убрал для чистоты (если тебе надо — включишь)

# Данные AmoCRM
AMOCRM_BASE_URL = "https://tech241224.amocrm.ru"
# Подключение к OpenAI

global chat_history

# История чата
chat_history = []
client_data = {"name": None, "phone": None, "email": None, "reason": None}

# --- Функции ---

def detect_language(text):
    try:
        lang = detect(text)
        if lang == "ru":
            return "ru"
        elif lang == "es":
            return "es"
        elif lang == "en":
            return "en"
        else:
            return "en"
    except:
        return "en"

def clean_text(text):
    return "".join(c for c in unicodedata.normalize("NFKD", text) if ord(c) < 0xFFFF)

def parse_client_info(prompt):
    words = prompt.split()
    extracted_data = {"name": None, "phone": None, "email": None, "reason": None}

    for word in words:
        if "@" in word:
            extracted_data["email"] = word
        elif word.isdigit() and len(word) > 6:
            extracted_data["phone"] = word
        elif len(word) > 2:
            if not extracted_data["name"]:
                extracted_data["name"] = word
            else:
                extracted_data["reason"] = word if not extracted_data["reason"] else f"{extracted_data['reason']} {word}"

    return extracted_data

def create_contact(name, phone=None, email=None, reason=None):
    if not name or (not phone and not email):
        print("❌ Недостаточно данных для создания контакта.")
        return None

    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}", "Content-Type": "application/json"}

    custom_fields = []
    if phone:
        custom_fields.append({"field_id": 949379, "values": [{"value": phone, "enum_id": 682997}]})
    if email:
        custom_fields.append({"field_id": 949381, "values": [{"value": email, "enum_id": 683005}]})
    if reason:
        custom_fields.append({"field_id": 1002227, "values": [{"value": reason}]})

    data = [{"name": name, "custom_fields_values": custom_fields}]
    response = requests.post(f"{AMOCRM_BASE_URL}/api/v4/contacts", headers=headers, json=data)

    print(f"📥 Ответ AmoCRM (status {response.status_code}): {response.text}")
    return response.json() if response.status_code in [200, 201] else None

# --- Основная функция общения ---

def chat_with_assistant(prompt):
    global chat_history

    prompt = clean_text(prompt)
    print(f"💬 Пользователь: {prompt}")

    client_info = parse_client_info(prompt)

    # Сохраняем диалог
    chat_history.append({"role": "user", "content": prompt})
    messages = [{"role": "system", "content": "Ты — виртуальный администратор клиники, отвечаешь вежливо и понятно."}] + chat_history

    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=messages,
        max_tokens=500
    )

    assistant_reply = clean_text(response.choices[0].message.content.strip())
    print(f"🤖 Ассистент: {assistant_reply}")

    chat_history.append({"role": "assistant", "content": assistant_reply})

    # Создаём контакт в AmoCRM
    if client_info["name"] and (client_info["phone"] or client_info["email"]):
        create_contact(client_info["name"], client_info["phone"], client_info["email"], client_info["reason"])

    return assistant_reply
