"""empty message

Revision ID: 5c33987f21ae
Revises: 8c61c59355ce
Create Date: 2021-12-27 20:50:54.708693

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5c33987f21ae'
down_revision = '8c61c59355ce'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('paragraph',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image_file', sa.Text(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('images')
    op.drop_table('description')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('description',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('description', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('post_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], name='description_post_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='description_pkey')
    )
    op.create_table('images',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('image_file', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('post_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], name='images_post_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='images_pkey')
    )
    op.drop_table('paragraph')
    # ### end Alembic commands ###
