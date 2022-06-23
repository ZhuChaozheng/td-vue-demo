# -*- coding: UTF-8 -*-
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from flask_cors import CORS
import json
import flask_sqlalchemy
import pandas as pd



#Create the Flask application and the Flask-SQLAlchemy object.

app = Flask(__name__)
CORS(app, resources=r'/*')
api = Api(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123@172.16.16.6:3306/mysql'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/json/test.db'
db = flask_sqlalchemy.SQLAlchemy(app)

TODOS = {
    "list":[
        {
            "index":1,
            "status":4,
            "no":"BH0038",
            "name":"沧州市办公用品采购项目",
            "paymentType":1,
            "contractType":2
        },
        {
            "index":2,
            "status":4,
            "no":"BH0038",
            "name":"沧州公用品采购项目",
            "paymentType":1,
            "contractType":2
        },
        
        ]
}


# {'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x7ff8ac1d6130>, 
# 'name': 'yes', 'birth_date': datetime.date(2018, 9, 12), 'id': 6}
# CREATE TABLE person (
#     id INTEGER NOT NULL, 
#     name VARCHAR, 
#     birth_date DATE, 
#     PRIMARY KEY (id)
# );
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    birth_date = db.Column(db.Date)

    def json_dict(self):
        return {'id': self.id, 'name': self.name, 
                'birth_date': self.birth_date.strftime('%Y-%m-%d')}


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
    title = db.Column(db.String(50))
    published_at = db.Column(db.DateTime)
    author_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    author = db.relationship(Person, backref=db.backref('articles'))

# # Todo
# #   show a single todo item and lets you delete them
class TodoMore1(Resource):
    def get(self, more):
        list_more = more.split(',')
        # peter = Person.query.filter_by(name='json').first()
        peters = Person.query.filter(Person.name.in_(list_more)).all()

        peter_lists = []
        for peter in peters:
            peter_lists.append(peter.json_dict())
        print(peter_lists)
        df = pd.DataFrame(peter_lists)
        print(df)
        path = "path_to_file.xlsx"
        df.to_excel(path, sheet_name="Sheet1")
        return peter_lists
        # print(peter)
# Todo
#   show a single todo item and lets you delete them
class TodoMore2(Resource):
    def get(self, more):
        print("2: ", type(more))
        return more
        # abort_if_todo_doesnt_exist(todo_id)
        # return TODOS[todo_id]
# Todo
#   show a single todo item and lets you delete them
class TodoMore12(Resource):
    def get(self, more):
        print("12: ", type(more))
        return more
        # abort_if_todo_doesnt_exist(todo_id)
        # return TODOS[todo_id]

# # Todo
# #   show a single todo item and lets you delete them
class Todo(Resource):
    def get(self, todo_id):
        check = todo_id
        peter = Person.query.filter_by(name='json').first()
        return peter.name
        # return TODOS

# TodoList
#   shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):
    def get(self):
        return TODOS

    def post(self):
        args = parser.parse_args()
        todo_id = 'todo%d' % (len(TODOS) + 1)
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201

# Create the database tables.
db.create_all()

##
## Actually setup the Api resource routing here
##
api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/checked/<todo_id>')
api.add_resource(TodoMore1, '/checked_more_1/<string:more>')
api.add_resource(TodoMore2, '/checked_more_2/<string:more>')
api.add_resource(TodoMore12, '/checked_more_12/<string:more>')



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True) 

