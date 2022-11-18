import requests
from  requests.exceptions import InvalidURL, ConnectionError
import pytest
import json


from src.main import url_or_string, get_methods

LIST_STRING = [
   "https://google.com",
   "Какая то строка",
   "http://grkdvjktu.com",
   "google.com",
   "https://ru.wikipedia.org/api/rest_v1/page/pdf/Заглавная_страница"
]

def test_string_is_a_link():
    assert url_or_string(LIST_STRING[0]) == True

    assert url_or_string(LIST_STRING[1]) == None

    assert url_or_string(LIST_STRING[2]) == None

    assert url_or_string(LIST_STRING[3]) == None

    assert url_or_string(LIST_STRING[4]) == False


def test_get_method():
   list_url = ["https://google.com", "https://youtube.com", "http://yandex.ru"]
   result_dict = {
       "https://google.com": { 
           "GET": 200,
           "HEAD": 301
       },
       "https://youtube.com": {
           "GET": 200,
           "HEAD": 301,
           "POST": 400,
           "PUT": 400
       },
       "http://yandex.ru": {
           "GET": 200,
           "HEAD": 302,
           "POST": 200,
           "PUT": 200,
           "DELETE": 200,
           "OPTIONS": 200,
           "PATCH": 200
       }
   }
   print(get_methods(list_url))
   assert get_methods(list_url) == json.dumps(result_dict, indent=4)

def test_except_massege(capfd):
    get_methods([LIST_STRING[1]])
    out, err = capfd.readouterr()
    assert out == f"Строка '{LIST_STRING[1]}' не является ссылкой\n"

    get_methods([LIST_STRING[2]])
    out, err = capfd.readouterr()
    assert out == f"Строка '{LIST_STRING[2]}' не является ссылкой\n"

    get_methods([LIST_STRING[3]])
    out, err = capfd.readouterr()
    assert out == f"Строка '{LIST_STRING[3]}' не является ссылкой\n"
