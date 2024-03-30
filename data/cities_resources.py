from flask import jsonify
from flask_restful import abort, Resource

from data import db_session
from data.cities import City
from data.reqparse import parser


def abort_if_news_not_found(city_id):
    session = db_session.create_session()
    news = session.query(City).get(city_id)
    if not news:
        abort(404, message=f"City {city_id} not found")


class CitiesResource(Resource):
    def get(self, id):
        abort_if_news_not_found(id)
        session = db_session.create_session()
        cities = session.query(City).get(id)
        return jsonify({'id': cities.id, 'city': cities.city})

    def delete(self, id):
        abort_if_news_not_found(id)
        session = db_session.create_session()
        cities = session.query(City).get(id)
        session.delete(cities)
        session.commit()
        return jsonify({'success': 'OK'})


class CitiesListResource(Resource):
    def get(self):
        session = db_session.create_session()
        cities = session.query(City).all()
        return [{'id': item.id, 'city': item.city} for item in cities]

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        cities = City(
            username=args['username'],
            email=args['email']
        )
        cities.set_password(args['password'])
        session.add(cities)
        session.commit()
        return jsonify({'id': cities.id})