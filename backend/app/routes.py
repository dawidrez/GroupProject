from flask import Blueprint, Response, jsonify, request

from .helpers.pagination import create_pagination
from .schemas import FilmSchema
from .services.film_service import get_paginated_films

film = Blueprint("film", __name__)


@film.route("/films", methods=["GET"])
def list_films() -> Response:
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 25, type=int)
    films, total_count = get_paginated_films(page, per_page)
    film_schemas = [FilmSchema.model_validate(film).model_dump() for film in films]
    return jsonify(
        items=film_schemas, pagination=create_pagination(page, per_page, total_count)
    )
