import os
import fauna
import fauna.client as fauna_client
import smtplib
import json

class Model():    
    def __init__(self) -> None:
        self.client = fauna_client.Client()# domain="db.eu.fauna.com"    
        self.data = None
        
    def user_data(self, data: dict):
        self.data = data
        query1 = fauna.fql("let customers Customers.create(${data})", data=data)
        result = self.client.query(query1)
        return result
        
    def verification(self, data: dict) -> bool:
        query = fauna.fql("Customers.byMail(${mail}).nonEmpty()", mail=data['mail'])
        result = self.client.query(query)
        return not result.data
    
    def name_verification(self,data: dict)-> bool:
        query = fauna.fql("Customers.byUser(${user}).nonEmpty()", user=data["user"])
        result = self.client.query(query)
        return not result.data
    
    
    def confirmation_login(self,mail: str,user: str) -> bool:
        query = fauna.fql("{uniqueUser: Customers.byUser(${user}).nonEmpty(),uniqueMail: Customers.byUser(${mail}).nonEmpty()}",user = user, mail = mail)
        result = self.client.query(query)
        return not any(result.data.values())
    
    def Order_data(self,data):
        query = fauna.fql("Orders.create(${data})", data=data)
        self.client.query(query)
        
    