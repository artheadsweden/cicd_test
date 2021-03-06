"""
The API
"""

import json
from flask import Flask, Response


def create_app():
    """
    Factory function
    :return: app object
    """
    app = Flask(__name__)

    @app.get('/api/v1.0/first')
    def first_get():
        return Response(json.dumps({'name': 'Jane', 'age': 24}),
                        200,
                        content_type='application/json')

    return app

