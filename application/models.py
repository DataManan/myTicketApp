import sqlite3
from sqlalchemy import create_engine, text
from flask_sqlalchemy import SQLAlchemy
from flask import Flask


app = Flask(__name__, template_folder="templates")


