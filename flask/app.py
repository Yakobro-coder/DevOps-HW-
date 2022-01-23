from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import jsonschema
from jsonschema import validate
import json
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user_flask:112233@127.0.0.1:5432/base_flask?client_encoding=utf8'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Advertisement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    description = db.Column(db.String())
    data_create = db.Column(db.DateTime, default=str(datetime.datetime.utcnow()))
    login = db.Column(db.String)
    email = db.Column(db.String)
    phone = db.Column(db.String)


def get_advertisement():
    advs = Advertisement().query.all()
    data = {}
    for adv in advs:
        data[adv.id] = {
            'login': adv.login,
            'title': adv.title,
            'description': adv.description,
            'data_create': str(adv.data_create),
            'email': adv.email,
            'phone': adv.phone
        }
    return jsonify(data)


def create_adv():
    with open('validate_create_schema.json', 'r') as file:
        schema_valid = json.load(file)

    try:
        validate(instance=request.json, schema=schema_valid)
    except jsonschema.exceptions.ValidationError as err:
        return jsonify({'msg': f'In {err.path[-1]}. {err.message}'})
    data = {**request.json['advertisement'], **request.json['user']}
    adv = Advertisement(**data)
    db.session.add(adv)
    db.session.commit()
    return jsonify({'statusCode': '201'})


@app.route('/adv/<advertisement_id>')
def delete_advertisement(advertisement_id):
    adv = Advertisement.query.filter_by(id=int(advertisement_id))
    if adv.count() == 0:
        return {'msg': 'ad not found', 'statusCode': '404'}

    db.session.delete(adv[0])
    db.session.commit()
    return jsonify({'status': 'OK', 'code': '204'})


app.add_url_rule('/adv', view_func=get_advertisement, methods=['GET'])
app.add_url_rule('/adv/<advertisement_id>/', view_func=delete_advertisement, methods=['DELETE'])
app.add_url_rule('/create', view_func=create_adv, methods=['POST'])
