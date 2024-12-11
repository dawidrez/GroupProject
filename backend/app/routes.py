from flask import Blueprint, jsonify

from .services.film_service import get_all_films

film = Blueprint("film", __name__)


@film.route("/films", methods=["GET"])
def list_films():
    films = get_all_films()
    return jsonify([film.to_dict() for film in films])
