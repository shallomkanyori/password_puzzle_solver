"""
MongoDB class
"""
from pymongo import MongoClient
from datetime import datetime
import os


class DBStorage():
    """MongoDB class to interact with the database."""

    def __init__(self, db):
        """Connect to MongoDB"""

        self.uri = os.getenv('MONGO_URI', 'mongodb://localhost:27017')
        self.client = MongoClient(self.uri)

        self.db = self.client[db]

    def insert_one(self, coll, data):
        """Inserts a document into a collection.

        Args:
            coll (str): The collection to insert into.
            data (dict): The data of the document to insert.
        """
        # data['created_at'] = datetime.isoformat(datetime.now())
        # data['updated_at'] = datetime.isoformat(datetime.now())
        return self.db[coll].insert_one(data)

    def find(self, coll, _filter={}):
        """Finds all documents in a collection that match a filter.

        Args:
            coll (str): The collection to search.
            _filter (dict): The criteria to match. Optional. Default gets all
                            documents in the collection.
        """
        return self.db[coll].find(_filter)

    def find_one(self, coll, _filter={}):
        """Finds first document in a collection that matches a filter.

        Args:
            coll (str): The collection to search.
            _filter (dict): The criteria to match. Optional. Default finds one
                            random document in a collection.
        """
        return self.db[coll].find_one(_filter)

    def update_one(self, coll, _filter, update):
        """Updates first document in a collection that matches a filter.

        Args:
            coll (str): The collection to search.
            _filter (dict): The criteria to match.
            update (dict): The updates to make to the document.
        """
        # if update.get('$set'):
        #     update['$set']['updated_at'] = datetime.isoformat(datetime.now())

        return self.db[coll].update_one(_filter, update)

    def update_many(self, coll, _filter, update):
        """Updates all documents in a collection that match a filter.

        Args:
            coll (str): The collection to search.
            _filter (dict): The criteria to match.
            update (dict): The updates to make to the documents.
        """
        # if update.get('$set'):
        #     d = datetime.now()
        #     update['$set']['updated_at'] = datetime.isoformat(d)
        return self.db[coll].update_many(_filter, update)

    def delete_one(self, coll, _filter):
        """Deletes first document in a collection that matches a filter.

        Args:
            coll (str): The collection to search.
            _filter (dict): The criteria to match.
        """
        return self.db[coll].delete_one(_filter)

    def delete_many(self, coll, _filter={}):
        """Deletes all documents in a collection that match a filter.

        Args:
            coll (str): The collection to search.
            _filter (dict): The criteria to match. Optional. Default deletes
                            all documents in a collection.
        """
        return self.db[coll].delete_many(_filter)

    def close(self):
        """Close the MongoDB connection."""
        self.client.close()
