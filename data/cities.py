import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Cities(SqlAlchemyBase):
    __tablename__ = 'cities'

    id = sqlalchemy.Column(sqlalchemy.Integer, autoincrement=True, nullable=False, primary_key=True)
    city = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    # user = orm.relationship('User')

    def __repr__(self):
        return f'<City> {self.id} {self.city}'
