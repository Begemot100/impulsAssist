import requests
import os

# 🔹 Настройки
BASE_URL = "https://tech241224.amocrm.ru"
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

HEADERS = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

# 1️⃣ Получаем Amojo ID (для чатов)
def get_amojo_id():
    url = f"{BASE_URL}/api/v4/account?with=amojo_id"
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        print(f"❌ Ошибка получения Amojo ID: {response.status_code}")
        return None

    return response.json().get("amojo_id")

# 2️⃣ Регистрируем канал в AmoCRM Чатах
def register_chat_channel(amojo_id):
    if not amojo_id:
        print("❌ Amojo ID не найден")
        return None

    registration_url = f"https://amojo.amocrm.ru/v2/origin/custom/{amojo_id}"
    data = {
        "name": "Тестовый канал",
        "hook_api_version": "v2"
    }

    response = requests.post(registration_url, headers=HEADERS, json=data)

    if response.status_code != 200:
        print(f"❌ Ошибка регистрации канала: {response.status_code}")
        print(response.text)
        return None

    return response.json().get("channel_id")

# 3️⃣ Получаем имя контакта из лида
def get_contact_name(lead_id):
    url = f"{BASE_URL}/api/v4/leads/{lead_id}?with=contacts"
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        print(f"❌ Ошибка получения лида: {response.status_code}")
        return None

    contacts = response.json().get("_embedded", {}).get("contacts", [])
    if not contacts:
        print("❌ Контакты не найдены")
        return None

    contact_id = contacts[0]["id"]  # Берем первый контакт
    contact_url = f"{BASE_URL}/api/v4/contacts/{contact_id}"
    contact_response = requests.get(contact_url, headers=HEADERS)

    if contact_response.status_code != 200:
        print(f"❌ Ошибка получения контакта: {contact_response.status_code}")
        return None

    return contact_response.json().get("name")

# 4️⃣ Отправляем сообщение в чат
def send_chat_message(channel_id, client_name, chat_id):
    if not channel_id:
        print("❌ Канал не зарегистрирован")
        return

    message_url = f"https://amojo.amocrm.ru/v2/origin/custom/{channel_id}/chats/{chat_id}/messages"
    message_data = {
        "event_type": "new_message",
        "payload": {
            "text": f"Привет, {client_name}! Это тестовое сообщение от бота.",
            "type": "text"
        }
    }

    response = requests.post(message_url, headers=HEADERS, json=message_data)

    if response.status_code != 200:
        print(f"❌ Ошибка отправки сообщения: {response.status_code}")
        print(response.text)
    else:
        print(f"✅ Сообщение отправлено: {client_name}")

# 5️⃣ Основной процесс
def main():
    lead_id = 26638991  # ID лида
    chat_id = "ВАШ_CHAT_ID"  # Узнайте chat_id заранее

    amojo_id = get_amojo_id()
    channel_id = register_chat_channel(amojo_id)
    client_name = get_contact_name(lead_id)

    if client_name:
        send_chat_message(channel_id, client_name, chat_id)

if __name__ == "__main__":
    main()