import sqlite3
from db import db

class UserModel(db.Model):
    __tablename__ = 'users'

    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(80))
    password=db.Column(db.String(80))



    def __init__(self,username,password):
        self.username=username
        self.password=password
    

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls,username):
        #connection= sqlite3.Connection('data.db')
        #cruser=connection.cursor()
        #query = "SELECT * FROM users WHERE username=?"
        #result=cruser.execute(query,(username,))
        #row = result.fetchone()
        #if row :
        #    #first way of get the result
        #    #we can use this one to fetch the data like in param id,username,password,
        #    #user=cls(row[0],row[1],row[2])
        #    #second
        #    #user=cls(*row)
        #else:
        #    user=None
        
        #connection.close()
        #return user
        return cls.query.filter_by(username=username).first()


    @classmethod
    def find_by_Id(cls,_id):
        #connection= sqlite3.Connection('data.db')
        #cruser=connection.cursor()
        #query = "SELECT * FROM users WHERE id=?"
        #result=cruser.execute(query,(_id,))
        #row = result.fetchone()
        ##    #first way of get the result
        #    #we can use this one to fetch the data like in param id,username,password,
        ##    #user=cls(row0,row1,row2)
        #    #second
        #    user=cls(*row)
        #else:
        #    user=None
        
        #connection.close()
        #return user
        return cls.query.filter_by(id=_id).first()