import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class City(SqlAlchemyBase):
    __tablename__ = 'cities'

    id = sqlalchemy.Column(sqlalchemy.Integer, autoincrement=True, nullable=False, primary_key=True)
    city = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    lat = sqlalchemy.Column(sqlalchemy.FLOAT, nullable=True)
    lng = sqlalchemy.Column(sqlalchemy.FLOAT, nullable=True)
    # user = orm.relationship('User')

    def __repr__(self):
        return f'<City> {self.id} {self.city}'
