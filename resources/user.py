import sqlite3
from flask_restful import Resource,reqparse
from models.user import UserModel


class UserRegister(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="this filed cannot be empty"
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help="this filed cannot be empty"
    )
    def post(self):
        data=UserRegister.parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {'message':"usename is already exists "},400
        #connection = sqlite3.connect('data.db')
        #curser = connection.cursor()
        #in the param of id bacouse it's auto increment so the value will be null 
        #query="INSERT INTO users VALUES (NULL, ?, ?)"
        #curser.execute(query, (data['username'], data['password']))
        #connection.commit()
        #connection.close()
        user = UserModel(**data)
        user.save_to_db()

        return{"message":"User created"},201