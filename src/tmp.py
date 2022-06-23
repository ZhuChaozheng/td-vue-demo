# -*- coding: UTF-8 -*-
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from flask_cors import CORS

import flask
import flask_sqlalchemy

# app = Flask(__name__)
# CORS(app, resources=r'/*')
# api = Api(app)

# TODOS = {
#     'todo1': {'task': 'build an API'},
#     'todo2': {'task': '?????'},
#     'todo3': {'task': 'profit!'},
#     "list":[
#         {
#             "index":1,
#             "status":4,
#             "no":"BH0038",
#             "name":"沧州市办公用品采购项目",
#             "paymentType":1,
#             "contractType":2,
#             "updateTime":"2020-05-30 14:05:44",
#             "amount":"170,000,000",
#             "adminName":"顾娟"
#         },
#         {
#             "index":2,
#             "status":2,
#             "no":"BH0081",
#             "name":"红河哈尼族彝族采购项目",
#             "paymentType":0,
#             "contractType":0,
#             "updateTime":"2020-05-30 22:59:10",
#             "amount":"267,000,000",
#             "adminName":"薛强"
#         },
#         {
#             "index":3,
#             "status":1,
#             "no":"BH0022",
#             "name":"铜川市办公用品采购项目",
#             "paymentType":1,
#             "contractType":1,
#             "updateTime":"2020-05-30 06:29:24",
#             "amount":"380,000,000",
#             "adminName":"陈平"
#         },
#         {
#             "index":4,
#             "status":4,
#             "no":"BH0038",
#             "name":"沧州市办公用品采购项目",
#             "paymentType":1,
#             "contractType":2,
#             "updateTime":"2020-05-30 14:05:44",
#             "amount":"170,000,000",
#             "adminName":"顾娟"
#         },
#         {
#             "index":5,
#             "status":2,
#             "no":"BH0081",
#             "name":"红河哈尼族彝族购项目",
#             "paymentType":0,
#             "contractType":0,
#             "updateTime":"2020-05-30 22:59:10",
#             "amount":"267,000,000",
#             "adminName":"薛强"
#         },
#         {
#             "index":6,
#             "status":1,
#             "no":"BH0022",
#             "name":"铜川市办公用品采购项目",
#             "paymentType":1,
#             "contractType":1,
#             "updateTime":"2020-05-30 06:29:24",
#             "amount":"380,000,000",
#             "adminName":"陈平"
#         },
#         {
#             "index":7,
#             "status":4,
#             "no":"BH0038",
#             "name":"沧州市办公用品采购项目",
#             "paymentType":1,
#             "contractType":2,
#             "updateTime":"2020-05-30 14:05:44",
#             "amount":"170,000,000",
#             "adminName":"顾娟"
#         },
#         {
#             "index":8,
#             "status":2,
#             "no":"BH0081",
#             "name":"红河哈尼族彝族目",
#             "paymentType":0,
#             "contractType":0,
#             "updateTime":"2020-05-30 22:59:10",
#             "amount":"267,000,000",
#             "adminName":"薛强"
#         }
#         ]
# }

# check = '66'

# def abort_if_todo_doesnt_exist(todo_id):
#     if todo_id not in TODOS:
#         abort(404, message="Todo {} doesn't exist".format(todo_id))

# parser = reqparse.RequestParser()
# parser.add_argument('task')

# # Todo
# #   show a single todo item and lets you delete them
# class TodoMore1(Resource):
#     def get(self, more):
#         print(more)
#         return more
#         # abort_if_todo_doesnt_exist(todo_id)
#         # return TODOS[todo_id]
# # Todo
# #   show a single todo item and lets you delete them
# class TodoMore2(Resource):
#     def get(self, more):
#         print(more)
#         return more
#         # abort_if_todo_doesnt_exist(todo_id)
#         # return TODOS[todo_id]
# # Todo
# #   show a single todo item and lets you delete them
# class TodoMore12(Resource):
#     def get(self, more):
#         print(more)
#         return more
#         # abort_if_todo_doesnt_exist(todo_id)
#         # return TODOS[todo_id]

# # Todo
# #   show a single todo item and lets you delete them
# class Todo(Resource):
#     def get(self, todo_id):
#         check = todo_id
#         return check
#         # abort_if_todo_doesnt_exist(todo_id)
#         # return TODOS[todo_id]

#     def delete(self, todo_id):
#         abort_if_todo_doesnt_exist(todo_id)
#         del TODOS[todo_id]
#         return '', 204

#     def put(self, todo_id):
#         args = parser.parse_args()
#         task = {'task': args['task']}
#         TODOS[todo_id] = task
#         return task, 201


# # TodoList
# #   shows a list of all todos, and lets you POST to add new tasks
# class TodoList(Resource):
#     def get(self):
#         return TODOS

#     def post(self):
#         args = parser.parse_args()
#         todo_id = 'todo%d' % (len(TODOS) + 1)
#         TODOS[todo_id] = {'task': args['task']}
#         return TODOS[todo_id], 201

# ##
# ## Actually setup the Api resource routing here
# ##
# api.add_resource(TodoList, '/todos')
# api.add_resource(Todo, '/checked/<todo_id>')
# api.add_resource(TodoMore1, '/checked_more_1/<string:more>')
# api.add_resource(TodoMore2, '/checked_more_2/<string:more>')
# api.add_resource(TodoMore12, '/checked_more_12/<string:more>')



# if __name__ == '__main__':
#     app.run(host='0.0.0.0', debug=True) 

# Create the Flask application and the Flask-SQLAlchemy object.
app = flask.Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = flask_sqlalchemy.SQLAlchemy(app)

# CREATE TABLE person (
#     id INTEGER NOT NULL, 
#     name VARCHAR, 
#     birth_date DATE, 
#     PRIMARY KEY (id)
# );
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode)
    birth_date = db.Column(db.Date)

# CREATE TABLE article (
#     id INTEGER NOT NULL, 
#     title VARCHAR, 
#     published_at DATETIME, 
#     author_id INTEGER, 
#     PRIMARY KEY (id), 
#     FOREIGN KEY(author_id) REFERENCES person (id)
# );
class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Unicode)
    published_at = db.Column(db.DateTime)
    author_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    author = db.relationship(Person, backref=db.backref('articles'))


# Create the database tables.
db.create_all()
