"""A sales module"""
# third-party import
import psycopg2
# local imports
from ..utils import Database
from ..utils import SalesUtils
from ..productmodel.productmodel import Product


class Sale(Product, Database):
    """A class to manipulate sales"""
    def __init__(self):
        """Class constructor"""
        Product.__init__(self)  # initialize the product class as a sale class object(self)
        Database.__init__(self) # initialize the database as a sale class object(self)
    def create_sale(self, sale_details):
        """A method that adds sales to database"""
        if SalesUtils().inspect_sale_details(sale_details) == "Details are ok!":
            attendant = sale_details["attendant"]
            product = sale_details["product"]
            quantity = sale_details["quantity"]
            bill = sale_details["bill"]
            #Check if item is available for sale
            if self.fetch_product_tosell(product) == "Product available for sale!":
                try:
                    con = self.connection()
                    cursor = con.cursor()
                    query = """INSERT INTO sales (attendant, product, quantity, salecost)
                                            VALUES({}, {}, {}, {});""".format(
                                                attendant, product, quantity, bill)
                    cursor.execute(query)
                    con.commit()
                    return "New sale made successfully!"
                except(Exception, psycopg2.Error) as error:
                    print("Something went wrong!", error)
                finally:
                    """Close the database connection"""
                    if con:
                        """close database connection"""
                        cursor.close()
                        con.close()
                        print("Connection closed!")
            return self.fetch_product_tosell(product)
        return SalesUtils().inspect_sale_details(sale_details)
    def get_sales(self):
        """A method to fetch all sales"""
        try:
            con = self.connection()
            cursor = con.cursor()
            query = """SELECT * FROM sales;"""
            cursor.execute(query)
            resultset = cursor.fetchall()
            if not resultset:
                return "No sales available!"
            for result in resultset:
                print(result)
        except(Exception, psycopg2.Error) as error:
            print("Something went wrong!", error)
        finally:
            """close connection"""
            if con:
                cursor.close()
                con.close()
                print("Connection closed!")
    def get_one_sale(self, saleId):
        """Fetch a specific sale based on its id"""
        if SalesUtils().check_id(saleId) == "Id is ok!":
            try:
                con = self.connection()
                cursor = con.cursor()
                query = """SELECT * FROM sales WHERE saleid = {}""".format(saleId)
                cursor.execute(query)
                resultset = cursor.fetchone()
                if not resultset:
                    return "No sales with that id exist!"
                return """ Sale Id     : {},
                            attendant   :{},
                            product     :{},
                            quantity    :{},
                            sale cost   :{}""".format(
                                resultset[0],resultset[1],resultset[2],resultset[3],resultset[4])
            except(Exception, psycopg2.Error) as error:
                print("Something went wrong!", error)
            finally:
                """Close database"""
                if con:
                    cursor.close()
                    con.close()
                    print("Connection closed!")
        return SalesUtils().check_id(saleId)
