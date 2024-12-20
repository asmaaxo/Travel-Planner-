"""Initial migration

Revision ID: 6cd9741bf1e1
Revises: 
Create Date: 2024-12-19 22:39:37.398821

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6cd9741bf1e1'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### Create tables ###
    op.create_table(
        'trips',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True, nullable=False),
        sa.Column('name', sa.String(), unique=True, nullable=False),
        sa.Column('budget', sa.Float(), nullable=True, server_default='0.0'),
    )

    op.create_table(
        'destinations',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True, nullable=False),
        sa.Column('trip_id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.ForeignKeyConstraint(['trip_id'], ['trips.id'], ondelete='CASCADE'),
    )

    op.create_table(
        'activities',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True, nullable=False),
        sa.Column('destination_id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.ForeignKeyConstraint(['destination_id'], ['destinations.id'], ondelete='CASCADE'),
    )
    # ### End table creation ###


def downgrade() -> None:
    # ### Drop tables in reverse order ###
    op.drop_table('activities')
    op.drop_table('destinations')
    op.drop_table('trips')
    # ### End table removal ###
