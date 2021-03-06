
from sqlalchemy import Column, String, create_engine,Integer
from flask_sqlalchemy import SQLAlchemy
import json
import os

database_path = os.environ['DATABASE_URL']
database_name = "agency1"
#database_path = "postgres://{}/{}".format('localhost:5432', database_name)



db = SQLAlchemy()


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


class Movies(db.Model):  
  __tablename__ = 'movies'

  id = Column(Integer, primary_key=True)
  title = Column(String)
  release_date= Column(String)

  def __init__(self, title, release_date):
    self.title = title
    self.release_date = release_date

  def format(self):
    return {
      'id': self.id,
      'title': self.title,
      'release_date': self.release_date }

  def insert(self):
      db.session.add(self)
      db.session.commit()

  def delete(self):
      db.session.delete(self)
      db.session.commit()

  def update(self):
      db.session.commit()




class Actor(db.Model):  
  __tablename__ = 'actors'

  id = Column( Integer, primary_key=True)
  name = Column(String)
  age= Column(String)
  gender=Column(String)

  def __init__(self, name, age,gender):
    self.name = name
    self.age = age
    self.gender = gender

  def format(self):
    return {
      'id': self.id,
      'name': self.name,
      'age': self.age,
      'gender': self.gender  }

  def insert(self):
      db.session.add(self)
      db.session.commit()

  def delete(self):
      db.session.delete(self)
      db.session.commit()

  def update(self):
      db.session.commit()
  
      
