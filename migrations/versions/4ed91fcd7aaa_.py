"""empty message

Revision ID: 4ed91fcd7aaa
Revises: b4b0c5fd65ec
Create Date: 2019-02-11 15:16:46.609797

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4ed91fcd7aaa'
down_revision = 'b4b0c5fd65ec'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('url_photo', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'url_photo')
    # ### end Alembic commands ###
