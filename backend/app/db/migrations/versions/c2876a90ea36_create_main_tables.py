"""create_main_tables

Revision ID: c2876a90ea36
Revises: 
Create Date: 2022-01-09 19:12:56.035433

"""
from alembic import op
import sqlalchemy as sa
from typing import Tuple


# revision identifiers, used by Alembic
revision = 'c2876a90ea36'
down_revision = None
branch_labels = None
depends_on = None

def timestamps(indexed: bool = False) -> Tuple[sa.Column]:
    return (
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
            index=indexed,
        ),
    )

def create_cleanings_table() -> None:
    propery = op.create_table(
        "property",
        sa.Column("id", sa.Integer, primary_key=True, unique=True, autoincrement=True),
        sa.Column("name", sa.Text, nullable=False, index=True),
        sa.Column("lat", sa.Float, nullable=False),
        sa.Column("lon", sa.Float, nullable=False),
    )
    tracker = op.create_table(
        "tracker",
        sa.Column("id", sa.Integer, primary_key=True, unique=True, autoincrement=True),
        sa.Column("lat", sa.Float, nullable=False),
        sa.Column("lon", sa.Float, nullable=False),
        *timestamps(),
    )

    op.bulk_insert(propery,
        [
            {
                'name':'Megatlon Barracas',
                'lat': -34.648872228362585, 
                'lon': -58.376403759816014 
            },
            {
                'name':'GYM Boca',
                'lat': -34.637745655618225, 
                'lon': -58.37338706348471 
            },
            {
                'name':'Easy Barracas',
                'lat': -34.63905106073504, 
                'lon': -58.3780133355436 
            }
        ]
    )

    op.bulk_insert(tracker,
        [
            {                
                'lat': -34.649058307483806, 
                'lon': -58.37636729747837 
            },
            {
                'lat': -34.649043257849996, 
                'lon': -58.37632789481542 
            },
            {
                'lat': -34.648448206472764, 
                'lon': -58.37700745325494 
            },
            {
                'lat': -34.646642792265524, 
                'lon': -58.377865376019486 
            },
            {
                'lat': -34.64743799140717, 
                'lon': -58.37371978605836
            }
        ]
    )

def upgrade() -> None:
    create_cleanings_table()

def downgrade() -> None:
    op.drop_table("property")
    op.drop_table("tracker")

