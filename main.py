from flask import Blueprint, render_template, abort, redirect, url_for, request
from jinja2 import TemplateNotFound
from forms import CardInput


main_bp = Blueprint('main_bp', __name__)



@main_bp.route('/' , methods=['GET', 'POST'])
def home_page():
    form = CardInput()
    if request.method == 'POST':
        return redirect(url_for('main_bp.survey', card_list=request.form['cards']))
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