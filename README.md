# Проект "Заметки"

## Описание проекта
Этот проект представляет собой аналог заметок на телефоне. Он включает в себя следующие основные компоненты:
- `auth.py`: Модуль для аутентификации и авторизации.
- `main.py`: Основной модуль приложения.
- `models.py`: Модуль, содержащий определения моделей данных.
- `templates/`: Каталог с HTML-шаблонами для веб-страниц.


## Клонирование проекта
1. Откройте терминал и перейдите в каталог, где вы хотите клонировать проект

2. Выполните следующую команду для клонирования репозитория:
   ```bash
   git clone git@github.com:usershoislom/flask-app.git
   
## Запуск проекта

0. Перейдите в каталог проекта:
   ```bash
	cd flask-app

1. Перейдите на ветку dev:
   ```bash
	git checkout dev

2. Установите зависимости из Pipfile:

   ```bash
    pipenv install

3. Активируйте виртуальное окружение:

   ```bash
    pipenv shell

4. Убедитесь, что в вашем виртуальном окружении установлены все зависимости из файла `requirements.txt`:
   ```bash
   pip install -r requirements.txt

5. Установите переменную окружения FLASK_APP:

    ```bash
    export FLASK_APP=project

6. Запустите приложение Flask:
    ```bash
    flask run
   
В скором временип появятся возможности добавлять/удалять/редактировать свои заметки

