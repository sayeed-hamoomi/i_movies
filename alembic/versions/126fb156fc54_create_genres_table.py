"""create genres table

Revision ID: 126fb156fc54
Revises: add9185ac6bf
Create Date: 2024-05-12 14:35:14.791089

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '126fb156fc54'
down_revision: Union[str, None] = 'add9185ac6bf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Genres',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('genre_name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('genre_name')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Genres')
    # ### end Alembic commands ###
