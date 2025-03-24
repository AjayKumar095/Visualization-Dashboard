import os 
import sys

import json
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

### confing mongodb

class Manage_db:
    
    def __init__(self, db_name:str):
        load_dotenv()
        self.__db_name  = db_name
        self.__db_uri = os.getenv("DB_URI")
        self.__client = MongoClient(self.__db_uri, server_api= ServerApi('1'))   
              
    def get_db(self):
        """ Get the database object """
        try:
            client = self.__client
            db = client[self.__db_name]
            return db
        except Exception as e:
            print(e)
            
    def get_client(self):
        """ Get the client object """
        try:
            return self.__client
        except Exception as e:
            print(e) 
            
    def close_connection(self):
        """ Close the connection """
        try:
            self.__client.close()
            return None
        except Exception as e:
            print(e)
                
if __name__ == "__main__":
    mangae_db = Manage_db("Sampledatabase")
    client = mangae_db.get_client()
    try:
       client.admin.command("ping")
       print("Connected successfully")
    except Exception as e:
        print(e)  

