"""add venue social rooms

Revision ID: d3f8eeee7681
Revises: 0863e495a8e8
Create Date: 2026-01-02 14:03:36.488124

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd3f8eeee7681'
down_revision: Union[str, Sequence[str], None] = '0863e495a8e8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
