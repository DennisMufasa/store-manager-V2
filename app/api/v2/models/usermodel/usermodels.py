"""A model that manipulates store manager data"""
# third-party import
import psycopg2
# local import
from ..utils import UserUtils
from ..utils import Database

class User(Database):
    """A user model that inherits a database configuration class"""
    def __init__(self):
        """Class constructor"""
        Database.__init__(self) # instantiate the inherited class
    def add_user(self, credentials):
        """Add a new user to database"""
        inspect_credentials = UserUtils()
        if inspect_credentials.inspect_user_credentials(credentials) == "Details are ok!":
            username = credentials["username"]
            password = credentials["password"]
            email = credentials["email"]
            try:
                con = self.connection()
                cursor = con.cursor()
                query = """INSERT INTO users (username, email, password) VALUES
                ('{}', '{}','{}');""".format(
                    username, email, password)
                cursor.execute(query)
                con.commit
                return "New user added!"
            except(Exception, psycopg2.DatabaseError) as error:
                print("Database Error", error)
            finally:
                if con:
                    cursor.close()
                    con.close()
                    print("Connection closed!")
        return inspect_credentials.inspect_user_credentials(credentials)
    def get_user(self, userId):
        """fetch specific user by their id"""
        if isinstance(userId, int):
            try:
                con = self.connection()
                cursor = con.cursor()
                query = """SELECT * FROM users WHERE userId = {}""".format(userId)
                cursor.execute(query)
                resultset = cursor.fetchone()
                if not resultset:
                    return """That id is not registered to any user"""
                return """username  : {},
                            email   : {}""".format(resultset[1], resultset[2])
            except(Exception, psycopg2.DatabaseError) as error:
                print("Database Error", error)
            finally:
                if con:
                    cursor.close()
                    con.close()
                    print("Connection closed!")
        return "Ensure user id is a number!"
    def get_users(self):
        """Fetch all users"""
        try:
            con = self.connection()
            cursor = con.cursor()
            query = """SELECT * FROM users;"""
            cursor.execute(query)
            resultset = cursor.fetchall()
            if not resultset:
                return """There are no users registered!"""
            return """ username : {},
                        email   : {},
                        user id : {}""".format(
                            resultset[1],
                            resultset[2],
                            resultset[0]
                        )
        except(Exception, psycopg2.DatabaseError) as error:
            print("Database Error", error)
        finally:
            if con:
                cursor.close()
                con.close()
                print("Conncetion Closed!")
