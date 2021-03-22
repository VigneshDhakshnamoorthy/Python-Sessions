import requests
import json

response = requests.get("https://reqres.in/api/users")
print("response : " + str(response.json()))
email = response.json()["data"]
for ema in email:
    print(ema["email"])

response = requests.post("https://reqres.in/api/users", data={ "name": "morpheus",
                                                               "job": "leader" })
print("createdAt : " + str(response.json()["createdAt"]))

response = requests.post("https://reqres.in/api/register", data={ "email": "eve.holt@reqres.in",
                                                                  "password": "pistol" })
print("token : " + str(response.json()["token"]))