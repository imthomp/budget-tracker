from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user

from . import account_bp
from .forms import ShareAccountForm
from ..models import db, User

@account_bp.route('/share', methods=['GET', 'POST'])
@login_required
def share_account():
    form = ShareAccountForm()
    if form.validate_on_submit():
        partner = User.query.filter_by(username=form.username.data).first()
        if partner:
            current_user.account = partner.account
            db.session.commit()
            flash(f'Account shared with {partner.username}.', 'success')
            return redirect(url_for('budget.dashboard'))
        flash('User not found.', 'danger')
    return render_template('account/share.html', form=form)
