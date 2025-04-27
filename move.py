import requests
import os
# 🔹 Настройки
BASE_URL = "https://tech241224.amocrm.ru"
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

# 🔹 ID воронки и статуса AI_agent
AI_AGENT_PIPELINE_ID = 9239766
AI_AGENT_STATUS_ID = 74180478

HEADERS = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

# 🔹 Получаем верхний (первый) лид из "Неразобранное"
def get_top_unprocessed_lead():
    url = f"{BASE_URL}/api/v4/leads?filter[pipeline_id]=9035110&page=1&limit=1"
    response = requests.get(url, headers=HEADERS)
    leads = response.json().get("_embedded", {}).get("leads", [])

    if leads:
        lead = leads[0]  # Берем только первого
        print(f"✅ Найден лид: {lead['id']} - {lead['name']}")
        return lead["id"]
    else:
        print("❌ Нет лидов для перемещения.")
        return None

# 🔹 Переносим лид в AI_agent
def move_lead_to_ai_agent(lead_id):
    if not lead_id:
        print("⚠️ Нет лидов для перемещения.")
        return

    url = f"{BASE_URL}/api/v4/leads"
    payload = [{"id": lead_id, "pipeline_id": AI_AGENT_PIPELINE_ID, "status_id": AI_AGENT_STATUS_ID}]

    response = requests.patch(url, headers=HEADERS, json=payload)
    print("✅ Лид перемещен:", response.json())

# 🔹 Запускаем процесс
lead_id = get_top_unprocessed_lead()
move_lead_to_ai_agent(lead_id)