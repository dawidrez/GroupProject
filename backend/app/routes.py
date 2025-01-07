from flask import Blueprint, Response, jsonify, request

from .helpers.pagination import create_pagination
from .schemas import FilmSchema, GenreSchema
from .services.film_service import get_paginated_films
from .services.genre_service import get_all_genres

film = Blueprint("film", __name__)


@film.route("/films", methods=["GET"])
def list_films() -> Response:
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", 10))
    genre = request.args.get("genre")
    title = request.args.get("title")

    films, total_count = get_paginated_films(
        page=page, per_page=per_page, genre_name=genre, title=title
    )

    pagination = create_pagination(page, per_page, total_count)
    return jsonify(
        {
            "items": [FilmSchema.model_validate(film).model_dump() for film in films],
            "pagination": pagination,
        }
    )


@film.route("/genres", methods=["GET"])
def list_genres() -> Response:
    genres = get_all_genres()
    genre_schemas = [GenreSchema.model_validate(genre).model_dump() for genre in genres]
    return jsonify(items=genre_schemas)
