from flask import Blueprint, render_template, abort, redirect, url_for, request
from jinja2 import TemplateNotFound
from backend.forms import CardInput


main_bp = Blueprint('main_bp', __name__)



@main_bp.route('/' , methods=['GET', 'POST'])
def home_page():
    form = CardInput()
    if request.method == 'POST':
        user_input_filtered = [card[2:] for card in request.form['cards'].splitlines()]
        print(type(user_input_filtered))
        print(user_input_filtered)
        return redirect(url_for('main_bp.survey', card_list=list(user_input_filtered)))
    try:
        return render_template('index.html', form=form)
    except TemplateNotFound:
        abort(404)

@main_bp.route('/survey/<card_list>', methods=['GET', 'POST'])
def survey(card_list):
    try:
        return render_template('survey.html', card_list = card_list)
    except TemplateNotFound:
        abort(404)