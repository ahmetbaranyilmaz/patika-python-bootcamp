from models.user import User
import sqlite3
import time

class DBConnection():
    def __init__(self, dbName) -> None:
        self.dbName = dbName

    def __getTableName(self) -> str:
        """
        This method created to create table name
        :return: <str> data_ with timestamp
        """
        return f'data_{str(time.time()).split(".")[0]}'

    def connectDB(self) -> sqlite3.Connection:
        """
        This method created to make connection to database
        :return: sqlite3.Connection
        """
        connection = None
        try:
            connection = sqlite3.connect(self.dbName)
        except Exception as err:
            print(f'Failed to create connection')
        else:
            return connection

    def createTable(self) -> None:
        """
        This method created to create table in database
        :return: None
        """
        connection = self.connectDB()
        try:
            curr = connection.cursor()
            query = f'''
                    CREATE TABLE IF NOT EXISTS {self.__getTableName()} (
                    "USER_ID"	INTEGER NOT NULL UNIQUE,
                    "NAME"	TEXT NOT NULL,
                    "USERNAME"	TEXT NOT NULL,
                    "EMAIL"	TEXT NOT NULL,
                    "EMAILUSERLK"	INTEGER NOT NULL,
                    "USERNAMELK"	INTEGER NOT NULL,
                    "BIRTH_YEAR"	INTEGER NOT NULL,
                    "BIRTH_MONTH"	INTEGER NOT NULL,
                    "BIRTH_DAY"	INTEGER NOT NULL,
                    "COUNTRY"	TEXT NOT NULL,
                    "ACTIVE_STATUS"	INTEGER NOT NULL,
                    PRIMARY KEY("USER_ID")
                );
            '''

            curr.execute(query)
            connection.commit()

        except Exception as err:
            print(f'Failed to create table')
            print(err)
        finally:
            connection.close()

    def addUser(self, user:User) -> None:
        """
        This method created to insert user to database
        :param user: <User> user model
        :return: None
        """
        connection = self.connectDB()
        try:
            query = f'''
            INSERT INTO {self.__getTableName()} 
            (NAME, USERNAME, EMAIL, 
             EMAILUSERLK, USERNAMELK,
             BIRTH_YEAR, BIRTH_MONTH, BIRTH_DAY, 
             COUNTRY, ACTIVE_STATUS) 
            VALUES("{user.name}", "{user.username}", "{user.email}",
                   "{user.emailuserlk}", "{user.usernamelk}",
                   "{user.birthYear}", "{user.birthMonth}", "{user.birthDay}",
                   "{user.country}", "{user.activeStatus}")
            '''
            curr = connection.cursor()
            curr.execute(query)
            connection.commit()
        except Exception as err:
            print(f'Failed to insert data')
            print(err)
        finally:
            connection.close()