"""empty message

Revision ID: bcdf48d944b7
Revises: 9c679d5283b3
Create Date: 2021-02-04 16:11:26.151050

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'bcdf48d944b7'
down_revision = '9c679d5283b3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('student', 'teste')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('student', sa.Column('teste', mysql.VARCHAR(length=250), nullable=True))
    # ### end Alembic commands ###
