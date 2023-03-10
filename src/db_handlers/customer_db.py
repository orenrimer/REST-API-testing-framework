import random

from src.utils.dbUtils import DbUtils


class CustomerDB:
    def __init__(self, host, port, db_name):
        self.db = DbUtils(host, port, db_name)
        self.TABLE_NAME = f"{db_name}.wp_users"

    def select_customer_by_email(self, email):
        """
            select a customer from the db using email
        """
        sql = f"SELECT * FROM {self.TABLE_NAME} WHERE user_email = '{email}';"
        response = self.db.select(sql)
        return response

    def select_customer_by_id(self, customer_id):
        """
            select a customer from the db using customer id
        """
        sql = f"SELECT * FROM {self.TABLE_NAME} WHERE ID = '{customer_id}';"
        response = self.db.select(sql)
        return response

    def select_random_customer(self, qty=1, params=None):
        """
            select a random customer from the db (excluding root user)
        """
        sql = f"SELECT * FROM {self.TABLE_NAME} WHERE ID <> 1 {params if params else ''} LIMIT {qty};"

        response = self.db.select(sql)
        return random.sample(response, k=int(qty))
    
    def select_all_customer(self):
        """
            select all customers from the database (excluding root user)
        """
        sql = f"SELECT * FROM {self.TABLE_NAME} WHERE ID <> 1;"

        return self.db.select(sql)
