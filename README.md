# Merhaba Server

This is the server/backend for the Merhaba app.

## Setup

### Local Bash-based OS

1. Clone the repo
2. Set current directory as repo
3. `python -m venv .` (This only needs to happen once)
4. `source ./bin/activate` (Do this every time you start a new session)
5. `pip install -r requirements.txt` (Do this every time requirements.txt is updated)
6. Create a `.env` and fill in the keys provided in `.env-example` (Make sure to keep the `.env` updated with `.env-example` BUT DON'T COMMIT `.env`)
7. The setup is done, to start the server run `flask --app ./src/main.py run` (Do this every time you want to restart the program)

### Local Windows

1. Clone the repo
2. Set current directory as repo
3. `python -m venv .` (This only needs to happen once)
4. `.\Scripts\activate` (Do this every time you start a new session)
5. `pip install -r requirements.txt` (Do this every time requirements.txt is updated)
6. Create a `.env` and fill in the keys provided in `.env-example` (Make sure to keep the `.env` updated with `.env-example` BUT DON'T COMMIT `.env`)
7. The setup is done, to start the server run `flask --app ./src/main.py run` (Do this every time you want to restart the program)

### Replit

1. Clone the repo
2. `python -m venv .` (This only needs to happen once)
3. `source ./bin/activate` (Do this every time you start a new session)
4. `pip install -r requirements.txt` (Do this every time requirements.txt is updated)
5. Set replit secrets to mirror those in the `.env-example` (Make sure to keep the secrets updated with `.env-example`)
6. The setup is done, to start the server run `flask --app ./src/main.py run --host 0.0.0.0` (Do this every time you want to restart the program)

## Commiting
- Don't commit the `.env` (It should already be in the `.gitignore` but this is very crucial)
- If you installed new libs, update `requirements.txt` with `pip freeze > requirements.txt`
- Don't commit the python venv directories (the ones created when `python -m venv .` was run), however I believe these are already covered in the `.gitignore`
