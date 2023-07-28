"""add content column to posts table

Revision ID: 907afcf64985
Revises: c2544589a313
Create Date: 2023-07-27 21:08:32.637826

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '907afcf64985'
down_revision = 'c2544589a313'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass

def downgrade():
    op.drop_column("posts", "content")
    pass
