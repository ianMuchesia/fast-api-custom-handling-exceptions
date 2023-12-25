"""add columns again,because the first one had bugs

Revision ID: 874295f771df
Revises: fb8fe29f6280
Create Date: 2023-12-25 15:46:46.747438

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '874295f771df'
down_revision: Union[str, None] = 'fb8fe29f6280'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
