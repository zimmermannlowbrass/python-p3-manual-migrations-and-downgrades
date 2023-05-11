"""Renaming name to last_name column

Revision ID: 627489f32358
Revises: 791279dd0760
Create Date: 2023-05-11 11:22:27.936778

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '627489f32358'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('students', 'name', new_column_name='last_name')


def downgrade() -> None:
    op.alter_column('students', 'last_name', new_column_name='name')
