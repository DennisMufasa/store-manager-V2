"""A model to manipulate products in inventory"""
# third-party imports
import psycopg2
# local imports
from ..utils import ProductUtils
from ..utils import Database


class Product(Database):
    """A class to manipulate product data"""
    def __init__(self):
        """class constructor"""
        # initializing the Database class as self in this class Product
        Database.__init__(self)
    def add_product(self, product_details):
        """A method to add new products to inventory"""
        if ProductUtils().inspect_product_details(product_details) == "Details are ok!":
            product_name = product_details["product_name"]
            product_category = product_details["product_category"]
            quantity = product_details["quantity"]
            unit_cost = product_details["unit_cost"]
            try:
                con = self.connection()
                cursor = con.cursor()
                query = """INSERT INTO inventory (productname, productcategory, productqty, unit_cost)
                                            VALUES({}, {}, {}, {});""".format(
                                                product_name, product_category, quantity, unit_cost
                                            )
                cursor.execute(query)
                con.commit()
                return "New product added!"
            except(Exception, psycopg2.DatabaseError) as error:
                print("Database Error", error)
            finally:
                if con:
                    cursor.close()
                    con.close()
                    print("Conncetion Closed!")
        return ProductUtils().inspect_product_details(product_details)
    def get_product(self, productId):
        """fetch a specific product by its id"""
        if ProductUtils().check_ids(productId) == "Id is ok!":
            try:
                con = self.connection()
                cursor = con.cursor()
                query = """SELECT * FROM inventory WHERE productid = {};""".format(productId)
                cursor.execute(query)
                resultset = cursor.fetchone()
                if not resultset:
                    return "That id is not registered!"
                return """  Product ID       : {},
                            Product name     : {},
                            Product Category : {},
                            unit cost        : {}""".format(
                                resultset[0], resultset[1], resultset[2], resultset[4]
                            )
            except(Exception, psycopg2.DatabaseError) as error:
                print("Database Error", error)
            finally:
                if con:
                    cursor.close()
                    con.close()
                    print("Conncetion Closed!")
    def get_products(self):
        """Fetch all products"""
        try:
            con = self.connection()
            cursor = con.cursor()
            query = """SELECT * FROM inventory;"""
            cursor.execute(query)
            resultset = cursor.fetchall()
            if not resultset:
                return "No products in Inventory"
            for result in resultset:
                print(result)
        except(Exception, psycopg2.DatabaseError) as error:
            print("Database Error", error)
        finally:
            if con:
                cursor.close()
                con.close()
                print("Conncetion Closed!")
    def add_existing_product(self, productId, value):
        """Add onto an already existing item"""
        if isinstance(value,int) is False and value < 1:
            return "You have to add sensible amounts of products!"
        if ProductUtils().check_ids(productId) == "Id is ok!":
            try:
                con = self.connection()
                cursor = con.cursor()
                query = """UPDATE inventory SET productqty = {} WHERE productid = {};""".format(
                    value, productId
                )
                cursor.execute(query)
                con.commit()
                return "{} items added!".format(value)
            except(Exception, psycopg2.DatabaseError) as error:
                print("Database Error", error)
            finally:
                if con:
                    cursor.close()
                    con.close()
                    print("Connection Closed!")
        return ProductUtils().check_ids(productId)
    def delete_product(self, productId):
        """Remove a product from inventory"""
        if ProductUtils().check_ids(productId) == "Id is ok!":
            try:
                con = self.connection()
                cursor = con.cursor()
                query = """DELETE FROM inventory WHERE productid = {}""".format(productId)
                cursor.execute(query)
                con.commit()
                return "Data successfully deleted!"
            except(Exception, psycopg2.DatabaseError) as error:
                print("Database Error", error)
            finally:
                if con:
                    cursor.close()
                    con.close()
                    print("Connection Closed!")
        return ProductUtils().check_ids(productId)
        