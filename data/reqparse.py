from flask_restful import reqparse


parser = reqparse.RequestParser()
parser.add_argument('title')
parser.add_argument('content')
parser.add_argument('is_private', type=bool)
parser.add_argument('is_published', type=bool)
parser.add_argument('user_id', type=int)

parser.add_argument('name')
parser.add_argument('about')
parser.add_argument('email')

parser.add_argument('team_leader', type=int)
parser.add_argument('job')
parser.add_argument('work_size', type=int)
parser.add_argument('collaborators')
parser.add_argument('is_finished', type=bool)