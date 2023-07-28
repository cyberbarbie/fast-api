"""add user table

Revision ID: 5151ae45cc90
Revises: 907afcf64985
Create Date: 2023-07-27 21:16:32.600134

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5151ae45cc90'
down_revision = '907afcf64985'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass
