"""create posts table

Revision ID: 04dc007e9c15
Revises: 
Create Date: 2023-12-25 14:12:54.329108

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '04dc007e9c15'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('jobs', sa.Column('id', sa.Integer(),nullable=False,primary_key=True)),
    sa.Column('title', sa.String(), nullable=False)
    
    


def downgrade() -> None:
    op.drop_table("posts")
