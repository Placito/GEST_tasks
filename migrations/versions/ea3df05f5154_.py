"""empty message

Revision ID: ea3df05f5154
Revises: 831f9b08cfd2
Create Date: 2023-11-14 14:33:30.822642

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea3df05f5154'
down_revision = '831f9b08cfd2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('role', sa.String(length=120), nullable=False))
        batch_op.create_unique_constraint(None, ['role'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('role')

    # ### end Alembic commands ###
