"""add user table

Revision ID: 0330807cdb8e
Revises: 026419a8c053
Create Date: 2023-12-25 15:19:24.047249

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0330807cdb8e'
down_revision: Union[str, None] = '026419a8c053'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column("username", sa.String(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("password", sa.String(), nullable=False),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True),server_default=sa.text("now()"),nullable=False),
        sa.UniqueConstraint("email")
      
    )
    pass


def downgrade() -> None:
    op.drop_table("users")
    pass
