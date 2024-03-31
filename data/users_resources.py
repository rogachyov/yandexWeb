from flask import jsonify
from flask_restful import abort, Resource

from data import db_session, users
from data.users import User
from data.reqparse import parser


def abort_if_user_not_found(users_id):
    session = db_session.create_session()
    news = session.query(User).get(users_id)
    if not news:
        abort(404, message=f"Users {users_id} not found")


class UsersResource(Resource):
    def get(self, id):
        abort_if_user_not_found(id)
        session = db_session.create_session()
        users = session.query(User).get(id)
        return jsonify(users.to_dict(
            only=('id', 'username', 'email')))

    def delete(self, id):
        abort_if_user_not_found(id)
        session = db_session.create_session()
        users = session.query(User).get(id)
        session.delete(users)
        session.commit()
        return jsonify({'success': 'OK'})

    def put(self, id):
        abort_if_user_not_found(id)
        session = db_session.create_session()
        user = session.query(User).get(id)
        args = parser.parse_args()
        if args['username']:
            user.username = args['username']
        if args['email']:
            user.email = args['email']
        if args['password']:
            user.set_password(args['password'])
        if args['city_id']:
            user.city_id = args['city_id']
        session.commit()
        return {'id': user.id, 'username': user.username, 'email': user.email}


class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify({'users': [item.to_dict(
            only=('id', 'username', 'email')) for item in users]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        users = User(
            username=args['username'],
            email=args['email']
        )
        users.set_password(args['password'])
        session.add(users)
        session.commit()
        return jsonify({'id': users.id})