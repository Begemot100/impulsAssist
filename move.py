import requests

# 🔹 Настройки
BASE_URL = "https://tech241224.amocrm.ru"
ACCESS_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImE0NDZhMGU4YmE0YzEwYThiYmYwZTAzMjU5N2M4MTc1NDlkZTc0ZmRkNmQxYWNjYzdlZmY1Yjg0MTg3MDljMjk1MGJjMGYwZTJmMWYzOGFiIn0.eyJhdWQiOiI0Y2RhMWVlNi00ODg5LTQ2YWUtYjU3YS01ZTFiOTZlYTJmY2EiLCJqdGkiOiJhNDQ2YTBlOGJhNGMxMGE4YmJmMGUwMzI1OTdjODE3NTQ5ZGU3NGZkZDZkMWFjY2M3ZWZmNWI4NDE4NzA5YzI5NTBiYzBmMGUyZjFmMzhhYiIsImlhdCI6MTczOTc0OTE4NSwibmJmIjoxNzM5NzQ5MTg1LCJleHAiOjE3Mzk4MzU1ODUsInN1YiI6IjExOTMzMDI2IiwiZ3JhbnRfdHlwZSI6IiIsImFjY291bnRfaWQiOjMyMTM5OTA2LCJiYXNlX2RvbWFpbiI6ImFtb2NybS5ydSIsInZlcnNpb24iOjIsInNjb3BlcyI6WyJwdXNoX25vdGlmaWNhdGlvbnMiLCJmaWxlcyIsImNybSIsImZpbGVzX2RlbGV0ZSIsIm5vdGlmaWNhdGlvbnMiXSwiaGFzaF91dWlkIjoiYzJjZjhmMzEtNzA3Yy00OGNkLTkwYjMtYTk1YTNjYTZmODk4IiwiYXBpX2RvbWFpbiI6ImFwaS1iLmFtb2NybS5ydSJ9.jFpnMLyUnPXmj6jL8uiYOp0faqcMG31RVleN1kceEiqSDuq7az-qODqW4HwvCqPp92AgPjkU3OWTJju_eWEEjr3qOEMr5-f8sWG_MxulwU2L9F8WAACfBjdJNsCV2Oh4L60gJG-Nxlwsu8gB6oYW0EhpAWt6qRCea9pNxvFZu8BqcPGO58rHlGMN4fpNQUrxzXw_ray0OG0OydpbrmipfFoIs4gW1CDSYYBcWaBB3xbmc9D4QG3VxXF2Mi_3MfgvRoMLVDHClBS5ugL_PQig-t0mvl6NmgF1IXN6WmnMc6o9YBJaqCX7f4jBXp9yNTwkpiQm4ShVimZPbvLgJo-gHw"

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