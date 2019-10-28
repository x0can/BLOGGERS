"""empty message

Revision ID: 9e446d7fc356
Revises: 6bce1dd2112f
Create Date: 2019-10-27 20:05:39.577378

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9e446d7fc356'
down_revision = '6bce1dd2112f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('blogs_user_id_fkey', 'blogs', type_='foreignkey')
    op.drop_column('blogs', 'user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogs', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('blogs_user_id_fkey', 'blogs', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###