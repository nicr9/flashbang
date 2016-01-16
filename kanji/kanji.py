from flask import Flask, render_template, redirect
from os import environ

import csv
import random
import os.path

# Config
DEBUG = True
SPREADSHEET = "https://docs.google.com/spreadsheets/d/1HYaVNzAfFPguuud0abHIcVBvYYc9l5yJ8R7fiukwSu8/pub?gid=1951215858&single=true&output=csv"
KANJI_PATH = os.path.join(os.path.dirname(__file__), 'kanji.csv')

# Create App
app = Flask(__name__)
app.config.from_object(__name__)

@app.route("/")
def homepage():
    with open(KANJI_PATH, 'r') as inp:
        reader = csv.reader(inp, delimiter=',')
        all_kanji = [
                [kanji, pronun, english]
                for kanji, pronun, english in reader
                ]
    return render_template("homepage.html", kanji=random.sample(all_kanji, 4))

@app.route("/reload")
def reload():
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000) # 127.0.0.1:4000
