"""create_main_tables

Revision ID: c2876a90ea36
Revises: 
Create Date: 2022-01-09 19:12:56.035433

"""
from alembic import op
import sqlalchemy as sa
import datetime


# revision identifiers, used by Alembic
revision = 'c2876a90ea36'
down_revision = None
branch_labels = None
depends_on = None

def create_cleanings_table() -> None:
    propery = op.create_table(
        "property",
        sa.Column("id", sa.Integer, primary_key=True, unique=True, autoincrement=True),
        sa.Column("name", sa.Text, nullable=False, index=True),
        sa.Column("lat", sa.Float, nullable=False),
        sa.Column("lon", sa.Float, nullable=False),
    )
    op.create_table(
        "tracker",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("lat", sa.Float, nullable=False),
        sa.Column("lon", sa.Float, nullable=False),
        sa.Column("date", sa.DateTime(timezone=True), nullable=True, server_default=sa.sql.func.now()),
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

def upgrade() -> None:
    create_cleanings_table()

def downgrade() -> None:
    op.drop_table("property")
    op.drop_table("tracker")

