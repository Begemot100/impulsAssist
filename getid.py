import requests
import hashlib
import hmac
import base64
import datetime
import email.utils
import os
# 🔹 Данные API
AMOCRM_BASE_URL = "https://tech241224.amocrm.ru"
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

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
