#!flask/bin/python
from flask import Flask, request, jsonify
from random import randint, seed
import json
import copy

app = Flask(__name__)

scores = [
    {
        'id': 2,
        'user': 'KingMowerB',
        'score': 2
    },
    {
        'id': 1,
        'user': 'taylorMowedOneGrass',
        'score': 1
    },
    {
        'id': 3,
        'user': 'randomPerson',
        'score': 3
    }
    {
        'id': 5,
        'user': 'Madness',
        'score': 120
    },
]

scores_ranked = []
id_value = 3

@app.route('/api/v1.0/recive_score_data', methods=['POST'])
def recive_score_data():
    try:
        receved_data = json.loads(list(request.form.to_dict().keys())[0])
        set_score(receved_data["user"], receved_data["score"], receved_data["id"])
        #rank_scores()
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"


def set_score(username, score, id_num):
    score = {
        'id': id_num,
        'user': username,
        'score': score
    }
    scores.append(score)


def rank_scores():
    _scores_ranked = []
    temp_list = copy.copy(scores)
    catcher = 100000
    x = 0
    while(temp_list):
        x += 1
        if(x >= catcher):
            print('catched!')
            return
        highest = 0
        indexSave = 0
        i = 0
        for score in temp_list:
            if(score['score'] > highest):
                highest = score['score']
                indexSave = i
            i += 1
        _scores_ranked.append(temp_list[indexSave])
        temp_list.pop(indexSave)
    return _scores_ranked

@app.route('/api/v1.0/scores', methods=['GET'])
def get_scores():
    scores_ranked = rank_scores()
    return jsonify({'scores': scores_ranked})
    #return jsonify({'scores': scores})


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
    #seed(2)
    #rank_scores()



