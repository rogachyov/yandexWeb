from flask import jsonify
from flask_restful import abort, Resource

from data import db_session, cities
from data.cities import Cities
from data.reqparse import parser


def abort_if_news_not_found(city_id):
    session = db_session.create_session()
    news = session.query(Cities).get(city_id)
    if not news:
        abort(404, message=f"City {city_id} not found")


class CitiesResource(Resource):
    def get(self, id):
        abort_if_news_not_found(id)
        session = db_session.create_session()
        cities = session.query(Cities).get(id)
        return jsonify(cities.to_dict(
            only=('id', 'city')))

    def delete(self, id):
        abort_if_news_not_found(id)
        session = db_session.create_session()
        cities = session.query(Cities).get(id)
        session.delete(cities)
        session.commit()
        return jsonify({'success': 'OK'})


class CitiesListResource(Resource):
    def get(self):
        session = db_session.create_session()
        cities = session.query(Cities).all()
        return jsonify({'cities': [item.to_dict(
            only=('id', 'city')) for item in cities]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        cities = Cities(
            username=args['username'],
            email=args['email']
        )
        cities.set_password(args['password'])
        session.add(cities)
        session.commit()
        return jsonify({'id': cities.id})