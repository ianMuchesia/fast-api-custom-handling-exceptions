"""add description column  to jobs table

Revision ID: 144f97638340
Revises: 04dc007e9c15
Create Date: 2023-12-25 15:08:36.822565

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '144f97638340'
down_revision: Union[str, None] = '04dc007e9c15'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("jobs", sa.Column("description", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("jobs", "description")
    pass
