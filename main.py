from flask import Flask, jsonify, request
import csv

all_movies = []
with open("data.csv", encoding='UTF-8') as file:
    reader = csv.reader(file)
    data = list(reader)
    all_movies = data[1:]

liked_movies = []
disliked_movies = []
dnw_movies = []

app = Flask(__name__)

@app.route("/get_movie")
def get_movie():
    return jsonify({
        "data": all_movies[0],
        "status": "success"
    })

@app.route("/liked_movies", methods=["POST"])
def liked_movies():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    liked_movies.append(movie)

    return jsonify({
        "status": "success"
    }), 201

@app.route("/disliked_movies", methods=["POST"])
def disliked_movies():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    disliked_movies.append(movie)

    return jsonify({
        "status": "success"
    }), 201

@app.route("/did_not_watch_movies", methods=["POST"])
def did_not_watch_movies():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    dnw_movies.append(movie)

    return jsonify({
        "status": "success"
    }), 201

if __name__ == "__main__":
    app.run()
