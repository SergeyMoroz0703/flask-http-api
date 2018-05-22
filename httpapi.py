# -*- coding: utf-8 -*-
# GET /createcm?summary=vvv&change=bbb HTTP/1.1

from flask import Flask
from flask import jsonify, request, make_response
from flask_restful import Resource, Api
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'users_db'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/users_db'
mongo = PyMongo(app)


@app.route('/users', methods=['GET'])
def get():
    data = []

    name = request.args.get('name', None)
    surname = request.args.get('surname', None)
    online = request.args.get('online', False)


    if name:
        cursor = mongo.db.users.find({"name": name}).limit(10)
        for user in cursor:
            data.append({"id": str(user['_id']), "name": user['name'], "surname": user['surname'], "online": user['online']})
        if len(data) > 0:
            return jsonify({"status": "ok", "data": data})
        else:
            # return jsonify({"response": "no user found with name {}".format(name)})
            return make_response(jsonify({'error': 'Not found user with name = {}'.format(name)}), 404)

    elif online:
        cursor = mongo.db.users.find({"online": True}).limit(10)
        for user in cursor:
            data.append({"id": str(user['_id']), "name": user['name'], "surname": user['surname'], "online": user['online']})
        if len(data) > 0:
            return jsonify({"status": "ok", "data": data})
        else:
            return jsonify({"response": "no user found online"})

    elif surname:
        cursor = mongo.db.users.find({"surname": surname}).limit(10)
        for user in cursor:
            data.append({"id": str(user['_id']), "name": user['name'], "surname": user['surname'], "online": user['online']})
        if len(data) > 0:
            return jsonify({"status": "ok", "data": data})
        else:
            return jsonify({"response": "no user found with name {}".format(name)})


@app.route('/users', methods=['POST'])
def post():

    user_db = mongo.db.users
    name = request.json['name']
    surname = request.json['surname']
    online = request.json['online']

    users_id = user_db.insert({'name': name, 'surname': surname, 'online': online})
    new_user_id = user_db.find_one({'_id': users_id})

    data = {'id': str(new_user_id['_id']), 'name': new_user_id['name'],
            'surname': new_user_id['surname'], 'online': new_user_id['online']}

    return jsonify({'result': data})


if __name__ == '__main__':
    app.run(debug=True)
