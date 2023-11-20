"""Contains the Category class."""
from models import Base
from sqlalchemy import Column, String, Integer


class Category(Base):
    """Represents a category."""
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String(60), nullable=False)

    def __init__(self, name):
        """Initializes a category instance.

        Args:
            name(str): The name of the category.
        """
        self.__validate_args(name)

        self.name = name

    def __repr__(self):
        """Returns a string representation of the category."""
        return "<Category(name='{:s}')>".format(self.name)

    def __validate_args(self, name):
        """Validates __init__ arguments."""
        if type(name) is not str:
            raise TypeError("Category name must be a string")

        if len(name) == 0:
            raise ValueError("Category name cannot be an emtpy string")
