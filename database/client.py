from faunadb import client as faunadb_client
from faunadb.errors import FaunaError
from faunadb import query as q
from faunadb.client import FaunaClient
from faunadb.errors import NotFound
from dotenv import load_dotenv
import os
load_dotenv()


Token = os.getenv("token")

client = FaunaClient(secret=Token,domain="db.eu.fauna.com")
