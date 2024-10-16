"""create greeting

Revision ID: bf293d3e5a43
Revises: 9bc6add9584b
Create Date: 2024-10-16 14:38:34.353957

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bf293d3e5a43'
down_revision = '9bc6add9584b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('greeting',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(length=16), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('text')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('greeting')
    # ### end Alembic commands ###
