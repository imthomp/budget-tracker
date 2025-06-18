# Budget Tracker

A multi-user budget tracker built with Flask. Users can register accounts, log in, and record income or expenses. Accounts can be shared with another user and the dashboard shows monthly summaries with category charts. Data is stored in SQLite by default.

## Setup

1. Create a virtual environment and install requirements. The project pins
   `Werkzeug<3` for compatibility with Flask-Login, so re-run the install
   command after updating `requirements.txt`:

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
If you have an older copy of `app.db` from a previous version of the app,
remove it so that the new account-sharing tables can be created automatically.

### Bank integration

The optional bank sync feature uses the Plaid API. Set the following
environment variables before running the app:

```
PLAID_CLIENT_ID=your_client_id
PLAID_SECRET=your_secret
PLAID_ENV=sandbox  # or development/production
```

After configuring these values and installing `plaid-python`, a button on the
dashboard allows syncing transactions from your linked bank account.
