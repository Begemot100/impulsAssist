import requests

BASE_URL = "https://tech241224.amocrm.ru"  # Твой AmoCRM домен
ACCESS_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjMzNzg3MTJkZWU1NjA4ODI2YWQyOTMzNjNjNGNmNGU5ODM2OTgwNDk3MzY1NmE0ZjU2ZTQwOWIzZjViYmQwYzI2MzRmMDI3ZWIzNmQyZTQ4In0.eyJhdWQiOiI0Y2RhMWVlNi00ODg5LTQ2YWUtYjU3YS01ZTFiOTZlYTJmY2EiLCJqdGkiOiIzMzc4NzEyZGVlNTYwODgyNmFkMjkzMzYzYzRjZjRlOTgzNjk4MDQ5NzM2NTZhNGY1NmU0MDliM2Y1YmJkMGMyNjM0ZjAyN2ViMzZkMmU0OCIsImlhdCI6MTczOTYyNjU4NywibmJmIjoxNzM5NjI2NTg3LCJleHAiOjE3NTEyNDE2MDAsInN1YiI6IjExOTMzMDI2IiwiZ3JhbnRfdHlwZSI6IiIsImFjY291bnRfaWQiOjMyMTM5OTA2LCJiYXNlX2RvbWFpbiI6ImFtb2NybS5ydSIsInZlcnNpb24iOjIsInNjb3BlcyI6WyJjcm0iLCJmaWxlcyIsImZpbGVzX2RlbGV0ZSIsIm5vdGlmaWNhdGlvbnMiLCJwdXNoX25vdGlmaWNhdGlvbnMiXSwiaGFzaF91dWlkIjoiNDg0NDBlYzQtY2E4Ni00NzYzLTgxZmMtNGVmYjQzNThmMDA0IiwiYXBpX2RvbWFpbiI6ImFwaS1iLmFtb2NybS5ydSJ9.YXEN6xQ6WwqM5rU_lnSLwLOMtgKP0Po-8wbqoC_2-NTyKIaFZnOoAeTBUa8CTu2t5iYDTNY7WRHt1GtTLj2_UHpOGCYs8OH-6kE36_BjovoMFHFizi8eLDxVWNgMtLWKxfkQq_V5vISLr8Vos1Q_Jar2jyefsjzRXTQI1r_XXZTP917mOogHeC_9mKJdbT2zmIBync33fmLUgZ8BDRIRTRvCsROm2oyZn6AmaomUSRf_CAP3EbwjZeVJZL12fKYAKKrROFaMxZLz_v-bqpagkqgwClnGMIaR0vH34_FYkfQvIMAqWYtlAlg7whiOrYxtg9s2RqAtjCX_6dsFGXDDbw"

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