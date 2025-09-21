Установка:
1. Клонировать репозиторий `git clone https://github.com/USW5sPlusom/Algorhythmica`
2. Создать виртуальное окружение: `python -m venv venv`
3. Активировать окружение: `source venv/bin/activate` (Linux/Mac) или `venv\Scripts\activate` (Windows)
4. Установить зависимости: `pip install -r requirements.txt`
5. Создать файл настроек: `cp settings_template.py algorhythmica/settings.py`
6. Настроить SECRET_KEY и другие параметры в settings.py
7. Выполнить миграции: `python manage.py migrate`
8. Запустить сервер: `python manage.py runserver`