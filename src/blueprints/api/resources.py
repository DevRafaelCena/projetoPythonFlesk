from flask import abort, jsonify
from flask_restful import Resource


class TesteResource(Resource):
    def get(self):
        return jsonify(
            {"teste": "API funcionando"}
        )
