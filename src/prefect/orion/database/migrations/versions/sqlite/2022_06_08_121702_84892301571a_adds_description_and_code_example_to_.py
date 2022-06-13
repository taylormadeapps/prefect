"""Adds description and code example to block type

Revision ID: 84892301571a
Revises: f65b6ad0b869
Create Date: 2022-06-08 12:17:02.928460

"""
import sqlalchemy as sa
from alembic import op

import prefect

# revision identifiers, used by Alembic.
revision = "84892301571a"
down_revision = "f65b6ad0b869"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("block_type") as batch_op:
        batch_op.add_column(sa.Column("description", sa.String(), nullable=True))
        batch_op.add_column(sa.Column("code_example", sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("block_type") as batch_op:
        batch_op.drop_column("code_example")
        batch_op.drop_column("description")
    # ### end Alembic commands ###
