#pip install requests
import requests 
url= "https://fake-json-api.mock.beeceptor.com/users"
responce= requests.get(url=url)

print(responce.json())


