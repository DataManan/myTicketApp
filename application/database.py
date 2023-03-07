from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy

engine = None
Base = declarative_base()
db = SQLAlchemy()
# def load_db():
#     db_uri = app.config["DATABASE_URI"]
#     engine = create_engine(db_uri)
#     Session = sessionmaker(bind=engine)
#     session = Session()
#     Base.metadata.create_all(bind=engine)
#     return session
