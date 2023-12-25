"""add descriptions again

Revision ID: 026419a8c053
Revises: 144f97638340
Create Date: 2023-12-25 15:15:26.483161

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '026419a8c053'
down_revision: Union[str, None] = '144f97638340'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("jobs", sa.Column("description", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("jobs", "description")
    pass
