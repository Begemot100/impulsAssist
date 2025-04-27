import requests
import os
BASE_URL = "https://tech241224.amocrm.ru"  # Твой AmoCRM домен
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

WEBHOOK_URL = "https://13e3-185-209-196-176.ngrok-free.app/webhook"  # Актуальный ngrok URL

# 📌 Новый формат запроса с правильными событиями
webhook_data = {
    "destination": WEBHOOK_URL,
    "events": [
        "add_lead",  # Создание сделки
        "update_lead",  # Обновление сделки
        "delete_lead",  # Удаление сделки
        "add_contact",  # Создание контакта
        "update_contact",  # Обновление контакта
        "delete_contact",  # Удаление контакта
        "add_task",  # Добавление задачи
        "update_task",  # Обновление задачи
        "delete_task"  # Удаление задачи
    ]
}

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

response = requests.post(f"{BASE_URL}/api/v4/webhooks", json=webhook_data, headers=headers)

if response.status_code == 200:
    print("✅ Вебхук успешно зарегистрирован!")
else:
    print(f"❌ Ошибка ({response.status_code}):", response.json())