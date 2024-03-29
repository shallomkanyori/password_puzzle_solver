#!/usr/bin/python3
"""This module defines a class to manage database storage."""
import models
import os
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


class DBStorage:
    """This class manages db storage of words"""

    __engine = None
    __session = None

    def __init__(self):
        """Initialize DBStorage."""

        usr = os.getenv('PWD_SOLVER_MYSQL_USER', default='')
        pwd = os.getenv('PWD_SOLVER_MYSQL_PWD', default='')
        host = os.getenv('PWD_SOLVER_MYSQL_HOST', default='')
        db = os.getenv('PWD_SOLVER_MYSQL_DB', default='')
        env = os.getenv('PWD_SOLVER_ENV', default='')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                        usr, pwd, host, db))

        if env == 'test':
            models.Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns all records or all records of a given class.

        Args:
            cls: The class to retrieve records of. Optional.
        """

        if cls:
            return self.__session.query(cls).all()
        else:
            res = self.__session.query(models.word.Word).all()
            res.extend(self.__session.query(models.category.Category).all())
            return res

    def get_random_word(self, difficulty):
        """Get a random word of a given difficulty."""

        if difficulty not in range(1, 4):
            return None

        words = (self.__session.query(models.word.Word)
                               .filter_by(difficulty=difficulty)
                               .all())
        word = random.choice(words)
        res = {"word": word.text,
               "difficulty": word.difficulty,
               "category": word.category.name}

        return res

    def get_category_by_name(self, category):
        """Returns the category with the given name. None if not found.

        Args:
            category (str): the name of the category.
        """
        if type(category) is not str:
            raise TypeError("Category name must be a string")

        category = (self.__session.query(models.category.Category)
                                  .filter_by(name=category)
                                  .first())

        return category

    def new(self, obj):
        """Adds new object to current database session"""

        self.__session.add(obj)

    def save(self):
        """Commits all changes of the current database session"""

        self.__session.commit()

    def reload(self):
        """Creates all tables in the database and the current database session.
        """
        models.Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                 expire_on_commit=False))
        self.__session = Session()

    def delete(self, obj=None):
        """Deletes an object from the current database session.

        Args:
            obj: the object to delete. Optional.
        """

        if obj:
            self.__session.delete(obj)

    def close(self):
        """Closes the current database session."""
        self.__session.close()
