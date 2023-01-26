"""empty message

Revision ID: 722ad4e900cb
Revises: 45e54ff9f84c
Create Date: 2023-01-26 13:52:13.866167

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '722ad4e900cb'
down_revision = '45e54ff9f84c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('nombre', sa.String(length=250), nullable=False))
        batch_op.add_column(sa.Column('contraseña', sa.String(length=20), nullable=False))
        batch_op.add_column(sa.Column('mail', sa.String(length=100), nullable=False))
        batch_op.drop_constraint('user_email_key', type_='unique')
        batch_op.drop_column('is_active')
        batch_op.drop_column('email')
        batch_op.drop_column('password')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.VARCHAR(length=80), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False))
        batch_op.create_unique_constraint('user_email_key', ['email'])
        batch_op.drop_column('mail')
        batch_op.drop_column('contraseña')
        batch_op.drop_column('nombre')

    # ### end Alembic commands ###
