from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms.validators import DataRequired


class CardInput(FlaskForm):
    cards = TextAreaField('Card list', validators=[DataRequired()])