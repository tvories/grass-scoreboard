#!flask/bin/python
from flask import Flask, jsonify

app = Flask(__name__)


scores = [
    {
        'id': 1,
        'user': 'tayloriscool',
        'score': 200001
    },
    {
        'id': 2,
        'user': 'brandumb',
        'score': 4
    }
]


@app.route('/api/v1.0/scores', methods=['GET'])
def get_scores():
    return jsonify({'scores': scores})


if __name__ == '__main__':
    app.run(debug=True)
