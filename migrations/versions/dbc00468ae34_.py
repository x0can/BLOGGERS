"""empty message

Revision ID: dbc00468ae34
Revises: 8bdeb2db6623
Create Date: 2019-10-27 08:31:21.863750

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dbc00468ae34'
down_revision = '8bdeb2db6623'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('blogs_comment_id_fkey', 'blogs', type_='foreignkey')
    op.drop_column('blogs', 'comment_id')
    op.add_column('comment', sa.Column('blogs_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'comment', 'blogs', ['blogs_id'], ['id'])
    op.drop_column('comment', 'comment')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment', sa.Column('comment', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'comment', type_='foreignkey')
    op.drop_column('comment', 'blogs_id')
    op.add_column('blogs', sa.Column('comment_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('blogs_comment_id_fkey', 'blogs', 'comment', ['comment_id'], ['id'])
    # ### end Alembic commands ###