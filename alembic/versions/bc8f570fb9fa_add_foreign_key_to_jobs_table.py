"""add foreign key to jobs table

Revision ID: bc8f570fb9fa
Revises: 0330807cdb8e
Create Date: 2023-12-25 15:26:14.406564

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bc8f570fb9fa'
down_revision: Union[str, None] = '0330807cdb8e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("jobs", sa.Column("user_id", sa.Integer(), nullable=False))
    #you have to give arbitraqry name to the foreign key then specify the source table, and then the target table and then the source column and then the target column
    op.create_foreign_key("fk_jobs_user_id", source_table="jobs", referent_table="users", local_cols=["user_id"], remote_cols=["id"], ondelete="CASCADE",)
    pass


def downgrade() -> None:
    op.drop_constraint("fk_jobs_user_id", "jobs", type_="foreignkey")
    op.drop_column("jobs", "user_id")
    pass
