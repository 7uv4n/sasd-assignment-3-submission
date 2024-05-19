@echo off

REM Set environment variables
set FLASK_APP=app.py
set FLASK_DEBUG=true

REM Check if venv is installed
echo Updating dependencies
python -m pip install --upgrade pip
python -m pip install virtualenv

REM Check if there's a venv directory
if not exist .venv (
    echo Creating a virtual environment
    python -m venv .venv
)

echo Activating virtual environment
call .venv\Scripts\activate

echo Installing Python requirements
python -m pip install -r requirements.txt
python -m pip install Flask-Migrate

echo Starting app server now
flask run
