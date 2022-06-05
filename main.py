from flask import Flask, jsonify, request, redirect, url_for, render_template
import csv
import random

jokes: list[dict[str, str]]


# Jokes sourced and adapted from https://www.hongkiat.com/blog/programming-jokes/
def read_jokes():
    with open("jokes.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)  # read header
        return [{
            "question": q,
            "answer": a
        } for q, a in reader]


app = Flask(__name__)


@app.route('/')
def joke_form():
    return render_template("index.html")


@app.route("/jokes/", methods=["GET", "POST"])
def jokes():
    num: int
    if request.method == "POST":
        num = request.form.get("num", type=int)
    else:
        num = request.args.get("num", type=int)

    num = 1 if num is None else num
    return jsonify(random.sample(jokes, num))


if __name__ == '__main__':
    jokes = read_jokes()
    app.run(host='0.0.0.0', port=5000)
