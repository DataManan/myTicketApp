from cgitb import html
from flask import Flask, render_template


app = Flask(__name__)
movies = [
    {
        "poster": "kgf2.jpg",
        "title": "kgf-2",
        "tags": ["action", "drama", "crime"]
    },
    {
        "poster": "pathaan.jpg",
        "title": "Pathaan",
        "tags": ["action", "drama", "crime"]
    },
    {
        "poster": "pushpa.jpg",
        "title": "Pushpa",
        "tags": ["action", "drama", "crime"]
    },
    {
        "poster": "Quantumania.jpg",
        "title": "Quantumania",
        "tags": ["action", "drama", "crime"]
    },
    {
        "poster": "rrr.jpg",
        "title": "RRR",
        "tags": ["action", "drama", "crime"]
    },
    {
        "poster": "wakanda_forever.jpg",
        "title": "Wakanda Forever",
        "tags": ["action", "drama", "crime"]
    },
]


@app.route("/")
def home():
    return render_template("index.html.jinja2", SHOWS=movies)

@app.route("/book_tickets")
def book_tickets():
    return render_template("show.html.jinja2")
if __name__ == "__main__":
    app.run(debug=True)
