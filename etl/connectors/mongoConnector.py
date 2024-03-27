from pymongo import MongoClient

class MongoDBConnection:
    def __init__(self, host='localhost', port=27017, username=None, password=None, database=None):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.database_name = database
        self.client = None
        self.db = None
    
    def connect(self):
        """Establish a connection to the MongoDB server."""
        try:
            self.client = MongoClient(self.host, self.port, username=self.username, password=self.password)
            if self.database_name:
                self.db = self.client[self.database_name]
            print("Connected to MongoDB successfully.")
        except Exception as e:
            print("Error connecting to MongoDB:", e)
    
    def disconnect(self):
        """Close the connection to the MongoDB server."""
        try:
            if self.client:
                self.client.close()
                print("Disconnected from MongoDB.")
        except Exception as e:
            print("Error disconnecting from MongoDB:", e)