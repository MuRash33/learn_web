"""added email to user

Revision ID: 8c603fe9454b
Revises: c7b1df75d934
Create Date: 2019-04-15 19:56:12.400924

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8c603fe9454b'
down_revision = 'c7b1df75d934'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('news', sa.Column('email', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('news', 'email')
    # ### end Alembic commands ###
