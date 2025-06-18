from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class ShareAccountForm(FlaskForm):
    username = StringField('Partner Username', validators=[DataRequired()])
    submit = SubmitField('Share Account')
