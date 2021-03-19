import requests
import json

response = requests.get("http://api.open-notify.org/astros.json")
print("Status : " + str(response.status_code))


def json_print(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=False, indent=3)
    print(text)


json_print(response.json())

for resp in response.json()['people']:
    print(resp['craft'], end=' ')
    print(resp['name'])

parameters = {
    "lat": 40.71,
    "lon": -74
}
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

json_print(response.json())
