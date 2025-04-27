import requests

BASE_URL = "https://tech241224.amocrm.ru"
ACCESS_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImE0NDZhMGU4YmE0YzEwYThiYmYwZTAzMjU5N2M4MTc1NDlkZTc0ZmRkNmQxYWNjYzdlZmY1Yjg0MTg3MDljMjk1MGJjMGYwZTJmMWYzOGFiIn0.eyJhdWQiOiI0Y2RhMWVlNi00ODg5LTQ2YWUtYjU3YS01ZTFiOTZlYTJmY2EiLCJqdGkiOiJhNDQ2YTBlOGJhNGMxMGE4YmJmMGUwMzI1OTdjODE3NTQ5ZGU3NGZkZDZkMWFjY2M3ZWZmNWI4NDE4NzA5YzI5NTBiYzBmMGUyZjFmMzhhYiIsImlhdCI6MTczOTc0OTE4NSwibmJmIjoxNzM5NzQ5MTg1LCJleHAiOjE3Mzk4MzU1ODUsInN1YiI6IjExOTMzMDI2IiwiZ3JhbnRfdHlwZSI6IiIsImFjY291bnRfaWQiOjMyMTM5OTA2LCJiYXNlX2RvbWFpbiI6ImFtb2NybS5ydSIsInZlcnNpb24iOjIsInNjb3BlcyI6WyJwdXNoX25vdGlmaWNhdGlvbnMiLCJmaWxlcyIsImNybSIsImZpbGVzX2RlbGV0ZSIsIm5vdGlmaWNhdGlvbnMiXSwiaGFzaF91dWlkIjoiYzJjZjhmMzEtNzA3Yy00OGNkLTkwYjMtYTk1YTNjYTZmODk4IiwiYXBpX2RvbWFpbiI6ImFwaS1iLmFtb2NybS5ydSJ9.jFpnMLyUnPXmj6jL8uiYOp0faqcMG31RVleN1kceEiqSDuq7az-qODqW4HwvCqPp92AgPjkU3OWTJju_eWEEjr3qOEMr5-f8sWG_MxulwU2L9F8WAACfBjdJNsCV2Oh4L60gJG-Nxlwsu8gB6oYW0EhpAWt6qRCea9pNxvFZu8BqcPGO58rHlGMN4fpNQUrxzXw_ray0OG0OydpbrmipfFoIs4gW1CDSYYBcWaBB3xbmc9D4QG3VxXF2Mi_3MfgvRoMLVDHClBS5ugL_PQig-t0mvl6NmgF1IXN6WmnMc6o9YBJaqCX7f4jBXp9yNTwkpiQm4ShVimZPbvLgJo-gHw"

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