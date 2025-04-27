import requests
import time

# 🔹 Настройки
BASE_URL = "https://tech241224.amocrm.ru"
ACCESS_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImE0NDZhMGU4YmE0YzEwYThiYmYwZTAzMjU5N2M4MTc1NDlkZTc0ZmRkNmQxYWNjYzdlZmY1Yjg0MTg3MDljMjk1MGJjMGYwZTJmMWYzOGFiIn0.eyJhdWQiOiI0Y2RhMWVlNi00ODg5LTQ2YWUtYjU3YS01ZTFiOTZlYTJmY2EiLCJqdGkiOiJhNDQ2YTBlOGJhNGMxMGE4YmJmMGUwMzI1OTdjODE3NTQ5ZGU3NGZkZDZkMWFjY2M3ZWZmNWI4NDE4NzA5YzI5NTBiYzBmMGUyZjFmMzhhYiIsImlhdCI6MTczOTc0OTE4NSwibmJmIjoxNzM5NzQ5MTg1LCJleHAiOjE3Mzk4MzU1ODUsInN1YiI6IjExOTMzMDI2IiwiZ3JhbnRfdHlwZSI6IiIsImFjY291bnRfaWQiOjMyMTM5OTA2LCJiYXNlX2RvbWFpbiI6ImFtb2NybS5ydSIsInZlcnNpb24iOjIsInNjb3BlcyI6WyJwdXNoX25vdGlmaWNhdGlvbnMiLCJmaWxlcyIsImNybSIsImZpbGVzX2RlbGV0ZSIsIm5vdGlmaWNhdGlvbnMiXSwiaGFzaF91dWlkIjoiYzJjZjhmMzEtNzA3Yy00OGNkLTkwYjMtYTk1YTNjYTZmODk4IiwiYXBpX2RvbWFpbiI6ImFwaS1iLmFtb2NybS5ydSJ9.jFpnMLyUnPXmj6jL8uiYOp0faqcMG31RVleN1kceEiqSDuq7az-qODqW4HwvCqPp92AgPjkU3OWTJju_eWEEjr3qOEMr5-f8sWG_MxulwU2L9F8WAACfBjdJNsCV2Oh4L60gJG-Nxlwsu8gB6oYW0EhpAWt6qRCea9pNxvFZu8BqcPGO58rHlGMN4fpNQUrxzXw_ray0OG0OydpbrmipfFoIs4gW1CDSYYBcWaBB3xbmc9D4QG3VxXF2Mi_3MfgvRoMLVDHClBS5ugL_PQig-t0mvl6NmgF1IXN6WmnMc6o9YBJaqCX7f4jBXp9yNTwkpiQm4ShVimZPbvLgJo-gHw"

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