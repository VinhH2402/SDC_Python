from flask import Flask, request
from routes.review import *


app = Flask(__name__)


@app.route("/")
def index():
    return 'This is Review API'

@app.route("/reviews", methods=['GET', 'POST'])
def reviews ():
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
