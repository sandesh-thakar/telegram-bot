# telegram-bot

## Installation

1. Clone this repository to your local machine

2. Create a virtual environment

```
python3 -m venv venv
```

3. Activate the virtual environment

```
source venv/bin/activate
```

4. Install the required libraries and dependencies from the `requirements.txt` file

```
pip install -r requirements.txt
```

5. Running database migrations: This will create a local SQLite database and create the necessary tables

```
(Open a new terminal)
cd backend
alembic upgrade head
```

6. Setup Redis

```
brew install redis
redis-server
```

## Running the application

1. Starting the backend server

```
(Open a new terminal)
source venv/bin/activate
cd backend
uvicorn main:app --reload
```

2. Starting the frontend client

```
(Open a new terminal)
cd frontend
npm install
npm start
```

3. Starting celery

```
(Open a new terminal)
source venv/bin/activate
celery -A celery_tasks.celery worker --loglevel=info
```

4. Starting the telegram bot

```
(Open a new terminal)
source venv/bin/activate
python telegram_bot.py
```

5. Accessing the bot on telegram

```
Open https://t.me/timelyaitask_bot
```
