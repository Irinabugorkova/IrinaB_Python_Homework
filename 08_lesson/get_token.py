import requests

url = "https://ru.yougile.com/api-v2/auth/keys"
payload = {
  "login": "jgjhbgjht@yandex.ru",
  "password": "Jfugjryg65",
  "companyId": " 5317ef3a-c6a7-4c2d-8922-686166270889"
}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)
print(response.json())
