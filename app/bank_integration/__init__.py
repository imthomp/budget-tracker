from datetime import datetime

from plaid import ApiClient, Configuration, Environment
from plaid.api import plaid_api
from plaid.model.transactions_get_request import TransactionsGetRequest
from plaid.model.transactions_get_request_options import TransactionsGetRequestOptions

from ..config import Config
from ..models import Transaction


def _create_client():
    configuration = Configuration(
        host=getattr(Environment, Config.PLAID_ENV.capitalize()),
        api_key={
            "PLAID-CLIENT-ID": Config.PLAID_CLIENT_ID,
            "PLAID-SECRET": Config.PLAID_SECRET,
        },
    )
    api_client = ApiClient(configuration)
    return plaid_api.PlaidApi(api_client)


client = _create_client()


def fetch_transactions(account_id, start_date, end_date):
    """Fetch transactions for an account and return ``Transaction`` objects."""
    request = TransactionsGetRequest(
        access_token=account_id,
        start_date=start_date,
        end_date=end_date,
        options=TransactionsGetRequestOptions(),
    )
    response = client.transactions_get(request)
    transactions = []
    for item in response['transactions']:
        tx = Transaction(
            amount=item['amount'],
            category=item['category'][0] if item.get('category') else 'Other',
            date=datetime.strptime(item['date'], '%Y-%m-%d').date(),
            description=item.get('name', ''),
        )
        transactions.append(tx)
    return transactions
