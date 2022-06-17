from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def index():
    return 'This is Review API'


if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)
