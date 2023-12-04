"""This module reads from a csv file and populates the database."""

from models import storage
from models.category import Category
from models.word import Word
import csv


def main():
    """Reads from a csv file and populates the database."""
    difficulty = {"Easy": 1,
                  "Medium": 2,
                  "Hard": 3
                  }

    with open('words.csv', newline='') as csvfile:
        wordreader = csv.DictReader(csvfile)
        for row in wordreader:
            category = storage.get_category_by_name(row["Category"])

            if not category:
                category = Category(row["Category"])
                storage.new(category)

            category.words.append(Word(row["Word"], difficulty[row["Difficulty"]]))

        storage.save()


if __name__ == "__main__":
    main()
