import requests

response = requests.get('https://api.ipify.org')
print(f'My public IP address is: {response.text}')
