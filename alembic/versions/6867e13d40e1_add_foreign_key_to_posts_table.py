"""add foreign key to posts table

Revision ID: 6867e13d40e1
Revises: 5151ae45cc90
Create Date: 2023-07-27 21:31:49.270125

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6867e13d40e1'
down_revision = '5151ae45cc90'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', source_table="posts", referent_table="users", local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('posts_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
