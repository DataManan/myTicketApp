from cgitb import html
from flask import Flask, render_template


app = Flask(__name__)
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
    return render_template("show.html.jinja2", SHOWS=movies)


if __name__ == "__main__":
    app.run(debug=True)
