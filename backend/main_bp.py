from flask import Blueprint, render_template, abort, redirect, url_for, request
from jinja2 import TemplateNotFound
from backend.forms import CardInput
from backend.filter_list import get_creatures

main_bp = Blueprint('main_bp', __name__)



@main_bp.route('/' , methods=['GET', 'POST'])
def home_page():
    form = CardInput()
    try:
        return render_template('index.html', form=form)
    except TemplateNotFound:
        abort(404)

@main_bp.route('/survey', methods=['GET', 'POST'])
def survey():
    if request.method != 'POST':
        return redirect('/')
    duplicate_subtypes, single_subtypes=get_creatures([card[2:] for card in request.form['cards'].splitlines()])
    return render_template('survey.html', duplicates=duplicate_subtypes, singles=single_subtypes)
