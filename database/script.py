import os
import fauna
import fauna.client as fauna_client

class Model():    
    def __init__(self) -> None:
        self.client = fauna_client.Client() # domain="db.eu.fauna.com"    
        
    def user_data(self, data: dict):
        query = fauna.fql("users.create(${data})", data=data)
        self.client.query(query)
        # result =self.client.query(
        #     q.create(q.collection("users"),{"data":data})
        # )
    
    def product_data(self,data):
        # result = self.client.query(
        #     q.create(q.collection("product"),{"data":data})
        # )
        pass
        
    def verifiction(self,data):
        query = fauna.fql("true")
        self.client.query(query)