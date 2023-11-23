"""Contains the Word class."""
from models import Base

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Word(Base):
    """Represents a word."""
    __tablename__ = "words"

    id = Column(Integer, primary_key=True)
    text = Column(String(60), nullable=False)
    difficulty = Column(Integer, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)

    category = relationship('Category', backref='words')

    def __init__(self, text, difficulty):
        """Initializes a category instance.

        Args:
            text: The content of the word.
            difficulty(int): The difficulty level of the word. 1, 2, 3.
        """

        self.__validate_args(text, difficulty)

        self.text = text
        self.difficulty = difficulty

    def __repr__(self):
        """Returns a string representation of the word."""
        return "<Word(txt='{:s}', difficulty={:d})>".format(self.text,
                                                            self.difficulty)

    def __validate_args(self, text, difficulty):
        """Validates __init__ arguments."""

        if type(text) is not str:
            raise TypeError("Word text must be a string")

        if len(text) == 0:
            raise ValueError("Word text cannot be an empty string")

        if type(difficulty) is not int:
            raise TypeError("Word difficulty must be an integer")

        if difficulty not in range(1, 4):
            raise ValueError("Word difficulty must be 1, 2, or 3")
