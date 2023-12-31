"""empty message

Revision ID: c9130b56e4f9
Revises: 
Create Date: 2023-12-03 21:46:30.736926

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c9130b56e4f9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blocklists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('expired', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('book_name', sa.String(length=80), nullable=False),
    sa.Column('thumb', sa.Integer(), nullable=False),
    sa.Column('tag', sa.String(length=80), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('book_name')
    )
    op.create_table('pages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('page_number', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(), nullable=False),
    sa.Column('image_url', sa.String(), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['book_id'], ['books.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pages')
    op.drop_table('books')
    op.drop_table('users')
    op.drop_table('blocklists')
    # ### end Alembic commands ###
