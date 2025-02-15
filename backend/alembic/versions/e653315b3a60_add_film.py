"""

Revision ID: e653315b3a60
Revises: 
Create Date: 2024-12-11 16:50:11.224789

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "e653315b3a60"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "film",
        sa.Column("original_title", sa.String(), nullable=False),
        sa.Column("english_title", sa.String(), nullable=True),
        sa.Column("year", sa.Integer(), nullable=False),
        sa.Column("filmweb_rating", sa.Numeric(precision=4, scale=2), nullable=True),
        sa.Column("imdb_rating", sa.Numeric(precision=4, scale=2), nullable=True),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("original_title"),
    )


def downgrade() -> None:
    op.drop_table("film")
