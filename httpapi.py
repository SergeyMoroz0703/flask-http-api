# -*- coding: utf-8 -*-

from bson import ObjectId
from flask import Flask
from flask import jsonify, request, make_response
from flask_pymongo import PyMongo
import re

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'users_db'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/users_db'
mongo = PyMongo(app)


@app.route('/users', methods=['GET'])
def get():
    data = []
    dict_to_search = {}
    for key, value in request.args.items():
        if key == 'online' and re.match(pattern='^(?i)(true)$', string=value):
            value = True
        elif key == 'online' and re.match(pattern='^(?i)(false)$', string=value):
            value = False
        dict_to_search[key] = value

    if 'id' in dict_to_search:
        cursor = mongo.db.users.find({'_id': ObjectId(dict_to_search['id'])})
        if cursor.count() > 0:
            for user in cursor:
                data.append({'id': str(user['_id']), 'name': user['name'],
                         'surname': user['surname'], 'online': user['online']})
            return jsonify({'status': 'ok', 'data': data})
        else:
            return make_response(jsonify({'error': 'Not found user with {value}'.format(value=dict_to_search)}), 404)

    cursor = mongo.db.users.find(dict_to_search).limit(80)
    if cursor.count() > 0:
        for user in cursor:
            data.append({'id': str(user['_id']), 'name': user['name'],
                         'surname': user['surname'], 'online': user['online']})
        return jsonify({'status': 'ok', 'data': data})
    else:
        return make_response(jsonify({'error': 'Not found user with {value}'.format(value=dict_to_search)}), 404)


@app.route('/users', methods=['POST'])
def post():

    user_db = mongo.db.users
    name = request.json['name']
    surname = request.json['surname']
    online = str(request.json['online'])
    if re.match(pattern='^(?i)(true)$', string=online):
        online = True
    else:
        online = False

    users_id = user_db.insert({'name': name, 'surname': surname, 'online': online})
    new_user_id = user_db.find_one({'_id': users_id})

    data = {'id': str(new_user_id['_id']), 'name': new_user_id['name'],
            'surname': new_user_id['surname'], 'online': new_user_id['online']}

    return make_response(jsonify({'result': data}), 201)


if __name__ == '__main__':
    app.run(debug=True)
