"""empty message

Revision ID: 04703a48641f
Revises: a3f0af5da51d
Create Date: 2024-02-10 12:22:10.771228

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '04703a48641f'
down_revision = 'a3f0af5da51d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.String(length=120), nullable=False))
        batch_op.drop_column('name')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.VARCHAR(length=120), autoincrement=False, nullable=False))
        batch_op.drop_column('email')

    # ### end Alembic commands ###
