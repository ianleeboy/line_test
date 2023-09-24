"""Initial migration.

Revision ID: 164b703edf44
Revises: 
Create Date: 2023-09-24 17:29:19.091311

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '164b703edf44'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('line_id', sa.String(length=50), nullable=True),
    sa.Column('display_name', sa.String(length=255), nullable=True),
    sa.Column('picture_url', sa.String(length=255), nullable=True),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('line_id')
    )
    op.create_table('reservation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('booking_service_category', sa.String(length=50), nullable=True),
    sa.Column('booking_service', sa.String(length=150), nullable=True),
    sa.Column('booking_datetime', sa.DateTime(), nullable=True),
    sa.Column('is_canceled', sa.Boolean(), server_default='0', nullable=True),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reservation')
    op.drop_table('user')
    # ### end Alembic commands ###
