import requests
import json


def url_or_string(link):
    """Функция определяет является строка ссылкой"""
    try:
        response = requests.get(link)
        if "text/html" in response.headers["Content-Type"]:
            return True
        else:
            return False
    except requests.ConnectionError as exception:
        print(f"{exception}: Строка '{link}' не является ссылкой")
    except requests.exceptions.InvalidURL as exception:
        print(f"{exception}: Строка '{link}' не является ссылкой")


def get_methods(string_list):
    """Функция определяет какие http методы доступны по ссылке
    и возвращает json
    """
    result = {}
    ctat_code = {}
    for link in string_list:
        if url_or_string(link):
            get = requests.get(link).status_code
            if get != 405:
                ctat_code["GET"] = get
                result[link] = ctat_code
            head = requests.head(link).status_code
            if head != 405:
                ctat_code["HEAD"] = head
                result[link] = ctat_code
            post = requests.post(link).status_code
            if post != 405:
                ctat_code["POST"] = post
                result[link] = ctat_code
            put = requests.put(link).status_code
            if put != 405:
                ctat_code["PUT"] = put
                result[link] = ctat_code
            delete = requests.delete(link).status_code
            if delete != 405:
                ctat_code["DELETE"] = delete
                result[link] = ctat_code
            options = requests.options(link).status_code
            if options != 405:
                ctat_code["OPTIONS"] = options
                result[link] = ctat_code
            patch = requests.patch(link).status_code
            if patch != 405:
                ctat_code["PATCH"] = patch
                result[link] = ctat_code
    return json.dumps(result, indent=4)


if __name__ == "__main__":
    string_list = ["https://google.com",
                   "https://youtube.com",
                   "Какая то строка",
                   "http://grkdvjktu.com",
                   "http://yandex.ru"]
    print(get_methods(string_list))
