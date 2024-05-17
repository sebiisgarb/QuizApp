import requests

parameteres = {
    "amount": 10,
    "type": "boolean",
    "category": 18
}

response = requests.get(url="https://opentdb.com/api.php", params=parameteres)
response.raise_for_status()
question_data = response.json()["results"]
