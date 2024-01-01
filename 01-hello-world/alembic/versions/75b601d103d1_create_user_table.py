"""create user table

Revision ID: 75b601d103d1
Revises: 790c96e41e01
Create Date: 2023-12-31 04:57:43.809053

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '75b601d103d1'
down_revision: Union[str, None] = '790c96e41e01'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
