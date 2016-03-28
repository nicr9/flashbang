from flask import Flask, render_template, redirect, request
from os import environ

import urllib
import re
import csv
import random
import os.path

# Config
DEBUG = False
SPREADSHEET = "https://docs.google.com/spreadsheets/d/1HYaVNzAfFPguuud0abHIcVBvYYc9l5yJ8R7fiukwSu8/pub?gid=1951215858&single=true&output=csv"

# Paths
CSV = os.path.join(os.path.dirname(__file__), "data")

# Create App
app = Flask(__name__)
app.config.from_object(__name__)

def key(name):
    underscores  = re.sub(" ", '_', name)
    alphabets = re.sub("[^\w_]", '', underscores)
    return alphabets.lower()

def get_csv_path(key):
    return os.path.join(CSV, key + '.csv')

@app.route("/")
def homepage():
    """
    Displays a list of spreadsheets that are on offer as flash cards.
    """
    # Open csv file and create a reader
    csv_path = get_csv_path("spreadsheets")
    with open(csv_path, 'r', encoding="utf8") as inp:
        reader = csv.reader(inp, delimiter=',')

        # Sort rows in file
        # [('name': 'flash_cards/name'), ...]
        rows = [
                (name, "flash_cards/{}".format(name))
                for (name, _) in reader
                ]
    return render_template("homepage.html", spreadsheets=rows)

@app.route("/create", methods=['POST', 'GET'])
def create():
    error = None
    if request.method == 'POST':
        name = key(request.form['name'])
        url = request.form['url']

        # Update spreadsheets.csv
        csv_path = get_csv_path("spreadsheets")
        with open(csv_path, 'a', encoding="utf8") as outp:
            writer = csv.writer(outp, delimiter=',')
            writer.writerow([name, url])

        # Create <name>.csv
        csv_path = get_csv_path(name)
        with open(csv_path, 'wb') as outp:
            response = urllib.request.urlopen(url)
            outp.write(response.read())

        return flash_cards(name)

    return render_template('homepage.html', error=error)

@app.route("/meta/<page>")
def meta(page):
    return render_template("{}.html".format(page))

@app.route("/flash_cards/<spreadsheet>")
def flash_cards(spreadsheet):
    """
    Reads contents of a spreadsheet from cache on disk to populate a table.
    """
    # Open csv file and create a reader
    csv_path = get_csv_path(spreadsheet)
    with open(csv_path, 'r', encoding="utf8") as inp:
        reader = csv.reader(inp, delimiter=',')

        # Read all rows of the csv file
        header = next(reader)
        rows = [row for row in reader]

    return render_template(
            "flash_cards.html",
            title=spreadsheet,
            header=header,
            rows=random.sample(rows, 4)
            )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000) # 127.0.0.1:4000
