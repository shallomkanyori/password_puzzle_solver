"""This module reads from a csv file and populates the database."""

from models import storage
from models.word import Word
import csv


def main():
    """Reads from a csv file and populates the database."""
    difficulty = {"Novice": 1,
                  "Intermediate": 2,
                  "Expert": 3
                  }

    with open('words.csv', newline='') as csvfile:
        wordreader = csv.DictReader(csvfile)
        for row in wordreader:
            w = Word(word=row['word'],
                     difficulty=difficulty[row['difficulty']],
                     hint=row['hint'])

            storage.insert_one('words', w.to_json())


if __name__ == "__main__":
    main()
