# QRKot
Сервис для поддержки котиков!
## Команда разработчиков
Динара Фатехова <https://github.com/Dinara-F>
## Технологии
- Python
- FastAPI
- SQLAlchemy
## Инструкции
Клонировать репозиторий:
```
git clone
```
Создать и активировать виртуальное окружение:
```
python -m venv venv
```
Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
``` 
Применить миграции
```
alembic upgrade head
```
Запустить сервер из корневой папки проекта
```
uvicorn app.main:app --reload
```