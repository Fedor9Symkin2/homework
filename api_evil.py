import requests

response = requests.get('https://evilinsult.com/generate_insult.php?lang=ru&type=json')

print(response.json().get('insult'))