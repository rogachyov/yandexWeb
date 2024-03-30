from flask_restful import reqparse


parser = reqparse.RequestParser()
# for user
parser.add_argument('name')
parser.add_argument('about')
parser.add_argument('email')

# for city
parser.add_argument('city')
