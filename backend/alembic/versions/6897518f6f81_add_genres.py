"""add genres

Revision ID: 6897518f6f81
Revises: e653315b3a60
Create Date: 2024-12-13 10:31:06.335107

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "6897518f6f81"
down_revision: Union[str, None] = "e653315b3a60"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "film_genre",
        sa.Column("film_id", sa.Uuid(), nullable=False, foreign_key="film.id"),
        sa.Column("genre_id", sa.Uuid(), nullable=False, foreign_key="genre.id"),
        sa.PrimaryKeyConstraint("film_id", "genre_id"),
    )
    op.create_table(
        "genre",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    op.add_column("film", sa.Column("src", sa.String(), nullable=False))
    op.create_unique_constraint("film_src_constraint", "film", ["src"])
    # ### end Alembic commands ###


def downgrade() -> None:
    op.drop_constraint("film_src_constraint", "film", type_="unique")
    op.drop_column("film", "src")
    op.create_table(
        "user",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column(
            "username", sa.VARCHAR(length=80), autoincrement=False, nullable=False
        ),
        sa.PrimaryKeyConstraint("id", name="user_pkey"),
        sa.UniqueConstraint("username", name="user_username_key"),
    )
    op.drop_table("genre")
    op.drop_table("film_genre")
    # ### end Alembic commands ###
