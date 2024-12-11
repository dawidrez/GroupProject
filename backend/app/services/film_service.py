from sqlalchemy.orm import Session

from ..models import Film

def get_all_films(session: Session):
    """Fetch all films from the database."""
    return session. Film.query.all()