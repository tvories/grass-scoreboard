#!flask/bin/python
from flask import Flask, jsonify
from random import randint, seed

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

id_value = 3


def set_score(username, score, id_num):
    score = {
        'id': id_num,
        'user': username,
        'score': score
    }
    scores.append(score)


@app.route('/api/v1.0/scores', methods=['GET'])
def get_scores():
    return jsonify({'scores': scores})


@app.route('/')
def index():
    score_rand = randint(1, 10000)
    id_rand = randint(3, 200)
    username = "usernamecool" + str(id_rand)
    set_score(username, score_rand, id_rand)
    return "adding new score"


# @app.route('/api/v1.0/set_score', methods=['POST'], username=username, id=id)
# def set_scores():
#     set_score()


if __name__ == '__main__':
    app.run(debug=True)
    seed(2)



