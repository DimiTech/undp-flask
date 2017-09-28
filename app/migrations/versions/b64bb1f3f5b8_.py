"""empty message

Revision ID: b64bb1f3f5b8
Revises: 765d276b70c9
Create Date: 2017-09-28 15:43:30.228339

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b64bb1f3f5b8'
down_revision = '765d276b70c9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('applications', sa.Column('applicant_website', sa.String(length=2083), nullable=False))
    op.add_column('applications', sa.Column('project_duration_in_months', sa.SmallInteger(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('applications', 'project_duration_in_months')
    op.drop_column('applications', 'applicant_website')
    # ### end Alembic commands ###
