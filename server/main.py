#!/usr/local/bin/python3
import collections
import collections.abc
collections.Iterable = collections.abc.Iterable

from flask import Flask, abort, jsonify, request
from flask_cors import CORS, cross_origin

from run_generation import generate_text

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/generate", methods=['POST'])
@cross_origin()
def get_generation():
    data = request.get_json()
    print(data)

    if 'text' not in data or len(data['text']) == 0 or 'model' not in data:
        abort(400)
    else:
        text = data['text']
        model = data['model']

    result = generate_text(
        model_type='gpt2',
        length=100,
        prompt=text,
        model_name_or_path=model
    )
    print(result)

    return jsonify({'result': result})

if __name__=='__main__':
    app.run(host='127.0.0.1', port=5000)