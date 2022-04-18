from flask import Blueprint, request, render_template
from flaskr.db import get_movies

bp = Blueprint('movies', __name__, url_prefix='/movies')

@bp.route('/', methods=['GET'])
def movie_list():
    movies = get_movies()
    hasHomepage = False
    if movies[0]['homepage'] != '':
        hasHomepage = True
    return render_template('movies.html', movies=movies, homepage=hasHomepage)