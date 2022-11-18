import requests
from requests.exceptions import InvalidURL, ConnectionError, MissingSchema
import json


def url_or_string(link):
    """Функция определяет является строка ссылкой"""
    FAILED_MESSAGE = f"Строка '{link}' не является ссылкой"

    try:
        response = requests.get(link)
        if "text/html" in response.headers["Content-Type"]:
            return True
        return False
    except ConnectionError:
        print(f"{FAILED_MESSAGE}")
    except InvalidURL:
        print(f"{FAILED_MESSAGE}")
    except MissingSchema:
        print(f"{FAILED_MESSAGE}")


def get_methods(string_list):
    """Функция определяет какие http методы доступны по ссылке
    и возвращает json
    """
    result = {}
    
    for link in string_list:
        ctat_code = {}
        if url_or_string(link):
            get = requests.get(link).status_code
            if get != 405:
                ctat_code["GET"] = get
                result[link] = ctat_code
            head = requests.head(link).status_code
            if head != 405:
                result[link]["HEAD"] = head
            post = requests.post(link).status_code
            if post != 405:
                result[link]["POST"] = post
            put = requests.put(link).status_code
            if put != 405:
                result[link]["PUT"] = put
            delete = requests.delete(link).status_code
            if delete != 405:
                result[link]["DELETE"] = delete
            options = requests.options(link).status_code
            if options != 405:
                result[link]["OPTIONS"] = options
            patch = requests.patch(link).status_code
            if patch != 405:
                result[link]["PATCH"] = patch
    return json.dumps(result, indent=4)


if __name__ == "__main__":
    string_list = ["https://google.com",
                   "https://youtube.com",
                   "Какая то строка",
                   "http://grkdvjktu.com",
                   "google.com",
                   "http://yandex.ru"]
    print(get_methods(string_list))
