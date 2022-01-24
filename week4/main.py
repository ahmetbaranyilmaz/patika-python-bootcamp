import argparse
from fileOperations import fileReader as fr
from database.DBConnection import DBConnection

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-f', '--file', required=True, help='Enter file name')
    parser.add_argument('-db', '--db', required=True, help='Enter database name')

    args = parser.parse_args()
    fileName = args.file
    dbName = args.db

    db = DBConnection(dbName)
    db.createTable()

    for user in fr.readJson(fileName):
        db.addUser(user)