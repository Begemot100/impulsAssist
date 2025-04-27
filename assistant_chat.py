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
ACCESS_TOKEN="eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjQ0ZTViZDc4YTU5ZWE1NmNlYzQ4OTdmOTA3MTJiZWJkMmNhZTBmM2U1YTIwYmUzMDNlN2MzMzg4ZGQwNjdjODkyNWYyYjQ4YWI2NTg0MGY4In0.eyJhdWQiOiI0OTZjY2QwZi0xYTExLTRmYWUtOWJlMy0yMzQ2YTgxZWQ2NmIiLCJqdGkiOiI0NGU1YmQ3OGE1OWVhNTZjZWM0ODk3ZjkwNzEyYmViZDJjYWUwZjNlNWEyMGJlMzAzZTdjMzM4OGRkMDY3Yzg5MjVmMmI0OGFiNjU4NDBmOCIsImlhdCI6MTc0NTc2NjkxMiwibmJmIjoxNzQ1NzY2OTEyLCJleHAiOjE3NTM5MjAwMDAsInN1YiI6IjExOTMzMDI2IiwiZ3JhbnRfdHlwZSI6IiIsImFjY291bnRfaWQiOjMyMTM5OTA2LCJiYXNlX2RvbWFpbiI6ImFtb2NybS5ydSIsInZlcnNpb24iOjIsInNjb3BlcyI6WyJjcm0iLCJmaWxlcyIsImZpbGVzX2RlbGV0ZSIsIm5vdGlmaWNhdGlvbnMiLCJwdXNoX25vdGlmaWNhdGlvbnMiXSwiaGFzaF91dWlkIjoiMmM1ZWExMjktNmY3Mi00ZGFmLWI0ZGUtNGNlODZiYWY2OWYwIiwiYXBpX2RvbWFpbiI6ImFwaS1iLmFtb2NybS5ydSJ9.czWCoR7tBjQtRXeca-hlVGb5z-E2DVGA-6RLIq07i2Azi7HLbWNP0vsBYN82vvCYFfd5XWousEDuz0rf1-2rErnaA_7L__8W5QZgi2-b5qUsg4xOm5RRl2vq9IdLx3Q6rwQxOQuR6fbTx5OVaEflit8GWtXN-AnQh7SNXLUCy-aEnakVevwGwWGz5DjIIwyJapAB_tgA4FVNC4TO80QLOJAX4JDnZ-ufdEEnqsjlYnqSozW5PrmhmC1tMHT10kfM_h9mlMgCPRxpAR1wkfkUuPiAtoProteIlIM6R5dKrjMwVCSSdu5MFwd0vXBBC-wTuPCjZNlKbN6641zeYm7DGw"
# Подключение к OpenAI
client = openai.OpenAI(
    api_key='***REMOVED***proj-pzsfyhV4FKt-3BMHIbxdVGzd3yg_wYgGVd352dve9RqrtT6MzuL_qlIzETvn03JjomYBSVIbhMT3BlbkFJOTK-f_bW6qzUsM0QhSJqeLYx67Kim1JbWlp856txdsGsoqX2e_J3dHVXow_2l14TeaBSuqwnUA')


embeddings = OpenAIEmbeddings(
    api_key = '***REMOVED***proj-pzsfyhV4FKt-3BMHIbxdVGzd3yg_wYgGVd352dve9RqrtT6MzuL_qlIzETvn03JjomYBSVIbhMT3BlbkFJOTK-f_bW6qzUsM0QhSJqeLYx67Kim1JbWlp856txdsGsoqX2e_J3dHVXow_2l14TeaBSuqwnUA')

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
