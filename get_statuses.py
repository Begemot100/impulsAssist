import requests
import json
import os

AMOCRM_BASE_URL = "https://tech241224.amocrm.ru"
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

response = requests.get(f"{AMOCRM_BASE_URL}/api/v4/leads/pipelines/9239766", headers=headers)

print(json.dumps(response.json(), indent=2, ensure_ascii=False))
