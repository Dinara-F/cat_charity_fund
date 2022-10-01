# QRKot
A training project of the application API for the QRKot Cat Charitable Foundation. Its purpose is to collect and distribute donations among various projects.
## Developers
- [Dinara Fatekhova](https://github.com/Dinara-F)
## Technologies
- [Python](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](http://www.sqlalchemy.org/)
- [Alembic](https://alembic.sqlalchemy.org/)
- [FastAPI Users](https://fastapi-users.github.io/fastapi-users/)
- [Uvicorn](https://www.uvicorn.org/)
## Instructions
Clone the repository:
```
git clone
```
Create and activate virtual environment:
```
python -m venv venv
```
Install requirements.txt:
```
pip install -r requirements.txt
``` 
Run migrations
```
alembic upgrade head
```
Run server
```
uvicorn app.main:app --reload
```
