from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticated,identity
from resources.user import UserRegister
from resources.item import Item,ItemList

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'#how to tell the alchemy about the data file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key='hello for the other side'
api=Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt=JWT(app,authenticated,identity)

api.add_resource(ItemList, '/items')

api.add_resource(Item, '/item/<string:name>')

api.add_resource(UserRegister,'/register')
if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)