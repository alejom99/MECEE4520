import csv
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/movie_ratings")
def movie_ratings():
    data = []
    with open('./movie_ratings.csv', 'r') as fin:
        reader = csv.DictReader(fin)
        for row in reader:
            data.append(row)

    return jsonify(data)