import os
import fauna
import fauna.client as fauna_client
import secrets
import json
from uuid import uuid4


class Model():
        
    def __init__(self) -> None:
        self.client = fauna_client.Client()# domain="db.eu.fauna.com"    
    
    def create_uuid4():
        return str(uuid4())
    
    def user_data(self, data: dict ) -> None:
        uiuid = str(uuid4())
        customer_id = {"customers_id":uiuid}
        data.update(customer_id)
        query1 = fauna.fql("Customers.create(${data})", data=data)
        self.client.query(query1)
    
    def verification(self, data: dict) -> bool:
        query = fauna.fql("Customers.byMail(${mail}).nonEmpty()", mail=data['mail'])
        result = self.client.query(query)
        return not result.data
    
    def name_verification(self, data: dict)-> bool:
        query = fauna.fql("Customers.byUser(${user}).nonEmpty()", user=data["user"])
        result = self.client.query(query)
        return not result.data
    
    
    def confirmation_login(self, mail: str, user: str) -> bool:
        query = fauna.fql("\
            {uniqueUser: Customers.byUser(${user}).nonEmpty(),uniqueMail: Customers.byUser(${mail}).nonEmpty()}", user=user, mail = mail)
        result = self.client.query(query)
        return not any(result.data.values())
    
    def order_data(self, data: dict) -> None:
        query = fauna.fql("Orders.create(${data})", data=data)
        self.client.query(query)
        
    def session_create(self, data: dict):
        query = fauna.fql("Session.create(${data})", data=data)
        result = self.client.query(query)
        return result.data["token"]
    
    def get_id_by_username(self, username) -> str:
        query = fauna.fql("Customers.byUser(${username}).first()", username=username)
        result = self.client.query(query)
        return result.data["customers_id"]
    
    def get_id_by_token(self, token) -> str:
        query = fauna.fql("Session.byToken(${token}).first()", token=token)
        result = self.client.query(query)
        return result.data["customers_id"]
    
    def get_customers_bycustomers_id(self, customers_id) -> dict:
        query = fauna.fql("Customers.byCustomers_id(${customers_id}).first()", customers_id=customers_id)
        result = self.client.query(query)
        result2 = {
            "user":str(result.data["user"]),
            "mail":str(result.data["mail"])
        }
        return result2
    
    def get_order_by_customers_id(self, customers_id) -> dict:
        bucket = {}
        query = fauna.fql("Orders.byCustomers_id(${customers_id}).order(){name,os,price,quantity,img}", customers_id=customers_id)
        result = self.client.query(query)
        for i in result.data:
            bucket.update(i)

        return bucket
    
    """def verification_quantity(self, customers_id):
        query = fauna.fql("Orders.byCustomers_id({customers_id}).map(.quantity).last()", customers_id=customers_id)
        
        return quantity"""
    
    
    """def get_user_id(self):
        query = fauna.fql("Customers.", token=token)
        result = self.client.query(query)
        return result.data["customers_id"]"""
    
