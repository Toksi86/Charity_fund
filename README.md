# Благотоворительные сборы

Сервис позволяет создавать и управлять благотворительными проектами.

## Установка

1. Склонируйте репозиторий:

    ```bash
    git clone [https://github.com/Toksi86/catcharity_fund.git](https://github.com/Toksi86/Charity_fund.git)
    ```

2. Перейдите в каталог проекта 
    ```bash
    cd cat_charity_fund/
    ```

3. Создайте виртуальную среду окружения
    ```bash
    python -m venv .venv
    ```

4. Активируйте вирутальную среду окружения
    ```bash
    source .venv/Scripts/activate
    ```

5. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```


6. Настройте переменные окружения
    - Создайте файл `.env` в корне проекта
        ```bash
        touch .env
        ```
    - Заполнить .env файл по примеру

        ```
        APP_TITLE=Заголовок вашего приложения
        DATABASE_URL=ваша_ссылка_на_базу_данных
        SECRET=ваш_секретный_ключ
        FIRST_SUPERUSER_EMAIL=почта_администратора
        FIRST_SUPERUSER_PASSWORD=пароль_администратора
        ```

7. Инициализируйте базу данных
    ```bash
    alembic.exe upgrade head
    ```

8. Запустите приложение:
    ```
    uvicorn app.main:app
    ```

## Автор

Автор проекта - [Шперлинг Константин](https://github.com/Toksi86/).

## Стек технологий

Проект реализован с использованием следующих технологий:
- Python
- FastAPI
- SQLAlchemy
- SQLite
- Alembic
- Pydantic
- FastAPI Users
- PyJWT
- OAuth2
- Swagger UI
- ReDoc
- Postman

## Доступ к справке

Доступ к справке предоставляется через ReDoc и Swagger UI.

ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Контакты

Если у вас есть вопросы или предложения, пожалуйста, свяжитесь со мной:

- Telegram: [@Toksi86](https://t.me/Toksi86)
