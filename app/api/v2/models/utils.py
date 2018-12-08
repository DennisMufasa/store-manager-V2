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
        if self.user_credentials["username"] == "":
            return "Username cannot be empty!"
        if self.user_credentials["email"] == "":
            return "Email cannot be empty!"
        if self.user_credentials["password"] == "":
            return "Password cannot be empty!"
        if self.user_credentials["role"] == "":
            return "Role cannot be empty!"
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