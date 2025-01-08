"""Add metacritic ratings

Revision ID: c3643b2b76df
Revises: 6897518f6f81
Create Date: 2025-01-07 21:04:13.923226

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "c3643b2b76df"
down_revision: Union[str, None] = "6897518f6f81"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "film", sa.Column("metacritic_rating", sa.Numeric(precision=2), nullable=True)
    )
    op.create_foreign_key("fk_film_genre", "film_genre", "film", ["film_id"], ["id"])
    op.create_foreign_key("fk_genre_film", "film_genre", "genre", ["genre_id"], ["id"])


def downgrade() -> None:
    op.drop_constraint("fk_film_genre", "film_genre", type_="foreignkey")
    op.drop_constraint("fk_genre_film", "film_genre", type_="foreignkey")
    op.drop_column("film", "metacritic_rating")
