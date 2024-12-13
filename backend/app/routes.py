from flask import Blueprint, jsonify

from .schemas import FilmSchema
from .services.film_service import get_all_films

film = Blueprint("film", __name__)


@film.route("/films", methods=["GET"])
def list_films():
    films = get_all_films()
    film_schemas = [FilmSchema.from_orm(film).dict() for film in films]
    return jsonify(film_schemas)
