from flask import Flask, Response
import json

from pip import main


app = Flask(__name__)

@app.get('/api/v1.0/first')
def first_get():
    return Response(json.dumps({'name': 'Jane', 'age': 24}), 200, content_type='application/json')


if __name__ == '__main__':
    app.run()    