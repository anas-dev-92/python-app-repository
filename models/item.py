from db import db

class itemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80))
    price=db.Column(db.Float(precision=2))
    
    def __init__(self,name,price):
        self.name=name
        self.price=price
    
    def json(self):
        return {'name':self.name,'price':self.price}

    
    @classmethod
    def find_by_name(cls,name):
        #this is how to make it without sqlalchemy
        #connection = sqlite3.Connection('data.db')
        #curser = connection.cursor()
        #query ="SELECT * FROM items WHERE name =?"
        #result = curser.execute(query,(name,))
        #row = result.fetchone()
        #connection.close()
        #if row:
        #    return cls(*row)
        return itemModel.query.filter_by(name=name).first()


    def save_to_db(self):
        #can use for both upadate and insert becouse if we send id sqlAlchemy whill uderstand and retrive and then updated(inserted agian in db)
        #this is how to make it without sqlalchemy
        #connection = sqlite3.Connection('data.db')
        #curser= connection.cursor()
        #query = "INSERT INTO items VALUES (?,?)"
        #curser.execute(query,(self.name,self.price))
        #connection.commit()
        #connection.close()
        db.session.add(self)
        db.session.commit()


    #def update(self):
        #connection = sqlite3.Connection('data.db')
        #curser= connection.cursor()
        #query = "UPDATE items SET price=? WHERE name =?"
        #curser.execute(query,(self.price,self.name))
        #connection.commit()
        #connection.close()
        #return  {'message':'Item has been deleted'}
    def delete_from_db(self):
        db.session.remove(self)
        db.session.commit()