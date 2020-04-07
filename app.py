#!flask/bin/python
from flask import Flask, request, jsonify
from random import randint, seed
import json
import copy
from faker import Faker

app = Flask(__name__)
fake = Faker('en-US')

scores = [
    {
        'id': 2,
        'user': 'KingMowerB',
        'score': 2,
        'MACId': "ComputerName"
    }
]

scores_ranked = []
id_value = 3
NUM_GENERATED_SCORES = 15


def score_generator():
    for i in range(0, NUM_GENERATED_SCORES):
        temp_id = randint(id_value, 100)
        temp_user = fake.name()
        temp_score = randint(1,100000)
        temp_mac = "00:00:00:00:00"
        score = {
            'id': temp_id,
            'user': temp_user,
            'score': temp_score,
            'MACId': temp_mac
        }
        scores.append(score)


def unique_user_check(new_entry):
    score_updated = False
    user_check = new_entry["MACId"]
    for score in scores:
        if(user_check == score['MACId']):
            score['user'] = new_entry['user']
            score['score'] = new_entry['score']
            score_updated = True
    return score_updated


@app.route('/api/v1.0/recive_score_data', methods=['POST'])
def recive_score_data():
    try:
        receved_data = json.loads(list(request.form.to_dict().keys())[0])
        score_updated = unique_user_check(receved_data)
        if(score_updated == False):
            set_score(receved_data["user"], receved_data["score"], receved_data["id"],receved_data["MACId"])
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"


def set_score(username, score, id_num, _MACId):
    score = {
        'id': id_num,
        'user': username,
        'score': score,
        'MACId': _MACId
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
    print(scores_ranked)
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
    score_generator()
    app.run(debug=True)

    #seed(2)
    #rank_scores()



