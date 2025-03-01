import pymongo
from pymongo.server_api import ServerApi
import passwords as pw

class User:
    def __init__(self, username=pw.username, password=pw.password):
        self.username = username
        self.password = password

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
            print(e)

    def add_collection(self, collection_name):
        try:
            self.collection1 = self.database1[collection_name]
        except Exception as e:
            print(e)

    def add_record_one(self, item_name, item_price, item_cat):
        try:
            self.collection1.insert_one({"Item" : item_name, "Price" : item_price, "Category" : item_cat})
            print(f"{item_name} successfully added.")
        except Exception as e:
            print(e)