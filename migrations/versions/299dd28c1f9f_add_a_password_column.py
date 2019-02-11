"""Add a password column

Revision ID: 299dd28c1f9f
Revises: 42e79010ae84
Create Date: 2019-02-08 11:47:35.583157

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '299dd28c1f9f'
down_revision = '42e79010ae84'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pass_secure', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'pass_secure')
    # ### end Alembic commands ###
