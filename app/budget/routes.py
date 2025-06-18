from flask import render_template, redirect, url_for
from flask_login import login_required, current_user
from datetime import date

from . import budget_bp
from .forms import TransactionForm
from ..models import db, Transaction


@budget_bp.route('/')
@login_required
def dashboard():
    transactions = Transaction.query.filter_by(account=current_user.account).order_by(Transaction.date.desc()).all()
    form = TransactionForm()
    month_start = date.today().replace(day=1)
    monthly = [tx for tx in transactions if tx.date >= month_start]
    total_income = sum(tx.amount for tx in monthly if tx.amount > 0)
    total_expenses = sum(-tx.amount for tx in monthly if tx.amount < 0)
    category_totals = {}
    for tx in monthly:
        category_totals[tx.category] = category_totals.get(tx.category, 0) + tx.amount
    return render_template(
        'budget/dashboard.html',
        transactions=transactions,
        form=form,
        total_income=total_income,
        total_expenses=total_expenses,
        category_totals=category_totals
    )


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
            user=current_user,
            account=current_user.account
        )
        db.session.add(transaction)
        db.session.commit()
    return redirect(url_for('budget.dashboard'))
