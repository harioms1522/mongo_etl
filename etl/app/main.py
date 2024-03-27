from ..connectors.mongoConnector import MongoDBConnection

# Create an instance of MongoDBConnection
mongo_conn = MongoDBConnection(host='143.110.176.233', port=27017, username='anantjain', password='cashluindiassd', database='ecom')


# Connect to MongoDB
mongo_conn.connect()

# Access the database (optional)
db = mongo_conn.db

# Perform operations on the database
# For example:
collection = db['order_infos']
result = collection.find_one()
print("HERER",result)

# Disconnect from MongoDB
# mongo_conn.disconnect()