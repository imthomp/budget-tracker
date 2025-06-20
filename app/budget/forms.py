from flask_wtf import FlaskForm
from wtforms import FloatField, StringField, DateField, SubmitField
from wtforms.validators import DataRequired


class TransactionForm(FlaskForm):
    amount = FloatField('Amount', validators=[DataRequired()])
    category = StringField('Category', validators=[DataRequired()])
    date = DateField('Date', validators=[DataRequired()])
    description = StringField('Description')
    submit = SubmitField('Add')


class SyncTransactionsForm(FlaskForm):
    """Simple form with a single submit button to sync bank data."""
    submit = SubmitField('Sync Bank Transactions')
