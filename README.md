# Приложение помогает определить есть ли ссылки в множестве строк и какие http методы есть у ссылки

## Запуск

### 1) Клонируйте репозиторий
для этого введите в консоль:
```
git clone https://github.com/AleksSpace/string_a_link.git
```

### 2) Установите зависимости с помощью poetry
для этого перейдите в каталок в который вы клонировали репозиторий и введите в консоль:
```
poetry install
```

### 3) Запуск тестов
введите в консоль:
```
poetry run pytest -v
```

### 4) Проверка покрываемости кода тестами
введите в консоль:
```
poetry run coverage run src/main.py
```
а затем:
```
poetry run coverage report -m
```
### Об авторе
- [Заикин Алексей](https://github.com/AleksSpace "GitHub аккаунт")