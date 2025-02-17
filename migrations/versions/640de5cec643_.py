"""empty message

Revision ID: 640de5cec643
Revises: ac166e618624
Create Date: 2024-06-13 09:37:01.827233

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '640de5cec643'
down_revision = 'ac166e618624'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('imagem', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_column('imagem')

    # ### end Alembic commands ###
