"""Contains the Word model."""
from pydantic import BaseModel
from enum import IntEnum


class DifficultyEnum(IntEnum):
    """Enum for word difficulty."""
    NOVICE = 1
    INTERMEDIEATE = 2
    EXPERT = 3


class Word(BaseModel):
    """Represents a word."""

    word: str
    difficulty: DifficultyEnum
    hint: str

    def to_json(self):
        """Returns the word as a JSON object."""

        return {
            'word': self.word,
            'difficulty': self.difficulty,
            'hint': self.hint
        }
