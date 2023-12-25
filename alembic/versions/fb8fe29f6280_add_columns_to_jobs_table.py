"""add columns to jobs table

Revision ID: fb8fe29f6280
Revises: bc8f570fb9fa
Create Date: 2023-12-25 15:35:57.449881

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fb8fe29f6280'
down_revision: Union[str, None] = 'bc8f570fb9fa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    op.add_column("jobs", sa.Column("company", sa.String(), nullable=False))
    op.add_column("jobs", sa.Column("company_url", sa.String(), nullable=True))
    op.add_column("jobs", sa.Column("location", sa.String(), nullable=False))
    op.add_column("jobs", sa.Column("is_active", sa.Boolean(), nullable=False, server_default="True"))
    op.add_column("jobs", sa.Column("created_at", sa.TIMESTAMP(timezone=True), server_default=sa.text("now()"), nullable=False))
    op.add_column("jobs", sa.Column("updated_at", sa.TIMESTAMP(timezone=True), server_default=sa.text("now()"), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("jobs", "company")
    op.drop_column("jobs", "company_url")
    op.drop_column("jobs", "location")
    op.drop_column("jobs", "is_active")
    op.drop_column("jobs", "created_at")
    op.drop_column("jobs", "updated_at")
    
    pass
