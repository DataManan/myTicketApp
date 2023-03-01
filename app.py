from cgitb import html
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os


current_dir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__, template_folder="templates")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    current_dir, "myticketDB.sqlite3"
)

db = SQLAlchemy()
db.init_app(app)
app.app_context().push()
# app = Flask(__name__)
movies = [
    {
        "show_id": "kgf2021",
        "poster": "kgf2.jpg",
        "title": "kgf-2",
        "tags": ["action", "drama", "crime"]
    },
    {
        "show_id": "pat2023",
        "poster": "pathaan.jpg",
        "title": "Pathaan",
        "tags": ["action", "drama", "crime"]
    },
    {
        "show_id": "pushpa2022",
        "poster": "pushpa.jpg",
        "title": "Pushpa",
        "tags": ["action", "drama", "crime"]
    },
    {
        "show_id": "quantumania2023",
        "poster": "Quantumania.jpg",
        "title": "Quantumania",
        "tags": ["action", "drama", "crime"]
    },
    {
        "show_id": "rrr2022",
        "poster": "rrr.jpg",
        "title": "RRR",
        "tags": ["action", "drama", "crime"]
    },
    {
        "show_id": "wf2023",
        "poster": "wakanda_forever.jpg",
        "title": "Wakanda Forever",
        "tags": ["action", "drama", "crime"]
    }
]


@app.route("/")
def home():
    return render_template("index.html.jinja2", SHOWS=movies)


@app.route("/book_tickets/<show_id>")
def book_tickets(show_id):

    return render_template("show.html.jinja2", SHOWS=movies, show_id=show_id)


if __name__ == "__main__":
    app.run(debug=True)
