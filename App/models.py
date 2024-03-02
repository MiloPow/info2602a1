from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
db = SQLAlchemy()

class UserPokemon(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, nullable = False)
  user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
  pokemon_id = db.Column(db.Integer, db.ForeignKey("pokemon_id"))

  get_json():
    pass

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(255), nullable = False)
  email = db.Column(db.String(255), nullable = False)
  password = db.Column(db.String(255), nullable = False)
  pokemon = db.relationship(db.Integer, backref="user", lazy=True, cascade="all, delete-orphan")

  catch_pokemon(pokemon_id, name):
    pass
  
  release_pokemon(pokemon_id, name):
    pass
  
  rename_pokemon(pokemon_id, name):
    pass

  set_password(password):
    pass

  check_password(password):
    pass

class Pokemon(db.Model):
  
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), nullable = False)
  attack = db.Column(db.Integer, nullable = False)
  defense = db.Column(db.Integer, nullable = False)
  hp = db.Column(db.Integer, nullable = False)
  height = db.Column(db.Integer, nullable = False)
  sp_attack = db.Column(db.Integer, nullable = False)
  sp_defense = db.Column(db.Integer, nullable = False)
  speed = db.Column(db.Integer, nullable = False)
  type1 = db.Column(db.String(255), nullable = False)
  type2 = db.Column(db.String(255), nullable = False)

  get_json():
    pass
