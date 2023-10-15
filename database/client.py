import os
from faunadb.client import FaunaClient
from faunadb.errors import FaunaError
from faunadb import query as q
from faunadb.client import FaunaClient
from faunadb.errors import NotFound

token = os.getenv("token")
from faunadb import query as q
from faunadb.objects import Ref
from faunadb.client import FaunaClient

# Initialize the FaunaDB client
client = FaunaClient(secret=token)

# Define the collection name
collection_name = "my_collection"

# Create a collection
collection_ref = client.query(q.create_collection({"name": collection_name}))

# Print the reference to the created collection
print("Collection created: {}".format(collection_ref))