"""Model holding helper functions"""
# third party import
import re
import psycopg2

class Database:
    """Configure a database conncetion"""
    def __init__(self):
        """class constructor"""
        self.role = "postgres"
        self.password = "mufasa"
        self.host = "127.0.0.1"
        self.port = "5432"
        self.database = "storemanager"
    def connection(self):
        """Make a conncetion to storemanager db"""
        try:
            con = psycopg2.connect(
                user=self.role,
                password=self.password,
                host=self.host,
                port=self.port,
                database=self.database
            )
            return con
        except (Exception, psycopg2.DatabaseError) as error:
            print("Database Error", error)

class ProductUtils:
        def __init__(self):
                """class constructor"""
                self.product_details = dict()
        def inspect_product_details(self, product_details):
                """Check product details before adding to inventory"""
                if isinstance(product_details, dict) is False:
                        return "credentials are dictionaries.Try using application/json!"
                self.product_details = product_details
                if not self.product_details:
                        return "Enter data for the server to process!"
                # make sure there are 5 items from server
                if len(self.product_details) != 5:
                        return "Ensure product details include name, category, quantity and unit cost"
                # ensure the 5 items are the ones required to store in db
                options = ["product_name", "product_category", "quantity", "unit_cost"]
                for i in range(len(options)):
                        if options[i] not in self.product_details.keys():
                                return "Ensure to enter {}!".format(options[i])
                # check whether dictionary items are empty strings
                for item in self.product_details:
                        if self.product_details[item] == "" or self.product_details[item] == " ":
                                return "Data fields e.g product name cannot be empty!"
                # check whether product category is sold by the store
                category = ["furniture", "electronics", "sports", "accessories"]
                if self.product_details["product_category"] not in category:
                        return "That product is not sold here!"
                # make sure the store has at least 10 items 
                if product_details["quantity"] < 10:
                        return "Store requires at least 10 items!"
                if isinstance(product_details["quantity"], int) is False:
                        return "Use numbers for quantity!"
                if isinstance(product_details["unit_ccost"], int) is False:
                        return "Use numebers for unit_cost!"
                return "Details are ok!"
        def check_ids(self, productId):
                """check ids"""
                if isinstance(productId, int) is False:
                        return "Make sure productId is a number!"
                elif productId < 1:
                        return "Id 0 doesn't exist!"
                else:
                        return "Id is ok!"
                
