import requests 
import base64

#Replace With My own Client ID and Client Secret
CLIENT_ID = '9e912b0d73424539b41d7c1c8a918645'
CLIENT_SECRET = '7b6ceab2e6ca41bc8903c5d69ac74810'

# Base64 encode the client Id and client secret
client_credentials = f"{CLIENT_ID}:{CLIENT_SECRET}"
client_credentials_base64 = base64.b64decode(client_credentials.encode())

#Request the access token

token_url = 'https://accounts.sportify.com/api/token'
headers = {
    'Authorization': f'Basic{client_credentials_base64.decode()}'
    
}

data = {
    'grant_type':'client_credentials'
    
}

response = request.post(token_url,data=data,headers = headers)

if response.status_code == 200:
    access_token = response.json()['access_token']
    print("Access token obtained successfully. ")
    
else:
    print("Error token obtained Successfully.")
    exit()
