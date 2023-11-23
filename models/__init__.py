"""Declares and initializes the Base variable."""
from sqlalchemy.ext.declarative import declarative_base
from models.engine.db_storage import DBStorage

Base = declarative_base()

from models.category import Category
from models.word import Word

storage = DBStorage()
storage.reload()
