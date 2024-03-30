from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

from data import db_session, news_resources, users_resources, jobs_resource
from data.users import User


app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    # для списка объектов
    api.add_resource(news_resources.NewsListResource, '/api/v2/news')
    api.add_resource(users_resources.UsersListResource, '/api/v2/users')
    api.add_resource(jobs_resource.JobsListResource, '/api/v2/jobs')

    # для одного объекта
    api.add_resource(news_resources.NewsResource, '/api/v2/news/<int:news_id>')
    api.add_resource(users_resources.UsersResource, '/api/v2/users/<int:user_id>')
    api.add_resource(jobs_resource.JobsResource, '/api/v2/jobs/<int:jobs_id>')
    app.run()


if __name__ == '__main__':
    main()