from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
from models.item import itemModel


class Item(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="this filed cannot be empty"
    )
    @jwt_required()
    def get(self, name):
        item =self.find_by_name(name)
        if item:
            return item.json()
        return {'message':"item not found"},404

    def post(self, name):
        if itemModel.find_by_name(name):
            return{'message':"this item name '{}' already eixsts".format(name)},400

        data=Item.parser.parse_args()
        item = itemModel( name,data['price'])
        try:
            item.save_to_db()
        except:
            return{'message':"An Error happen please try agian later"},500
        return item.json() , 201
    
    

    def delete(self,name):
        #connection = sqlite3.Connection('data.db')
        #curser= connection.cursor()
        #query = "DELETE FROM items WHERE name=?"
        #curser.execute(query,(name,))
        #connection.commit()
        #connection.close()
        #return  {'message':"Item has been deleted"}
        item = itemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return {'message':"item has been deleted"}

    def update(self,name):
        data=Item.parser.parse_args()
        item=itemModel.find_by_name(name)
        #Update_item=itemModel(name,data['price'])
        
        if item is None:
            
            item=itemModel(name,data['price'])
        else:
            item.price=data['price']
        item.save_to_db()
        return item.json()

class ItemList(Resource):
    @jwt_required()
    def get(self):
        #connection = sqlite3.Connection('data.db')
        #curser= connection.cursor()
        #query = "SELECT * FROM items"
        #result=curser.execute(query)
        #items=[]
        ##    items.append({'name':row[0],'price':row[1]})
        #connection.close()

        #return {'items':[item.json()for item in itemModel.query.all()]} #another way by use the lambda
        return {'items':list(map(lambda x: x.json(),itemModel.query.all()))}