"""empty message

Revision ID: 8d870bdeae05
Revises: d6808924af12
Create Date: 2022-01-09 22:46:53.000911

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d870bdeae05'
down_revision = 'd6808924af12'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('newsletter',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('emal', sa.Text(), nullable=True),
    sa.Column('date', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.alter_column('blog', 'author',
               existing_type=sa.INTEGER(),
               nullable='True')
    op.alter_column('comment', 'author',
               existing_type=sa.INTEGER(),
               nullable='True')
    op.alter_column('comment', 'post_id',
               existing_type=sa.INTEGER(),
               nullable='True')
    op.alter_column('comment', 'blog_id',
               existing_type=sa.INTEGER(),
               nullable='True')
    op.alter_column('post', 'author',
               existing_type=sa.INTEGER(),
               nullable='True')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('post', 'author',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('comment', 'blog_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('comment', 'post_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('comment', 'author',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('blog', 'author',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_table('newsletter')
    # ### end Alembic commands ###