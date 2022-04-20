from flask import Blueprint, request, render_template   #Imports data from flask
from flaskr.db import get_movies

bp = Blueprint('movies', __name__, url_prefix='/movies')    #Sets bp to flask's Blueprint module

@bp.route('/', methods=['GET'])
def movie_list():   #Defines the movie list, gets the movies, and returns them under a template
    movies = get_movies()
    return render_template('movies.html', movies=movies)