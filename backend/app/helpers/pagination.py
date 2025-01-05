from typing import TypedDict


class Pagination(TypedDict):
    total_items: int
    total_pages: int
    current_page: int
    per_page: int
    has_prev: bool
    has_next: bool
    prev_page: int | None
    next_page: int | None


def create_pagination(current_page: int, per_page: int, total_items: int) -> Pagination:
    last_page = (total_items - 1) // per_page + 1
    return {
        "total_items": total_items,
        "total_pages": last_page,
        "current_page": current_page,
        "per_page": per_page,
        "has_prev": current_page > 1,
        "has_next": current_page < last_page,
        "prev_page": current_page - 1 if current_page > 1 else None,
        "next_page": current_page + 1 if current_page < last_page else None,
    }
