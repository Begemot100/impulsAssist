import requests
import os
BASE_URL = "https://tech241224.amocrm.ru"
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

# headers = {
#     "Authorization": f"Bearer {ACCESS_TOKEN}"
# }
#
# response = requests.get(f"{BASE_URL}/api/v4/leads",
#                         headers=headers,
#                         params={"filter[pipeline_id]": "9035110", "page": 1, "limit": 5})
#
# print(response.json())

HEADERS = {
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}

# Получаем список воронок
response = requests.get(f"{BASE_URL}/api/v4/leads/pipelines", headers=HEADERS)
pipelines = response.json().get("_embedded", {}).get("pipelines", [])

# Выводим все воронки и их статусы
for pipeline in pipelines:
    print(f"ID воронки: {pipeline['id']}, Название: {pipeline['name']}")
    for status in pipeline.get("_embedded", {}).get("statuses", []):
        print(f"  - ID статуса: {status['id']}, Название: {status['name']}")