import requests

from src.main import url_or_string, get_methods

LIST_STRING = [
   "https://google.com",
   "Какая то строка",
   "http://grkdvjktu.com",
   "http://yandex.ru"
]

def test_string_is_a_link():
    # response = requests.get(url=LIST_STRING[0])
    assert url_or_string(LIST_STRING[0]) == True
    assert url_or_string(LIST_STRING[1]) == True
    assert url_or_string(LIST_STRING[2]) == True
    assert url_or_string(LIST_STRING[3]) == True



