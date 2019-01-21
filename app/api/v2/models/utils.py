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


class UserUtils:
    """A class holding helper functions"""
    def __init__(self):
        """class constructor"""
        self.user_credentials = dict()
    def inspect_user_credentials(self, credentials):
        """Check user crednetials for anomalies before registration"""
        if isinstance(credentials, dict) is False:
            return "credentials are dictionaries.Try using application/json!"
        self.user_credentials = credentials
        if not self.user_credentials:
            return "Enter data for the server to process!"
        if len(self.user_credentials) != 4:
            return "Ensure attendant details include their email, username, password, role"
        # check whether data has all required fields
        fields = ["username", "email", "password", "role"]
        for i in range(len(fields)):
            if fields[i] not in self.user_credentials.keys():
                return "Ensure to include {}".format(fields[i])
        # check for empty strings
        for item in self.user_credentials:
            if self.user_credentials[item] == "" or self.user_credentials[item] == " ":
                return "Ensure to enter sensible user data!"
        if  bool(re.search(r'@', self.user_credentials["email"])) is False:
            return "Your email should have an @ somewhere!"
        if self.user_credentials["role"]!="admin" and self.user_credentials["role"] != "attendant":
            return "Roles are that of the admin and attendant only!"
        if len(self.user_credentials["password"]) < 6:
            return "Password too short! make it at least 6 chars log."
        return "Details are ok!"
    def check_userIds(self, userId):
        """Check user ids"""
        if isinstance(userId, int) is False:
            return "Make sure userId is a number!"
        elif userId < 1:
            return "0 is not a valid id!"
        else:
            return "Id is ok!"


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


class SalesUtils:
        """A model holding sales model helper functions"""
        def __init__(self):
                """class constructor"""
                self.sale_details = dict()
        def inspect_sale_details(self, sale_details):
                """A method to check sale details before purchase"""
                # check datatype of sales details
                if isinstance(sale_details, dict) is False:
                        return "credentials are dictionaries.Try using application/json!"
                self.sale_details = sale_details
                # check if any data is entered
                if not self.sale_details:
                        return "Enter data for the server to process!"
                # ensure the required fields are present
                if len(self.sale_details) != 4:
                        return "Ensure Sale details include attendant, product name, quantity and bill!"
                options = ["attendant", "product", "quantity", "bill"]
                for i in range(len(options)):
                        if options[i] not in self.sale_details.keys():
                                return "Ensure to include {}".format(options[i])
                # check for empty and null entries
                for item in self.sale_details:
                        if self.sale_details[item] == "" or self.sale_details[item] == " ":
                                return "Ensure the data fields i.e product are not empty or null!"
                return "Details are ok!"
        def check_id(self, saleId):
                """Inspect sale ids before quering database"""
                if isinstance(saleId, int) is False:
                        return "Ensure sale id is a number!"
                elif saleId < 1:
                        return "Id 0 doesn't exist!"
                else:
                        return "Id is ok!"
