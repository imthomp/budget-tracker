# Budget Tracker

A multi-user budget tracker built with Flask. Users can register accounts, log in, and record income or expenses. The dashboard lists recent transactions and provides a form to add more. Data is stored in SQLite by default.

## Setup
1. Create a virtual environment and install requirements:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   flask --app run.py run
   ```

A default development database `app.db` will be created on first run.
