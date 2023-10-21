import os
import fauna
import fauna.client as fauna_client
import smtplib
import json


from email.message import EmailMessage

class Model():    
    def __init__(self) -> None:
        self.client = fauna_client.Client() # domain="db.eu.fauna.com"    
        
    def user_data(self, data: dict):
        query = fauna.fql("users.create(${data})", data=data)
        self.client.query(query)

    def product_data(self,data: dict):
        # result = self.client.query(
        #     q.create(q.collection("product"),{"data":data})
        # )
        pass
        
    def verification(self, data: dict) -> bool:
        query = fauna.fql("users.byMail(${mail}).nonEmpty()", mail=data['mail'])
        result = self.client.query(query)
        return not result.data
    
    def name_verification(self,data: dict)-> bool:
        query = fauna.fql("users.byUser(${user}).nonEmpty()", user=data["user"])
        result = self.client.query(query)
        return not result.data
    
    
    def confirmation_login(self,mail: str,user: str) -> bool:
        query = fauna.fql("{uniqueUser: users.byUser(${user}).nonEmpty(),uniqueMail: users.byUser(${mail}).nonEmpty()}",user = user, mail = mail)
        result = self.client.query(query)
        return not any(result.data.values())
    
        