"""empty message

Revision ID: 8221e9728340
Revises: 4ef6247f36b5
Create Date: 2017-11-17 13:18:07.932425

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8221e9728340'
down_revision = '4ef6247f36b5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'admin')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('admin', sa.BOOLEAN(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
