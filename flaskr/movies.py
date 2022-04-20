from flask import Blueprint, request, render_template   #Import data from flask
from flaskr.db import get_movies

bp = Blueprint('movies', __name__, url_prefix='/movies')    #Set bp to the Blueprint module

@bp.route('/', methods=['GET'])
def movie_list():   #Define a Movie list and return a rendered template of the movies
    movies = get_movies()
    return render_template('movies.html', movies=movies)