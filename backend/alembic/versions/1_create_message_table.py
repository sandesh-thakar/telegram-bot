"""create message table

Revision ID: 1
Revises: 
Create Date: 2023-10-31 13:11:11.251129

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "1"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        "messages",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("sender", sa.String, index=True),
        sa.Column("content", sa.String),
        sa.Column(
            "timestamp", sa.DateTime, server_default=sa.func.now(), nullable=False
        ),
    )


def downgrade():
    op.drop_table("messages")
