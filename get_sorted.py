import requests
import time
import os
# 🔹 Настройки API
BASE_URL = "https://tech241224.amocrm.ru"
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

HEADERS = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

# 1️⃣ Получаем все воронки и их ID
def get_pipelines():
    url = f"{BASE_URL}/api/v4/leads/pipelines"
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        print(f"❌ Ошибка API: {response.status_code}")
        return {}

    pipelines = response.json().get("_embedded", {}).get("pipelines", [])
    return {p["name"].lower(): p["id"] for p in pipelines}

# 2️⃣ Получаем ID разделов в воронке
def get_pipeline_stage_ids(pipeline_id):
    url = f"{BASE_URL}/api/v4/leads/pipelines/{pipeline_id}/statuses"
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        print(f"❌ Ошибка API: {response.status_code}")
        return {}

    stages = response.json().get("_embedded", {}).get("statuses", [])
    return {s["name"].lower(): s["id"] for s in stages}

# 3️⃣ Получаем все лиды из "Неразобранное"
def get_unsorted_leads():
    url = f"{BASE_URL}/api/v4/leads/unsorted?page=1&limit=100"
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        print(f"❌ Ошибка API: {response.status_code}")
        return []

    leads = response.json().get("_embedded", {}).get("unsorted", [])
    print(f"✅ Найдено {len(leads)} заявок в 'Неразобранное'")
    return leads

# 4️⃣ Принятие лида из "Неразобранное"
def accept_lead(unsorted_id):
    url = f"{BASE_URL}/api/v4/leads/unsorted/{unsorted_id}/accept"
    response = requests.post(url, headers=HEADERS)

    if response.status_code == 200:
        print(f"✅ Лид {unsorted_id} успешно принят!")
        return True
    else:
        print(f"❌ Ошибка при принятии лида {unsorted_id}: {response.text}")
        return False

# 5️⃣ Перемещение лида в нужный раздел
def move_lead(lead_id, new_pipeline_id, new_stage_id):
    url = f"{BASE_URL}/api/v4/leads/{lead_id}"
    payload = {
        "pipeline_id": new_pipeline_id,
        "status_id": new_stage_id
    }

    response = requests.patch(url, headers=HEADERS, json=payload)

    if response.status_code == 200:
        print(f"✅ Лид {lead_id} перемещен в воронку {new_pipeline_id}, раздел {new_stage_id}")
    else:
        print(f"❌ Ошибка при перемещении лида {lead_id}: {response.text}")

def main():
    pipelines = get_pipelines()

    instagram_pipeline_id = pipelines.get("instagram")
    facebook_pipeline_id = pipelines.get("facebook")
    impuls_pipeline_id = pipelines.get("impuls_web")

    if not instagram_pipeline_id or not facebook_pipeline_id or not impuls_pipeline_id:
        print("❌ Ошибка: Не найдены все воронки")
        return

    print(f"✅ Воронка Instagram ID: {instagram_pipeline_id}")
    print(f"✅ Воронка Facebook ID: {facebook_pipeline_id}")
    print(f"✅ Воронка Impuls_web ID: {impuls_pipeline_id}")

    instagram_stages = get_pipeline_stage_ids(instagram_pipeline_id)
    facebook_stages = get_pipeline_stage_ids(facebook_pipeline_id)
    impuls_stages = get_pipeline_stage_ids(impuls_pipeline_id)

    if not instagram_stages or not facebook_stages or not impuls_stages:
        print("❌ Ошибка: Не удалось получить разделы всех воронок")
        return

    print(f"📸 Разделы Instagram: {instagram_stages}")
    print(f"📘 Разделы Facebook: {facebook_stages}")
    print(f"⚡ Разделы Impuls_web: {impuls_stages}")

    leads = get_unsorted_leads()
    for lead in leads:
        lead_id = lead["_embedded"]["leads"][0]["id"]
        unsorted_id = lead["uid"]

        # ✅ Исправлено: если source_name отсутствует, используем пустую строку
        source = (lead.get("source_name") or "").lower()
        source = source.replace("https://", "").replace("http://", "")

        if not accept_lead(unsorted_id):
            continue

        if "facebook" in source and facebook_stages:
            stage_id = facebook_stages.get("первичный контакт", list(facebook_stages.values())[0])
            move_lead(lead_id, facebook_pipeline_id, stage_id)

        elif "instagram" in source and instagram_stages:
            stage_id = instagram_stages.get("первичный контакт", list(instagram_stages.values())[0])
            move_lead(lead_id, instagram_pipeline_id, stage_id)

        elif "impuls" in source and impuls_stages:
            stage_id = impuls_stages.get("первичный контакт", list(impuls_stages.values())[0])
            move_lead(lead_id, impuls_pipeline_id, stage_id)

        else:
            print(f"🔹 Лид {lead_id} оставлен в 'Неразобранное' (Источник: {source})")

        time.sleep(0.1)

if __name__ == "__main__":
    main()