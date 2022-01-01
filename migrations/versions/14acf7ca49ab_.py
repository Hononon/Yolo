"""empty message

Revision ID: 14acf7ca49ab
Revises: f02631405b0d
Create Date: 2021-08-12 17:29:13.831464

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '14acf7ca49ab'
down_revision = 'f02631405b0d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('new_video', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'new_video')
    # ### end Alembic commands ###
