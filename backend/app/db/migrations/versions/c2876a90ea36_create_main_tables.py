"""create_main_tables

Revision ID: c2876a90ea36
Revises: 
Create Date: 2022-01-09 19:12:56.035433

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic
revision = 'c2876a90ea36'
down_revision = None
branch_labels = None
depends_on = None

def create_cleanings_table() -> None:
    op.create_table(
        "property",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.Text, nullable=False, index=True),
        sa.Column("lat", sa.Float, nullable=True),
        sa.Column("lon", sa.Float, nullable=True),
    )
    op.create_table(
        "tracker",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("lat", sa.Float, nullable=False, index=True),
        sa.Column("lon", sa.Float, nullable=True),
    )


def upgrade() -> None:
    create_cleanings_table()


def downgrade() -> None:
    op.drop_table("property")
    op.drop_table("tracker")

