import requests
import time
import os
# 🔹 Настройки
BASE_URL = "https://tech241224.amocrm.ru"
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

HEADERS = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

# 1️⃣ Найти лида "Кирилл Стрельников"
def find_lead():
    url = f"{BASE_URL}/api/v4/leads?filter[name]=Кирилл Стрельников&page=1&limit=10"
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        print(f"❌ Ошибка API: {response.status_code}")
        return None

    leads = response.json().get("_embedded", {}).get("leads", [])
    if leads:
        lead_id = leads[0]["id"]
        print(f"✅ Найден лид 'Кирилл Стрельников' с ID: {lead_id}")
        return lead_id
    else:
        print("❌ Лид не найден.")
        return None

# 2️⃣ Получить контакт лида
def get_contact(lead_id):
    url = f"{BASE_URL}/api/v4/leads/{lead_id}/contacts"
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        print(f"❌ Ошибка API: {response.status_code}")
        return None

    contacts = response.json().get("_embedded", {}).get("contacts", [])
    if contacts:
        contact_id = contacts[0]["id"]
        print(f"✅ Контакт лида: {contact_id}")
        return contact_id
    else:
        print("❌ Контакт не найден.")
        return None

# 3️⃣ Получить ID чата контакта
def get_chat_id(contact_id):
    url = f"{BASE_URL}/api/v4/contacts/{contact_id}/chats"
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        print(f"❌ Ошибка API: {response.status_code}")
        return None

    chats = response.json().get("_embedded", {}).get("chats", [])
    if chats:
        chat_id = chats[0]["id"]
        print(f"✅ Найден чат ID: {chat_id}")
        return chat_id
    else:
        print("❌ Чат не найден.")
        return None

# 4️⃣ Отправить сообщение в чат
def send_chat_message(chat_id, text):
    url = f"{BASE_URL}/api/v4/chats/{chat_id}/messages"
    payload = {"text": text}

    response = requests.post(url, headers=HEADERS, json=payload)

    if response.status_code == 201:
        print(f"✅ Сообщение '{text}' отправлено в чат!")
    else:
        print(f"❌ Ошибка при отправке сообщения: {response.text}")

CONTACT_ID = 12345678  # ЗАМЕНИТЬ на ID контакта

def get_chat():
    url = f"{BASE_URL}/api/v4/contacts/{CONTACT_ID}/chats"
    response = requests.get(url, headers=HEADERS)

    print(f"🟡 API Response Status: {response.status_code}")
    print(f"🟡 API Response Text: {response.text}")

get_chat()
# 🔄 Автоматический процесс
def main():
    lead_id = find_lead()
    if not lead_id:
        return

    time.sleep(1)  # 🔹 Пауза между запросами

    contact_id = get_contact(lead_id)
    if not contact_id:
        return

    time.sleep(1)  # 🔹 Пауза между запросами

    chat_id = get_chat_id(contact_id)
    if not chat_id:
        return

    time.sleep(1)  # 🔹 Пауза между запросами

    send_chat_message(chat_id, "Привет, Кирилл! Это тестовое сообщение в чат AmoCRM 🤖")

# 🔥 Запуск скрипта
if __name__ == "__main__":
    main()