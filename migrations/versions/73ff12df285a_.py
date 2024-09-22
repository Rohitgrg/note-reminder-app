"""empty message

Revision ID: 73ff12df285a
Revises: 1486b35104eb
Create Date: 2024-09-22 14:02:49.544653

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '73ff12df285a'
down_revision = '1486b35104eb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reminder',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('reminder_date', sa.DateTime(), nullable=True),
    sa.Column('note_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['note_id'], ['note.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reminder')
    # ### end Alembic commands ###
