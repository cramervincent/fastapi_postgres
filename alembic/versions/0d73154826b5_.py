"""empty message

Revision ID: 0d73154826b5
Revises: cec44851eaf5
Create Date: 2023-02-14 20:16:22.466634

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0d73154826b5'
down_revision = 'cec44851eaf5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('fullname', sa.String(), nullable=True))
    op.drop_column('users', 'first_name')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('first_name', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('users', 'fullname')
    # ### end Alembic commands ###