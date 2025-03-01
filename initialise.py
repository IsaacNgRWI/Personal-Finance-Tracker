import pymongo
from pymongo.server_api import ServerApi
from datetime import datetime
import passwords as pw

class User:
    def __init__(self, username=pw.username, password=pw.password):
        self.username = username
        self.password = password
        self.database1 = None
        self.collection1 = None

    def startdb(self, database_name):
        uri = f"mongodb+srv://{self.username}:{self.password}@cluster0.2o89z.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
        # creates a new client and connects it to the server
        client =pymongo.MongoClient(uri, server_api=ServerApi("1"))

        # sends a ping to test connection, returns a message if connection established or the error if not
        try:
            client.admin.command("ping")
            print("MongoDB database successfully connected")
            # creates a database name after database_name inputted
            self.database1 = client[database_name]
            print("----------------------------------------------")
        except Exception as e:
            print(f"An error has occurred: {e}")

    def add_collection(self, collection_name):
        try:
            self.collection1 = self.database1[collection_name]
        except Exception as e:
            print(f"An error has occurred: {e}")

    def add_record_one(self, item_name, item_price, item_cat):
        try:
            self.collection1.insert_one({"Item" : str(item_name), "Price" : float(item_price), "Category" : str(item_cat), "Date" : datetime.now()})
            print(f"{item_name} successfully added at {datetime.now()}")
        except Exception as e:
            print(f"An error has occurred: {e}")

    def return_all(self, amount=None):
        counter = 0
        try:
            if amount > 1:
                print("The number of records requested cannot be less than 1")
            elif amount is None:
                for i in self.collection1.find.sort("Date", -1):
                    counter += 1
                    print(f"Returning all purchases:")
                    print(f"{counter}. {i}")
            else:
                for i in self.collection1.find.sort("Date", -1).limit(int(amount)):
                    counter += 1
                    print(f"Returning {amount} most recent purchases:")
                    print(f"{counter}. {i}")
        except Exception as e:
            print(f"An error has occurred: {e}")
