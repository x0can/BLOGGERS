"""empty message

Revision ID: 8e5fd5bf55c4
Revises: 962e67bdd6ce
Create Date: 2019-10-29 20:53:22.543269

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e5fd5bf55c4'
down_revision = '962e67bdd6ce'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('profile_pic_path', sa.NullType(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'profile_pic_path')
    # ### end Alembic commands ###
