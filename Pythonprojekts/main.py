import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '7b7d6f9a80db91b762b3041d2cae5162'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}


body_create = {
    "name": "Питончик",
    "photo_id": 5
}

body_change = {
    "pokemon_id": "141097",
    "name": "Чипа Чапа",
    "photo_id": 12
}


body_in_pokeballe = {
    "pokemon_id": "141097"
}


'''response_create = requests.post(url = f'{URL}/pokemons', headers= HEADER, json = body_create)
print(response_create.text)'''


'''response_change_name = requests.put(url = f'{URL}/pokemons', headers= HEADER, json = body_change)
print(response_change_name.text)'''


response_in_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers= HEADER, json = body_in_pokeballe)
print(response_in_pokeball.text)