"""init

Revision ID: 225f5a6c7cda
Revises: 
Create Date: 2024-03-13 21:50:04.527061

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '225f5a6c7cda'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('assessment_item',
    sa.Column('domain_pk', sa.Integer(), nullable=False),
    sa.Column('assessment_item_code', sa.String(), nullable=False),
    sa.Column('assessment_item_name', sa.String(), nullable=False),
    sa.Column('pk', sa.Integer(), nullable=False),
    sa.Column('date_updated', sa.DateTime(), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('pk')
    )
    op.create_index(op.f('ix_assessment_item_pk'), 'assessment_item', ['pk'], unique=False)
    op.create_table('assessor',
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('role', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('pk', sa.Integer(), nullable=False),
    sa.Column('date_updated', sa.DateTime(), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('pk')
    )
    op.create_index(op.f('ix_assessor_pk'), 'assessor', ['pk'], unique=False)
    op.create_table('child',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('birth_date', sa.DateTime(), nullable=False),
    sa.Column('admission_date', sa.DateTime(), nullable=False),
    sa.Column('discharge_date', sa.DateTime(), nullable=False),
    sa.Column('pk', sa.Integer(), nullable=False),
    sa.Column('date_updated', sa.DateTime(), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('pk')
    )
    op.create_index(op.f('ix_child_pk'), 'child', ['pk'], unique=False)
    op.create_table('domain',
    sa.Column('domain_label', sa.String(), nullable=False),
    sa.Column('domain_name', sa.String(), nullable=False),
    sa.Column('pk', sa.Integer(), nullable=False),
    sa.Column('date_updated', sa.DateTime(), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('pk')
    )
    op.create_index(op.f('ix_domain_pk'), 'domain', ['pk'], unique=False)
    op.create_table('role',
    sa.Column('role_label', sa.String(), nullable=False),
    sa.Column('role_name', sa.String(), nullable=False),
    sa.Column('pk', sa.Integer(), nullable=False),
    sa.Column('date_updated', sa.DateTime(), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('pk')
    )
    op.create_index(op.f('ix_role_pk'), 'role', ['pk'], unique=False)
    op.create_table('child_assessment_item',
    sa.Column('child_id', sa.Integer(), nullable=True),
    sa.Column('assessment_item_id', sa.Integer(), nullable=True),
    sa.Column('assessor_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['assessment_item_id'], ['assessment_item.pk'], ),
    sa.ForeignKeyConstraint(['assessor_id'], ['assessor.pk'], ),
    sa.ForeignKeyConstraint(['child_id'], ['child.pk'], )
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('child_assessment_item')
    op.drop_index(op.f('ix_role_pk'), table_name='role')
    op.drop_table('role')
    op.drop_index(op.f('ix_domain_pk'), table_name='domain')
    op.drop_table('domain')
    op.drop_index(op.f('ix_child_pk'), table_name='child')
    op.drop_table('child')
    op.drop_index(op.f('ix_assessor_pk'), table_name='assessor')
    op.drop_table('assessor')
    op.drop_index(op.f('ix_assessment_item_pk'), table_name='assessment_item')
    op.drop_table('assessment_item')
    # ### end Alembic commands ###
