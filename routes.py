from flask import Blueprint

short = Blueprint('short', __name__)

@short.route('/<short_url>')
def redirect_to_url(short_url):
    pass

