import requests
#
# # AmoCRM API URL
# BASE_URL = "https://tech241224.amocrm.ru"
#
# # Данные интеграции (замените на свои значения)
# CLIENT_ID = "4cda1ee6-4889-46ae-b57a-5e1b96ea2fca"
# CLIENT_SECRET = "jsfCnCoQpHUE5EF3M1y7tnO8RCOwoLUnhdIbk9MEPGoWpPLt1RPg9ijwH3A8xWxz"
# REDIRECT_URI = "https://ecd0-185-209-196-176.ngrok-free.app/webhook"
# REFRESH_TOKEN = "def502000065c63e34dd7376127c2916628023975686f1d66e958427c15e866880cb3fa9b62815fef4c55682e1927ba38382687d2c7478931eec0a0d2a9e5de790da30d69144355e91610a433d8cdabfbe60f3c4d1556501678df460735774df6c255efbe8ed824a1f901d80c9b59466f35eb79869b8de132ebd56f03b7af756193653a3c76d25befba1970b3efa50abcfb619c7f6557166c41fbf1739c6a71c2a02101246882eccdccd144b7e0d48adc2517dddd660aa6c90547bc83dc3d094883a89a05427e41731c2ba6735c665a2335ece90655e64df6430c05eb551e6e22d38bc0a8529bdbaea211f6f8dfde8f1ba63822c0097585d7e6d943c305e4e9390dac229d9a2b4247e9f2ece837d14e6400c4974e4dc72f1ffd766d905abf2b1fcd025a33d244810f6c5e4f1c951fa7456e4244a547e9f925a2c8773ce136440137e8851e46c4040064d0c4ea441da67646e7f2f7fcf3c7bf1a4acf0c90c18650af2d4d9d9b32af8eb08dd2d6042550091b2b17d1c87ba2d926af7a20d157b654d557083923819e70e6fc3470ca0939e6f0753a0e8bb08e0fdec669406c34fcf69804bca2a023b111b7495e2d205776645617e4e737593c55b5fe1f6cc04e594bfb9bbc2271d4b1994b5211fb6b83139d628816f9cf659b1b2dd54c94b190449af54e1e5be96465a101e394db2fc84a4b5b1b07306da3f1a0f67ade03edb194d2f8f9d65cf.eyJhdWQiOiI0Y2RhMWVlNi00ODg5LTQ2YWUtYjU3YS01ZTFiOTZlYTJmY2EiLCJqdGkiOiIwODNiODY3ZjdmMjRjZWViMmFjNjJiYTc4MjI2NThkNTgyNTU1Y2JmYTQ3Y2MwMzBiOWQ1ZjY5NDdmZDk0N2U4OGM3M2Y2N2QyYTk4N2E2MyIsImlhdCI6MTczOTYxMzU5NiwibmJmIjoxNzM5NjEzNTk2LCJleHAiOjE3NTExNTUyMDAsInN1YiI6IjExOTMzMDI2IiwiZ3JhbnRfdHlwZSI6IiIsImFjY291bnRfaWQiOjMyMTM5OTA2LCJiYXNlX2RvbWFpbiI6ImFtb2NybS5ydSIsInZlcnNpb24iOjIsInNjb3BlcyI6WyJjcm0iLCJmaWxlcyIsImZpbGVzX2RlbGV0ZSIsIm5vdGlmaWNhdGlvbnMiLCJwdXNoX25vdGlmaWNhdGlvbnMiXSwiaGFzaF91dWlkIjoiNWMyZjliZDItZTkyMS00OTU1LTg1ZGUtZTZiODlkMmM4NzNkIiwiYXBpX2RvbWFpbiI6ImFwaS1iLmFtb2NybS5ydSJ9.J-70wsvphXJejcu_WzQWNzmx2yJX0UcIAVNLPdoCcUIacer0V4HGy3n71mW0XYw_nJ71Rfhcpar5SD_PP9acG8BLG3gbgxG_f0f4PyG4-ir2yQC6Fi8ejJygdBJgHNIXwr_nC8t377S1ox3LlZcmmsxIcSgwYeiafE2rRIWZier59kNR5DT4hTiriMiR3FhG7-tVdpoBs_y94Fm1scPbF0WWTUvXFjpsOL9jsCurKxw8YTV7hqcPE-SOPs4yW86Gqxl2eLsWmTZiqp6cqX-iwYVPA0ct8R7LUVyIHp9jhn6Yq7rfK24cN1HwqlT7cZs2-FEMe1-Mfs4fWhIwdVPzKQ"
#
# # Формируем запрос на обновление токена
# data = {
#     "client_id": CLIENT_ID,
#     "client_secret": CLIENT_SECRET,
#     "grant_type": "refresh_token",
#     "refresh_token": REFRESH_TOKEN,
#     "redirect_uri": REDIRECT_URI
# }
#
# response = requests.post(f"{BASE_URL}/oauth2/access_token", json=data)
#
# # Проверяем результат
# if response.status_code == 200:
#     tokens = response.json()
#     print("✅ Новый access_token:", tokens["access_token"])
#     print("🔄 Новый refresh_token:", tokens["refresh_token"])
# else:
#     print("❌ Ошибка обновления токена:", response.json())
# ACCESS_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImJiOTM2NzA4OTNhMjAyYTY4OTY4YzU2OTAyNGEzNDM4M2RjZTBhM2Q3MDUxYjY0ZjM3ZTViZGNmY2YyMWVmNGEwODllNmRlNzhhMjRhNDRkIn0.eyJhdWQiOiI0Y2RhMWVlNi00ODg5LTQ2YWUtYjU3YS01ZTFiOTZlYTJmY2EiLCJqdGkiOiJiYjkzNjcwODkzYTIwMmE2ODk2OGM1NjkwMjRhMzQzODNkY2UwYTNkNzA1MWI2NGYzN2U1YmRjZmNmMjFlZjRhMDg5ZTZkZTc4YTI0YTQ0ZCIsImlhdCI6MTczOTYyNDcyNywibmJmIjoxNzM5NjI0NzI3LCJleHAiOjE3Mzk3MTExMjcsInN1YiI6IjExOTMzMDI2IiwiZ3JhbnRfdHlwZSI6IiIsImFjY291bnRfaWQiOjMyMTM5OTA2LCJiYXNlX2RvbWFpbiI6ImFtb2NybS5ydSIsInZlcnNpb24iOjIsInNjb3BlcyI6WyJwdXNoX25vdGlmaWNhdGlvbnMiLCJmaWxlcyIsImNybSIsImZpbGVzX2RlbGV0ZSIsIm5vdGlmaWNhdGlvbnMiXSwiaGFzaF91dWlkIjoiODNmZjQ1MDMtYWQ5NS00Zjc0LThlMmYtZTg4MjY2MzlkMjBmIiwiYXBpX2RvbWFpbiI6ImFwaS1iLmFtb2NybS5ydSJ9.RAAFM6e_JaKhy8H6TFGszS1MKfVWOQvDkOTbbf2s7FWT1dfwE3neln8MPCzQ8R8vSXWSCvvfc_JasjEjtEAIwE0FxqP4TGEhAQCcyywXQXa8e-Rtm1XIQTCn-PNjMAs3Jgy5L3ACz7bYCBXWgliPGbppXUp9-KFF1HAXWKgnUWq0E2hfsgw-tgX0I114M_lAG1Bom4oXYd_JpSNMBdohSyM6KrM7o6HRGjtei_hXidd2x_jnMWvL_4IBBs3hRRzXjE7-_Gj7WLlQjfsoF9ADvAYj6rxaUanjvo37beEyCmJ1GgGhEld-oGHGv35AijfCpwOrEYmwAEXTU942E8ajOg"
# REFRESH_TOKEN = "def50200ef5d7d4aa2b37956da3e42587b73741ab79d879f9864f774dd5693f0b78fd6844c0b0735530d231e4c5d59ddf31a5701a559ff8d41995d4e52f96f074f03c20a90777d8535d581b9939dcfc3e760847e17f608bf28be204c1aa9cc35443bc442ed8db19ae0905d425c25e5eeb0345209164922bd3ce9dcd70daa6a30d23db7254302476cf997fde482b2f8356ed80cf812848d3bd56ecfee3370f39cd477b21d8f2a9208b8cecfb17d0406f0fef6f9e2fb96da34e66b3b9a333b816c3f0af23bedb09d3e56159c871c95a0b188f8106fc1b999b1a6174711397553f2eaa8637021671c421e733d921d8e064049849a6f7dd28ac7863073e184942088c2d098c8444f4604126aca8acf6f5d697d60c36043fbb6aabb84dc4e2f3fbf0da40915c0f5f3c652876b17ffcd6602432851644b6dc51e49e8da20f535a87f8c010baae3f0f8832ebcde36ec7cc54c5991ab0b4c5b5205d0cbb2d0011b8e591d45b865fa82575554602b4b936392fbf13c649ee3866827f20caca338d27fbdbf85e9f75f84e7ea7b7c73708f83f6abd4e1940cc0ee749d04e2facb3e42f671a378a6834c601c6557689e9088ef5388e35db99467e83bc3e61e2293feda565de70c84ee68b8eac2db5448d9604b5127f804df6dda4d886de247816a56367859ef535d0aea8dcd776072d27a0f96f5a30ee751cbd7d12d0e8b3cbc5b211e6a687702ae3f1afb"
# AMOCRM_BASE_URL = "https://tech241224.amocrm.ru"
#
# def find_contact(query):
#     headers = {
#         "Authorization": f"Bearer {ACCESS_TOKEN}",
#         "Content-Type": "application/json"
#     }
#     response = requests.get(
#         f"{AMOCRM_BASE_URL}/api/v4/contacts",
#         headers=headers,
#         params={"query": query}
#     )
#     print(f"📤 Запрос: {response.url}")
#     print(f"📥 Ответ: {response.text}")  # ← Логируем ответ API
#
#     if response.status_code == 401:
#         print("❌ Токен истёк! Требуется обновление.")
#         return None
#
#     try:
#         return response.json()
#     except requests.exceptions.JSONDecodeError:
#         print("❌ Ошибка: Сервер вернул пустой ответ.")
#         return None
#
# def refresh_access_token():
#     url = "https://tech241224.amocrm.ru/oauth2/access_token"
#     data = {
#         "client_id": "4cda1ee6-4889-46ae-b57a-5e1b96ea2fca",
#         "client_secret": "jsfCnCoQpHUE5EF3M1y7tnO8RCOwoLUnhdIbk9MEPGoWpPLt1RPg9ijwH3A8xWxz",
#         "grant_type": "refresh_token",
#         "refresh_token": "def50200ef5d7d4aa2b37956da3e42587b73741ab79d879f9864f774dd5693f0b78fd6844c0b0735530d231e4c5d59ddf31a5701a559ff8d41995d4e52f96f074f03c20a90777d8535d581b9939dcfc3e760847e17f608bf28be204c1aa9cc35443bc442ed8db19ae0905d425c25e5eeb0345209164922bd3ce9dcd70daa6a30d23db7254302476cf997fde482b2f8356ed80cf812848d3bd56ecfee3370f39cd477b21d8f2a9208b8cecfb17d0406f0fef6f9e2fb96da34e66b3b9a333b816c3f0af23bedb09d3e56159c871c95a0b188f8106fc1b999b1a6174711397553f2eaa8637021671c421e733d921d8e064049849a6f7dd28ac7863073e184942088c2d098c8444f4604126aca8acf6f5d697d60c36043fbb6aabb84dc4e2f3fbf0da40915c0f5f3c652876b17ffcd6602432851644b6dc51e49e8da20f535a87f8c010baae3f0f8832ebcde36ec7cc54c5991ab0b4c5b5205d0cbb2d0011b8e591d45b865fa82575554602b4b936392fbf13c649ee3866827f20caca338d27fbdbf85e9f75f84e7ea7b7c73708f83f6abd4e1940cc0ee749d04e2facb3e42f671a378a6834c601c6557689e9088ef5388e35db99467e83bc3e61e2293feda565de70c84ee68b8eac2db5448d9604b5127f804df6dda4d886de247816a56367859ef535d0aea8dcd776072d27a0f96f5a30ee751cbd7d12d0e8b3cbc5b211e6a687702ae3f1afb",
#         "redirect_uri": "https://tech241224.amocrm.ru/webhook"
#     }
#     response = requests.post(url, json=data)
#     if response.status_code == 200:
#         new_token = response.json().get("access_token")
#         print(f"✅ Новый токен: {new_token}")
#         return new_token
#     else:
#         print(f"❌ Ошибка обновления токена: {response.text}")
#         return None
#
# # Обновляем токен и пробуем снова
# ACCESS_TOKEN = refresh_access_token()


import requests
import time

AMOCRM_BASE_URL = "https://tech241224.amocrm.ru"
ACCESS_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjMzNzg3MTJkZWU1NjA4ODI2YWQyOTMzNjNjNGNmNGU5ODM2OTgwNDk3MzY1NmE0ZjU2ZTQwOWIzZjViYmQwYzI2MzRmMDI3ZWIzNmQyZTQ4In0.eyJhdWQiOiI0Y2RhMWVlNi00ODg5LTQ2YWUtYjU3YS01ZTFiOTZlYTJmY2EiLCJqdGkiOiIzMzc4NzEyZGVlNTYwODgyNmFkMjkzMzYzYzRjZjRlOTgzNjk4MDQ5NzM2NTZhNGY1NmU0MDliM2Y1YmJkMGMyNjM0ZjAyN2ViMzZkMmU0OCIsImlhdCI6MTczOTYyNjU4NywibmJmIjoxNzM5NjI2NTg3LCJleHAiOjE3NTEyNDE2MDAsInN1YiI6IjExOTMzMDI2IiwiZ3JhbnRfdHlwZSI6IiIsImFjY291bnRfaWQiOjMyMTM5OTA2LCJiYXNlX2RvbWFpbiI6ImFtb2NybS5ydSIsInZlcnNpb24iOjIsInNjb3BlcyI6WyJjcm0iLCJmaWxlcyIsImZpbGVzX2RlbGV0ZSIsIm5vdGlmaWNhdGlvbnMiLCJwdXNoX25vdGlmaWNhdGlvbnMiXSwiaGFzaF91dWlkIjoiNDg0NDBlYzQtY2E4Ni00NzYzLTgxZmMtNGVmYjQzNThmMDA0IiwiYXBpX2RvbWFpbiI6ImFwaS1iLmFtb2NybS5ydSJ9.YXEN6xQ6WwqM5rU_lnSLwLOMtgKP0Po-8wbqoC_2-NTyKIaFZnOoAeTBUa8CTu2t5iYDTNY7WRHt1GtTLj2_UHpOGCYs8OH-6kE36_BjovoMFHFizi8eLDxVWNgMtLWKxfkQq_V5vISLr8Vos1Q_Jar2jyefsjzRXTQI1r_XXZTP917mOogHeC_9mKJdbT2zmIBync33fmLUgZ8BDRIRTRvCsROm2oyZn6AmaomUSRf_CAP3EbwjZeVJZL12fKYAKKrROFaMxZLz_v-bqpagkqgwClnGMIaR0vH34_FYkfQvIMAqWYtlAlg7whiOrYxtg9s2RqAtjCX_6dsFGXDDbw"
REFRESH_TOKEN = "def50200664920b5db8a420cbffeeb7fe97112db40c79a91a51457922bc23ed0bf8a5d0bea08acad37fa1535dd3e88e8224a38c9f4798e0dd8d04a3ec463ebc439acb9f342fea43a0653f4197951190564626c9af126b3a25f0f6545524e237f6c87f58fb84944da3cf46d15ebced41475029b6b9c0e85cdbb0fbcb16739c4d857008d012d1495750eacebc4bc46a85d5d781a71cb368e18bd6fab231e53fbba4e9d6865846d4cbcf99f11e673a40e8c4a014aeaa3f46e5e901265c26d3d17a45d0c375dfaaa4e1a7cfccb9766ff6512dee2fb737d5078ea48d9d7ac4d10252a6686669f60d20b815fe7e74553ced9490017fe2317e3d5481c295e48cdb75316b00cce2480181947ca38c9b98688272447cc71a5729945ea83bf1e42f17f448acee7e5f520578b527941477d0bbfdfc0596cacc92fb1a1c61075cc95d8cb7ad2751ecc9215cedef07e5cbccb0474969ff9f0dc25fe0f55e7c6e999c7a54b592399de306e31b4501c7fe0c9384f286a36973c851928c8350bf853be2f9729d279dfd9db56826df46f5dda592a9ef5182408f1741915ed6258152aab7f21cad8bfb0e8edf826450fefc3d39e5c9ff19c4b8d3d7ba9bca64a02435aa86be0edba86b3d297bfa92738c0ec54932811a5eaf718fb4da5e9729564de948d34b318837159da194c574055c2c310f5e30b5e"

# # Функция обновления токена
# def refresh_access_token():
#     global ACCESS_TOKEN, REFRESH_TOKEN
#     url = f"{AMOCRM_BASE_URL}/oauth2/access_token"
#     data = {
#         "client_id": "4cda1ee6-4889-46ae-b57a-5e1b96ea2fca",
#         "client_secret": "I2iSaq6frPjhV5pzMSgzYwz1V6YtkPdB6zriSlJ84xCd5G6H1FOrec1V9f1kXMMi",
#         "grant_type": "refresh_token",
#         "refresh_token": REFRESH_TOKEN,
#         "redirect_uri": "https://600b-185-209-196-176.ngrok-free.app/webhook"
#     }
#
#     response = requests.post(url, json=data)
#
#     if response.status_code == 200:
#         tokens = response.json()
#         ACCESS_TOKEN = tokens["access_token"]
#         REFRESH_TOKEN = tokens["refresh_token"]
#         print(f"✅ Новый ACCESS_TOKEN: {ACCESS_TOKEN[:20]}...")
#         print(f"✅ Новый REFRESH_TOKEN: {REFRESH_TOKEN[:20]}...")
#     else:
#         print(f"❌ Ошибка обновления токена: {response.text}")
import sys
sys.stdout.reconfigure(encoding='utf-8')

def create_contact(name, phone, email=None):
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    contact_data = {
        "name": name,
        "custom_fields_values": [
            {
                "field_id": 949379,  # Телефон
                "values": [{"value": phone, "enum_id": 682997}]  # MOB
            }
        ]
    }

    if email:
        contact_data["custom_fields_values"].append(
            {
                "field_id": 949381,  # Email
                "values": [{"value": email, "enum_id": 683005}]  # WORK
            }
        )

    contact_data["custom_fields_values"].append(
        {
            "field_id": 1002161,  # Источник
            "values": [{"enum_id": 713619}]  # Facebook
        }
    )

    response = requests.post(f"{AMOCRM_BASE_URL}/api/v4/contacts", headers=headers, json=[contact_data])
    print(f"Ответ на создание контакта: {response.text}".encode("utf-8", "ignore").decode("utf-8"))

    if response.status_code in [200, 201]:
        return response.json()
    else:
        print("\u274c Ошибка создания контакта!")
        return None


# Тест вызова функции
create_contact("Имя клиента", "+34680925970", "email@example.com")

# Тестируем создание контакта
create_contact("Кир", "+34680925970", "test@example.com")
def find_contact(query):
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    response = requests.get(
        f"{AMOCRM_BASE_URL}/api/v4/contacts",
        headers=headers,
        params={"query": query}
    )
    print(f" Запрос: {response.url}")
    print(f" Ответ: {response.text}")  # Логируем ответ

    if response.status_code == 401:
        print(" Токен истёк! Обновляем токен...")
        refresh_access_token()
        return find_contact(query)

    try:
        return response.json()
    except requests.exceptions.JSONDecodeError:
        print(" Ошибка: AmoCRM вернул пустой ответ.")
        return None

# Проверяем контакт по номеру
find_contact("+34680925970")


# # Автообновление токена каждые 23 часа
# while True:
#     refresh_access_token()
#     time.sleep(82800)  # 23 часа
