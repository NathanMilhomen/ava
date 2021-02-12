"""empty message

Revision ID: 384c1ab3091e
Revises: da3972a435fa
Create Date: 2021-02-12 15:20:53.187008

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '384c1ab3091e'
down_revision = 'da3972a435fa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('university_professor',
    sa.Column('university_id', sa.Integer(), nullable=False),
    sa.Column('professor_id', sa.String(length=11), nullable=True),
    sa.ForeignKeyConstraint(['professor_id'], ['professor.id'], ),
    sa.ForeignKeyConstraint(['university_id'], ['university.id'], ),
    sa.PrimaryKeyConstraint('university_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('university_professor')
    # ### end Alembic commands ###