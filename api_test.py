import requests

BASE_URL = "https://dummyjson.com"

# 1. Login and get access token
login_url = f"{BASE_URL}/auth/login"

login_payload = {
    "username": "emilys",
    "password": "emilyspass",
    "expiresInMins": 30
}

login_response = requests.post(login_url, json=login_payload)

print("Login Status:", login_response.status_code)
print("Login Response:", login_response.json())

# Validate login
assert login_response.status_code == 200

access_token = login_response.json()["accessToken"]

# 2. Call authenticated API
# Path parameter: user_id
user_id = 1

# Query parameters
params = {
    "limit": 10,
    "skip": 0
}

headers = {
    "Authorization": f"Bearer {access_token}"
}

user_url = f"{BASE_URL}/auth/users/{user_id}"

response = requests.get(
    user_url,
    headers=headers,
    params=params
)

print("\nUser Status:", response.status_code)
print("User Response:", response.json())

# 3. Validations
assert response.status_code == 200

user_data = response.json()

assert user_data["id"] == user_id
assert "username" in user_data
assert "email" in user_data