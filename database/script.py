from faunadb import client as faunadb_client
from faunadb.errors import FaunaError
from faunadb import query as q
from faunadb.client import FaunaClient
from faunadb.errors import NotFound
from client import client
import os

token = os.getenv("token")

Client  = FaunaClient(secret=token)
class Model():
    
    def user_data(data):
        result = Client.query(
            q.create(q.collection("users"),{"data":data})
        )
        return result
    
    def product_data(data):
        result = Client.query(
            q.create(q.collection("product"),{"data":data})
        )
        return result
    
    def carte_data(data):
        result = Client.query(
            q.create(q.collection())
        )