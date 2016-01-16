from flask import Flask, render_template, redirect
from redis import Redis
from os import environ

# Config
DEBUG = True
#REDIS_HOST = environ['REDIS_1_PORT_6379_TCP_ADDR']

# Util functions
def get_random_kanji():
    """Returns four random kanji tuples."""
    return [
            ['a', 'b', 'c'],
            ['d', 'e', 'f'],
            ['g', 'h', 'i'],
            ['j', 'k', 'l'],
            ]

# Create App
app = Flask(__name__)
app.config.from_object(__name__)

@app.before_request
def before_request():
    #g.db = Redis(host=app.config['REDIS_HOST'])
    pass

@app.route("/")
def homepage():
    return render_template("homepage.html", kanji=get_random_kanji())

@app.route("/reload")
def reload():
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000) # 127.0.0.1:4000
