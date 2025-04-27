import requests
import hashlib
import hmac
import base64
import datetime
import email.utils

# 🔹 Данные API
AMOCRM_BASE_URL = "https://tech241224.amocrm.ru"
ACCESS_TOKEN="eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjMyZjc5MzdlMmE1MjYzOWFmNDUyZjYwN2I5NDBiZDA0NzRmZmM4N2QzYWRjOTJiOTNiNGQyYjljMmZlYmE5NGMzNzg4YzkzYmQ4NzIwNTRjIn0.eyJhdWQiOiI0Y2RhMWVlNi00ODg5LTQ2YWUtYjU3YS01ZTFiOTZlYTJmY2EiLCJqdGkiOiIzMmY3OTM3ZTJhNTI2MzlhZjQ1MmY2MDdiOTQwYmQwNDc0ZmZjODdkM2FkYzkyYjkzYjRkMmI5YzJmZWJhOTRjMzc4OGM5M2JkODcyMDU0YyIsImlhdCI6MTczOTkxMDY2MCwibmJmIjoxNzM5OTEwNjYwLCJleHAiOjE3Mzk5OTcwNjAsInN1YiI6IjExOTMzMDI2IiwiZ3JhbnRfdHlwZSI6IiIsImFjY291bnRfaWQiOjMyMTM5OTA2LCJiYXNlX2RvbWFpbiI6ImFtb2NybS5ydSIsInZlcnNpb24iOjIsInNjb3BlcyI6WyJwdXNoX25vdGlmaWNhdGlvbnMiLCJmaWxlcyIsImNybSIsImZpbGVzX2RlbGV0ZSIsIm5vdGlmaWNhdGlvbnMiXSwiaGFzaF91dWlkIjoiNDA5NDRjODEtMDJkMi00NjljLTk3Y2UtNDE3MWQ5OGE3YTY4IiwiYXBpX2RvbWFpbiI6ImFwaS1iLmFtb2NybS5ydSJ9.SM1jbLEUYlh4jSNkL0_Ff_69iArSnUg1WNq6ztqQ6rxSRIDV6DUQ2JBa9UI3TEoheQFAUvE448l26teVQ2PiB1PJ3b7lDn9BrUt21Mz8lFc3Jo0poWxNQWTmTMNaJEfOgZQBXAYPP5Nah8qoeeWwhwqUAreD9w2I5symJGHIKi7FYaatmK7ibHSXHbQlknkBvVtdlAjF-SzPaKBpFaFIc-Z1Xy_8wDYU7610KXOgim0pPMoQ7QFO__58WIAWgR43nicerCS2p_V34PxDOp6w1m9TC9wTpB774Ok1F4XazOu7YsJ83cWHgl_curj5ApyVswsBz0O6gSDJ9OBlHVxDjw"
SECRET_KEY = "lyqwrzrlz7OLLnaCggsB5ecko7wAhw4ePOOUfKNjNuC0w6lgQc15zwIdDCMidjEs"
CHANNEL_ID = "54c34715-4c26-4fd5-b17b-e874f1837b87"
ACCOUNT_ID = "32139906"

# 🔹 URL для подключения
url = f"{AMOCRM_BASE_URL}/v2/origin/custom/{CHANNEL_ID}/connect"

# 🔹 Тело запроса
payload = {"account_id": ACCOUNT_ID}
body_str = str(payload).encode("utf-8")

# 🔹 MD5-хеш тела запроса
content_md5 = hashlib.md5(body_str).hexdigest()

# 🔹 Дата в формате RFC 2822
date_str = email.utils.formatdate(timeval=None, localtime=False, usegmt=True)

# 🔹 Генерация HMAC-SHA1 подписи
string_to_sign = f"POST\n{content_md5}\napplication/json\n{date_str}\n/v2/origin/custom/{CHANNEL_ID}/connect"
signature = hmac.new(SECRET_KEY.encode(), string_to_sign.encode(), hashlib.sha1).digest()
x_signature = base64.b64encode(signature).decode()

# 🔹 Заголовки запроса
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json",
    "Date": date_str,
    "Content-MD5": content_md5,
    "X-Signature": x_signature,
    "User-Agent": "Mozilla/5.0"
}

# 🔹 Отправка запроса
response = requests.post(url, json=payload, headers=headers)

# 🔹 Обработка ответа
if response.status_code == 200:
    data = response.json()
    print(f"✅ Подключение успешно! Scope ID: {data.get('scope_id')}")
else:
    print(f"❌ Ошибка {response.status_code}: {response.text}")

import requests
import hashlib
import hmac
import base64
import datetime
import email.utils
import json

# 🔹 Данные API
AMOCRM_BASE_URL = "https://tech241224.amocrm.ru"
ACCESS_TOKEN="eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjMyZjc5MzdlMmE1MjYzOWFmNDUyZjYwN2I5NDBiZDA0NzRmZmM4N2QzYWRjOTJiOTNiNGQyYjljMmZlYmE5NGMzNzg4YzkzYmQ4NzIwNTRjIn0.eyJhdWQiOiI0Y2RhMWVlNi00ODg5LTQ2YWUtYjU3YS01ZTFiOTZlYTJmY2EiLCJqdGkiOiIzMmY3OTM3ZTJhNTI2MzlhZjQ1MmY2MDdiOTQwYmQwNDc0ZmZjODdkM2FkYzkyYjkzYjRkMmI5YzJmZWJhOTRjMzc4OGM5M2JkODcyMDU0YyIsImlhdCI6MTczOTkxMDY2MCwibmJmIjoxNzM5OTEwNjYwLCJleHAiOjE3Mzk5OTcwNjAsInN1YiI6IjExOTMzMDI2IiwiZ3JhbnRfdHlwZSI6IiIsImFjY291bnRfaWQiOjMyMTM5OTA2LCJiYXNlX2RvbWFpbiI6ImFtb2NybS5ydSIsInZlcnNpb24iOjIsInNjb3BlcyI6WyJwdXNoX25vdGlmaWNhdGlvbnMiLCJmaWxlcyIsImNybSIsImZpbGVzX2RlbGV0ZSIsIm5vdGlmaWNhdGlvbnMiXSwiaGFzaF91dWlkIjoiNDA5NDRjODEtMDJkMi00NjljLTk3Y2UtNDE3MWQ5OGE3YTY4IiwiYXBpX2RvbWFpbiI6ImFwaS1iLmFtb2NybS5ydSJ9.SM1jbLEUYlh4jSNkL0_Ff_69iArSnUg1WNq6ztqQ6rxSRIDV6DUQ2JBa9UI3TEoheQFAUvE448l26teVQ2PiB1PJ3b7lDn9BrUt21Mz8lFc3Jo0poWxNQWTmTMNaJEfOgZQBXAYPP5Nah8qoeeWwhwqUAreD9w2I5symJGHIKi7FYaatmK7ibHSXHbQlknkBvVtdlAjF-SzPaKBpFaFIc-Z1Xy_8wDYU7610KXOgim0pPMoQ7QFO__58WIAWgR43nicerCS2p_V34PxDOp6w1m9TC9wTpB774Ok1F4XazOu7YsJ83cWHgl_curj5ApyVswsBz0O6gSDJ9OBlHVxDjw"
SECRET_KEY = "lyqwrzrlz7OLLnaCggsB5ecko7wAhw4ePOOUfKNjNuC0w6lgQc15zwIdDCMidjEs"
CHANNEL_ID = "54c34715-4c26-4fd5-b17b-e874f1837b87"
ACCOUNT_ID = "32139906"

# 🔹 URL для подключения
path = f"/v2/origin/custom/{CHANNEL_ID}/connect"
url = f"{AMOCRM_BASE_URL}{path}"

# 🔹 Тело запроса
payload = {
    "account_id": ACCOUNT_ID,
    "title": "ScopeTitle",  # Название канала
    "hook_api_version": "v2",
}

request_body = json.dumps(payload)

# 🔹 Формируем Content-MD5 (хэш тела запроса)
content_md5 = hashlib.md5(request_body.encode("utf-8")).hexdigest()

# 🔹 Формируем заголовок Date в формате RFC 2822
date_str = email.utils.formatdate(timeval=None, localtime=False, usegmt=True)

# 🔹 Генерируем HMAC-SHA1 подпись
string_to_sign = f"POST\n{content_md5}\napplication/json\n{date_str}\n{path}"
signature = hmac.new(SECRET_KEY.encode("utf-8"), string_to_sign.encode("utf-8"), hashlib.sha1).digest()
x_signature = base64.b64encode(signature).decode()

# 🔹 Заголовки запроса
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Date": date_str,
    "Content-Type": "application/json",
    "Content-MD5": content_md5,
    "X-Signature": x_signature,
}

# 🔹 Отправка POST-запроса
response = requests.post(url, json=payload, headers=headers)

# 🔹 Обработка ответа
if response.status_code == 200:
    data = response.json()
    print(f"✅ Подключение успешно! Scope ID: {data.get('scope_id')}")
else:
    print(f"❌ Ошибка подключения: {response.status_code} - {response.text}")
