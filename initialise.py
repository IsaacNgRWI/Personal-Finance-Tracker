import pymongo
from pymongo.server_api import ServerApi
import passwords as pw

class Start:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def startdb(self):
        uri = f"mongodb+srv://{self.username}:{self.password}@cluster0.2o89z.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
        # creates a new client and connects it to the server
        client =pymongo.MongoClient(uri, server_api=ServerApi("1"))

        # sends a ping to test connection, returns a message if connection established or the error if not
        try:
            client.admin.command("ping")
            print("MongoDB database successfully connected")
            print("----------------------------------------------")
        except Exception as e:
            print(e)

