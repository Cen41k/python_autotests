import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '7b7d6f9a80db91b762b3041d2cae5162'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '10267'


def test_status_code(): 
     response = requests.get(url = f'{URL}/trainers', params= {'trainer_id' : TRAINER_ID})
     assert response.status_code == 200

def test_part_of_json():
     response_get = requests.get(url = f'{URL}/trainers', params= {'trainer_id' : TRAINER_ID})
     assert response_get.json()["data"][0]["trainer_name"] == 'Сеньчик'
    
def test_trainer():
    response_geti = requests.get(url=f'{URL}/trainers', params={'trainer_id': TRAINER_ID})
    assert response_geti.json()["data"][0]["id"] == '10267'
    print(response_geti.json)

def test_trainer1():
    response_geti = requests.get(url=f'{URL}/trainers', params={'trainer_id': TRAINER_ID})
    
    # Предполагаем, что ответ содержит данные в формате JSON и есть хотя бы один тренер
    trainer_data = response_geti.json()["data"][0]
    
    # Извлекаем id и имя тренера
    trainer_id = trainer_data["id"]
    trainer_name = trainer_data["trainer_name"]  
    
    # Выводим id и имя тренера
    print(f"ID тренера: {trainer_id}")
    print(f"Имя тренера: {trainer_name}")
    
    # Проверяем, соответствует ли id ожидаемому значению
    assert trainer_id == '10267'
    
    # Выводим текст ответа для отладки
    print(response_geti.text)