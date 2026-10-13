"""create user table

Revision ID: ef460bde9fd3
Revises: 
Create Date: 2026-10-13 14:41:04.070321+00:00

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ef460bde9fd3'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table("user",
                    sa.Column('id', sa.Integer, nullable=False, primary_key=True),
                    sa.Column('email', sa.String(length=120), nullable=False, unique=True),
                    sa.Column('password', sa.String(length=120), nullable=False),
                    sa.Column('password_salt', sa.String(length=120), nullable=False, unique=True),
                    sa.Column("created_at", sa.DateTime, nullable=False, server_default=sa.func.now()),
                    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("user")
