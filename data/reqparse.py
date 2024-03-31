from flask_restful import reqparse


parser = reqparse.RequestParser()
# for user
parser.add_argument('username')
parser.add_argument('password')
parser.add_argument('email')
parser.add_argument('city_id', type=int)

# for city
parser.add_argument('city')
