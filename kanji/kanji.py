from flask import Flask, render_template, redirect
from os import environ

import csv
import random
import os.path

# Config
DEBUG = True
SPREADSHEET = "https://docs.google.com/spreadsheets/d/1HYaVNzAfFPguuud0abHIcVBvYYc9l5yJ8R7fiukwSu8/pub?gid=1951215858&single=true&output=csv"

# Paths
CSV = os.path.dirname(__file__)

# Create App
app = Flask(__name__)
app.config.from_object(__name__)

@app.route("/")
def homepage():
    """
    Displays a list of spreadsheets that are on offer as flash cards.
    """
    # Open csv file and create a reader
    csv_path = os.path.join(CSV, 'spreadsheets.csv')
    with open(csv_path, 'r', encoding="utf8") as inp:
        reader = csv.reader(inp, delimiter=',')

        # Sort rows in file
        # [('name': 'flash_cards/name'), ...]
        rows = [
                (name, "flash_cards/{}".format(name))
                for name in reader
                ]
    return render_template("homepage.html", rows=rows)

@app.route("/flash_cards/<spreadsheet>")
def flash_cards(spreadsheet):
    """
    Reads contents of a spreadsheet from cache on disk to populate a table.
    """
    # Open csv file and create a reader
    csv_path = os.path.join(CSV, spreadsheet + ".csv")
    with open(csv_path, 'r', encoding="utf8") as inp:
        reader = csv.reader(inp, delimiter=',')

        # Read all rows of the csv file
        rows = [row for row in reader]

    return render_template("flash_cards.html", title=spreadsheet, rows=random.sample(rows, 4))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000) # 127.0.0.1:4000
