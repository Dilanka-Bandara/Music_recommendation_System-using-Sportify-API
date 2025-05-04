import requests
import base64

# Replace with your own Client ID and Client Secret
CLIENT_ID = '9e912b0d73424539b41d7c1c8a918645'
CLIENT_SECRET = '7b6ceab2e6ca41bc8903c5d69ac74810'

# Base64 encode the client ID and client secret
client_credentials = f"{CLIENT_ID}:{CLIENT_SECRET}"
client_credentials_base64 = base64.b64encode(client_credentials.encode()).decode()

# Request the access token
token_url = 'https://accounts.spotify.com/api/token'  # Fixed typo: "sportify" -> "spotify"

headers = {
    'Authorization': f'Basic {client_credentials_base64}',  # Space after 'Basic'
    'Content-Type': 'application/x-www-form-urlencoded'
}

data = {
    'grant_type': 'client_credentials'
}

response = requests.post(token_url, data=data, headers=headers)  # Fixed: 'requests' not 'request'

if response.status_code == 200:
    access_token = response.json()['access_token']
    print("Access token obtained successfully.")
    print("Access Token:", access_token)
else:
    print("Error obtaining access token.")
    print("Status Code:", response.status_code)
    print("Response:", response.text)
