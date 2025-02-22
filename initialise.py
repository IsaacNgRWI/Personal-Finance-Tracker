import pymongo
from pymongo.server_api import ServerApi
import password as pw

class StartDb:
    def __init__(self, username, password):
        self.username = username
        self.password = password