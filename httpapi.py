# -*- coding: utf-8 -*-

from flask import Flask
from flask import jsonify, request, make_response
from flask_restful import Resource, Api
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'users_db'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/users_db'
mongo = PyMongo(app)


@app.route('/users/<int:id>', methods=['GET'])
def get(id=None, name=None, surname=None, online=False):
    data = []

    if id:
        user_info = mongo.db.users.find_one({"id": id}, {"_id": 0})
        if user_info:
            return jsonify({"status": "ok", "data": user_info})
        else:
            return make_response(jsonify({'error': 'Not found user with id = {}'.format(id)}), 404)

    elif name:
        cursor = mongo.db.users.find({"name": name}, {"_id": 0}).limit(10)
        for user in cursor:
            data.append({"id": user['id'], "name": user['name'], "surname": user['surname'], "online": user['online']})
        if len(data) > 0:
            return jsonify({"status": "ok", "data": data})
        else:
            return jsonify({"response": "no user found with name {}".format(name)})

    elif surname:
        cursor = mongo.db.users.find({"surname": surname}, {"_id": 0}).limit(10)
        for user in cursor:
            data.append({"id": user['id'], "name": user['name'], "surname": user['surname'], "online": user['online']})
        if len(data) > 0:
            return jsonify({"status": "ok", "data": data})
        else:
            return jsonify({"response": "no user found with name {}".format(name)})

    elif online:
        cursor = mongo.db.users.find({"online": True}, {"_id": 0}).limit(10)
        for user in cursor:
            data.append({"id": user['id'], "name": user['name'], "surname": user['surname'], "online": user['online']})
        if len(data) > 0:
            return jsonify({"status": "ok", "data": data})
        else:
            return jsonify({"response": "no user found online"})











if __name__ == '__main__':
    app.run(debug=True)