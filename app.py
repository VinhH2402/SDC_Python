from flask import Flask, request
from flask_caching import Cache
from routes.review import *
from flask_mysqldb import MySQL

app = Flask(__name__)

#cache
cache = Cache(config={"DEBUG": True,
                      "CACHE_TYPE": "SimpleCache",
                      "CACHE_DEFAULT_TIMEOUT": 300})
cache.init_app(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'reviewAPI'

mysql = MySQL(app)


@app.route("/")
def index():
    return 'This is Review API'


@app.route("/reviews", methods=['GET', 'POST'])
@cache.cached(timeout=50, query_string=True)
def reviews():
    return getReviews(request)


@app.route("/reviews/meta", methods=['GET'])
def get_meta():
    return 'get meta'


@app.route("/reviews/<review_id>/helpful", methods=['PUT'])
def helpful(review_id):
    return review_id + ' helpfull'


@app.route("/reviews/<review_id>/report", methods=['PUT'])
def report(review_id):
    return review_id + ' helpfull'


if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)
