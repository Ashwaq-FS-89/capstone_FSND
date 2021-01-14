import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db , Actor , Movies
import json
from auth.auth import AuthError, requires_auth

def create_app(test_config=None):

  app = Flask(__name__)
  setup_db(app)

  CORS(app, resources={r"/*": {"origins": "*"}})
  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods','GET,PUT,POST,DELETE,OPTIONS')
    return response


  @app.route('/actors')
  @requires_auth('get:actor')
  def get_actors(token):
    actors=Actor.query.all()

    return jsonify({
      'actors':[actor.format() for actor in actors],
      'success':True
    })

  @app.route('/actors/<int:id>' , methods=['DELETE'])
  @requires_auth('delete:actor')
  def delete_actors(token,id):
    actor= Actor.query.filter(Actor.id==id).one_or_none()
    if actor is None:
      abort(404)
    actor.delete()

    return jsonify({
      'actor deleted': id ,
      'success':True
    })

  @app.route('/actors/<int:id>' , methods=['PATCH'])
  @requires_auth('patch:actor')
  def update_actors(token,id):
    data=request.get_json()
    actor= Actor.query.filter(Actor.id==id).one_or_none()
    if actor is None:
      abort(404)

    actor.name = data ['name']
    actor.age = data ['age']
    actor.gender = data ['gender']

    actor.update()

    return jsonify({
      'actor ': actor.format() ,
      'success':True
    })
  @app.route('/actors' , methods=['POST'])
  @requires_auth('post:actor')
  def post_actor(token):
    data=request.get_json()
    new_actor= Actor(
      name = data ['name'],
      age = data ['age'],
      gender = data ['gender'])

    new_actor.insert()

    return jsonify({
      'actor ': new_actor.format() ,
      'success':True
     })

  @app.route('/movies')
  @requires_auth('get:movie')
  def get_movies(token):
    movies=Movies.query.all()

    return jsonify({
      'movies':[movie.format() for movie in movies],
      'success':True
    })

  @app.route('/movies/<int:id>' , methods=['DELETE'])
  @requires_auth('delete:movie')
  def delete_movies(token,id):
    movie=Movies.query.filter(Movies.id==id).one_or_none()
    if movie is None:
      abort(404)
    movie.delete()

    return jsonify({
      'movie deleted': id ,
      'success':True
    })

  @app.route('/movies/<int:id>' , methods=['PATCH'])
  @requires_auth('patch:movie')
  def update_movies(token,id):
    data=request.get_json()
    movie=Movies.query.filter(Movies.id==id).one_or_none()
    if movie is None:
      abort(404)

    movie.title = data ['title']
    movie.release_date = data ['release_date']

    movie.update()

    return jsonify({
      'movie ': movie.format() ,
      'success':True
    })

  @app.route('/movies' , methods=['POST'])
  @requires_auth('post:movie')
  def post_movie(token):
    data=request.get_json()
    new_movie=Movies(
      title = data ['title'],
      release_date = data ['release_date']
     )
    new_movie.insert()
  
    return jsonify({
      'movie ': new_movie.format() ,
      'success':True
    })
  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
        "success": False, 
        "error": 404,
        "message": "Resource Not found"
        }), 404

  @app.errorhandler(405)
  def not_found(error):
    return jsonify({
        "success": False, 
        "error": 405,
        "message": "Method Not Allowed"
        }), 405

  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
      "success": False, 
      "error": 422,
      "message": "unprocessable"
      }), 422

  @app.errorhandler(400)
  def bad_request(error):
    return jsonify({
        "success": False, 
        "error": 400,
        "message": "Bad Request"
        }), 400
      
  @app.errorhandler(500)
  def internal_server_error(error):
    return jsonify({
        "success": False, 
        "error": 500,
        "message": " Internal Server Error"
        }), 500
  @app.errorhandler(AuthError)
  def handle_auth_error(error):
    return jsonify({
        "success": False, 
        "message":error.error,
        "code":error.status_code
        }),error.status_code
  return app

app = create_app()

if __name__ == '__main__':
    app.run()