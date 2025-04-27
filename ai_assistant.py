import requests
import openai
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langdetect import detect
import re
import json
import unicodedata
from knowledge_base import knowledge_base
import time
import os


# Если нет базы и модели, временно отключим их импорты
# from ai_assistant import ClientInquiry, session  # ❌ Убрал для чистоты (если тебе надо — включишь)

# Данные AmoCRM
AMOCRM_BASE_URL = "https://tech241224.amocrm.ru"
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

# Подключение к OpenAI
client = openai.OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

embeddings = OpenAIEmbeddings(
    openai_api_key=os.getenv("OPENAI_API_KEY")
)
waiting_for_client_info = False
client_data_temp = {}

# История чата
# Глобальные переменные
chat_history = []
waiting_for_client_info = False
waiting_for_language = True
client_data_temp = {}
current_lang = None


headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

response = requests.get(f"{AMOCRM_BASE_URL}/api/v4/leads/pipelines/{9239766}", headers=headers)
print(json.dumps(response.json(), indent=2, ensure_ascii=False))
# ===== Вспомогательные функции =====

def clean_text(text):
    return "".join(c for c in unicodedata.normalize("NFKD", text) if ord(c) < 0xFFFF)

def detect_language(prompt):
    try:
        return detect(prompt)
    except:
        return "es"

def calculate_typing_delay(text):
    typing_speed = 25  # символов в секунду
    delay = len(text) / typing_speed
    return min(delay, 5)

def detect_language_choice(prompt):
    prompt_lower = prompt.lower()
    if "рус" in prompt_lower or "ru" in prompt_lower:
        return "ru"
    elif "esp" in prompt_lower or "español" in prompt_lower or "es" in prompt_lower:
        return "es"
    elif "english" in prompt_lower or "en" in prompt_lower:
        return "en"
    return None

def send_greeting(lang):
    if lang == "ru":
        return "Здравствуйте! Чем могу помочь вам сегодня? 🌸"
    elif lang == "es":
        return "¡Hola! ¿En qué puedo ayudarle hoy? 🌸"
    else:
        return "Hello! How can I assist you today? 🌸"

def get_system_message(lang):
    if lang == "ru":
        return (
            "Ты — вежливая и доброжелательная девушка-администратор клиники эстетической медицины IMPULS. "
            "Не предлагаешь звонить. Сама собираешь данные для записи: имя и телефон. "
            "Если спрашивают телефон, указывай: '+34 66 22 66 999'. "
            "Если спрашивают адрес, для Барселоны отвечай: 'Pl. d'Urquinaona, 6, Piso14, A1, 08010 Barcelona'. "
            "Для Таррагоны: 'Pl. de la Generalitat, 1, Local 7, 43005 Tarragona'. "
            "Отвечай тепло, дружелюбно и профессионально на русском языке."
        )
    elif lang == "es":
        return (
            "Eres una amable recepcionista de la clínica estética IMPULS. "
            "No ofreces llamar. Tú misma recoges nombre y teléfono para la cita. "
            "Teléfono: '+34 66 22 66 999'. "
            "Dirección en Barcelona: 'Pl. d'Urquinaona, 6, Piso14, A1, 08010 Barcelona'. "
            "Dirección en Tarragona: 'Pl. de la Generalitat, 1, Local 7, 43005 Tarragona'. "
            "Contesta cálidamente y de forma profesional en español."
        )
    else:
        return (
            "You are a polite and friendly female receptionist of the IMPULS aesthetic clinic. "
            "Do not offer to call. Collect name and phone number directly. "
            "Phone: '+34 66 22 66 999'. "
            "Barcelona address: 'Pl. d'Urquinaona, 6, Piso14, A1, 08010 Barcelona'. "
            "Tarragona address: 'Pl. de la Generalitat, 1, Local 7, 43005 Tarragona'. "
            "Always answer warmly and professionally in English."
        )

def parse_info_from_prompt(prompt):
    global client_data_temp
    print(f"🔍 Парсим данные из сообщения: {prompt}")

    # Ищем телефон
    phone_match = re.search(r"(\+?\d{7,15})", prompt)
    if phone_match:
        client_data_temp["phone"] = phone_match.group()
        print(f"✅ Телефон найден: {client_data_temp['phone']}")

    # Ищем имя (первое слово без цифр и символов)
    words = prompt.split()
    name_candidates = [word for word in words if word.isalpha() and len(word) > 1]
    if name_candidates:
        client_data_temp["name"] = name_candidates[0]
        print(f"✅ Имя найдено: {client_data_temp['name']}")

def format_chat_history(chat_history):
    """Форматирует историю чата для записи в заметку AmoCRM."""
    dialogue = ""
    for message in chat_history:
        role = "👤 Клиент" if message["role"] == "user" else "🤖 Ассистент"
        dialogue += f"{role}: {message['content']}\n"
    return dialogue.strip()

def create_lead_with_chat(name, phone, chat_history):
    print("➡️ Отправка сделки в AmoCRM...")

    contact_id = create_contact(name, phone)
    if not contact_id:
        print("❌ Сделка не может быть создана без контакта.")
        return False

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    lead_data = [
        {
            "name": f"Запись {name}",
            "pipeline_id": 9239766,
            "status_id": 74180478,
            "_embedded": {
                "contacts": [
                    {
                        "id": contact_id  # ✅ Только ID контакта
                    }
                ],
                "notes": [
                    {
                        "note_type": "common",
                        "params": {
                            "text": format_chat_history(chat_history)
                        }
                    }
                ]
            }
        }
    ]

    print(f"📋 Создаём сделку с данными: {json.dumps(lead_data, indent=2, ensure_ascii=False)}")

    response = requests.post(f"{AMOCRM_BASE_URL}/api/v4/leads", headers=headers, json=lead_data)

    print(f"📥 Ответ от AmoCRM: {response.status_code} {response.text}")

    if response.status_code in [200, 201]:
        print("✅ Сделка успешно создана в AmoCRM.")
        return True
    else:
        print("❌ Ошибка при создании сделки в AmoCRM.")
        return False


# ===== Основная функция =====
from flask import session
import time
# .
def chat_with_assistant(prompt):
    global waiting_for_client_info, waiting_for_language, client_data_temp, current_lang

    if 'chat_history' not in session:
        session['chat_history'] = []

    if prompt is None:
        # 🧹 Полная очистка истории при первом заходе
        session['chat_history'] = []
        chat_history = []

        greeting = send_greeting(current_lang)
        chat_history.append({"role": "assistant", "content": greeting})
        session['chat_history'] = chat_history
        return {
            "assistant_reply": greeting,
            "chat_history": chat_history
        }

    # Обычная работа
    chat_history = session['chat_history']

    prompt = clean_text(prompt)
    print(f"💬 Пользователь: {prompt}")

    chat_history.append({"role": "user", "content": prompt})

    system_message = get_system_message(current_lang)
    messages = [{"role": "system", "content": system_message}] + chat_history

    # Сначала ищем ответ в базе знаний
    docs = db.similarity_search(prompt, k=2)

    if docs and any(doc.page_content.strip() for doc in docs):
        knowledge_text = "\n\n".join(doc.page_content for doc in docs)
        assistant_reply = f"Вот, что я нашла по вашему запросу:\n\n{knowledge_text}"
    else:
        # Если в базе ничего нет — спрашиваем у GPT
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=messages,
            max_tokens=500
        )
        assistant_reply = clean_text(response.choices[0].message.content.strip())

    print(f"🤖 Ассистент: {assistant_reply}")

    # Проверка — нужно ли запросить имя и телефон
    if any(word in prompt.lower() for word in ["запис", "консультац", "удалить", "appointment", "consultation", "tattoo removal"]):
        waiting_for_client_info = True
        assistant_reply += "\n\n" + {
            "ru": "Пожалуйста, напишите ваше имя и номер телефона для предварительной записи. 📞",
            "es": "Por favor, escriba su nombre y número de teléfono para la reserva preliminar. 📞",
            "en": "Please write your name and phone number for the preliminary booking. 📞"
        }.get(current_lang, "Пожалуйста, укажите ваше имя и номер телефона. 📞")

    if waiting_for_client_info:
        parse_info_from_prompt(prompt)
        if client_data_temp.get("name") and client_data_temp.get("phone"):
            contact_id = create_contact(client_data_temp["name"], client_data_temp["phone"])
            if contact_id:
                lead_id = create_lead(client_data_temp["name"], contact_id)
                if lead_id:
                    create_note_for_lead(lead_id, format_chat_history(chat_history))
            waiting_for_client_info = False
            client_data_temp = {}

    chat_history.append({"role": "assistant", "content": assistant_reply})
    session['chat_history'] = chat_history[-10:]
    time.sleep(calculate_typing_delay(assistant_reply))

    return {
        "assistant_reply": assistant_reply,
        "chat_history": chat_history
    }


def create_contact(name, phone):
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    data = [
        {
            "first_name": name,
            "custom_fields_values": [
                {
                    "field_id": 949379,
                    "values": [{"value": phone}]
                }
            ]
        }
    ]
    response = requests.post(f"{AMOCRM_BASE_URL}/api/v4/contacts", headers=headers, json=data)

    if response.status_code in [200, 201]:
        contact_id = response.json()["_embedded"]["contacts"][0]["id"]
        print(f"✅ Контакт создан: ID = {contact_id}")
        return contact_id
    else:
        print(f"❌ Ошибка при создании контакта: {response.status_code} {response.text}")
        return None


def create_lead(name, contact_id):
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    data = [
        {
            "name": f"Запись {name}",
            "pipeline_id": 9239766,
            "status_id": 74180478,
            "_embedded": {
                "contacts": [
                    {"id": contact_id}
                ]
            }
        }
    ]
    response = requests.post(f"{AMOCRM_BASE_URL}/api/v4/leads", headers=headers, json=data)

    if response.status_code in [200, 201]:
        lead_id = response.json()["_embedded"]["leads"][0]["id"]
        print(f"✅ Сделка создана: ID = {lead_id}")
        return lead_id
    else:
        print(f"❌ Ошибка при создании сделки: {response.status_code} {response.text}")
        return None


def create_note_for_lead(lead_id, chat_text):
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    note_data = [
        {
            "entity_id": lead_id,
            "note_type": "common",
            "params": {
                "text": chat_text
            }
        }
    ]
    response = requests.post(f"{AMOCRM_BASE_URL}/api/v4/leads/notes", headers=headers, json=note_data)

    if response.status_code in [200, 201]:
        print(f"✅ Заметка добавлена к сделке {lead_id}")
    else:
        print(f"❌ Ошибка при создании заметки: {response.status_code} {response.text}")
