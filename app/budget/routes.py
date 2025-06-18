from flask import render_template, redirect, url_for
from flask_login import login_required, current_user

from . import budget_bp
from .forms import TransactionForm
from ..models import db, Transaction


@budget_bp.route('/')
@login_required
def dashboard():
    transactions = current_user.transactions.order_by(Transaction.date.desc()).all()
    form = TransactionForm()
    return render_template('budget/dashboard.html', transactions=transactions, form=form)


@budget_bp.route('/add', methods=['POST'])
@login_required
def add_transaction():
    form = TransactionForm()
    if form.validate_on_submit():
        transaction = Transaction(
            amount=form.amount.data,
            category=form.category.data,
            date=form.date.data,
            description=form.description.data,
            user=current_user
        )
        db.session.add(transaction)
        db.session.commit()
    return redirect(url_for('budget.dashboard'))
