#SAME CODING FROM TERMINAL FILE AND TERMINAL BLOG DATABASE.PY FILE
import pymongo                                            # importing pymongo module


class Database(object):                                   # creating a class called Database with parameter object
    URI = "mongodb://127.0.0.1:27017"                     # variable URI bound to the string ... string is the mongodb address
    DATABASE = None                                       # variable DATABASE bound to the value None
                                                          # LINE 6-7 are basic requierments to create a database within mongo db


    @staticmethod                                          # have to use the staticmethod if we are not using the self attribute
    def initialize():                                      # defining initialize method w/o self attribute ...
        client = pymongo.MongoClient(Database.URI)         # variable client bound to pymondo module ..
                                                           # ... module bound to MongoClient which accesses Database and URI variable
        Database.DATABASE = client["Fullstack"]            # the class Database and the variable DATABASE bound to the variable client which contains ...
                                                           # ... the database 'Fullstack' which we created with mongodb on the command prompt

    @staticmethod                                          # have to use the staticmethod if we are not using the self attribute
    def insert(collection, data):                          # defining insert method with collection and data as parameters
        Database.DATABASE[collection].insert(data)         # class Database and the variable DATABASE bound to collection parameter ...
                                                           # ... in which we are inserting parameter data .... inserting data into collection

    @staticmethod                                          # have to use the staticmethod if we are not using the self attribute
    def find(collection, query):                           # defining the find method with collection and query ... query is a specfic piece of data
        return Database.DATABASE[collection].find(query)   # return the collection and query that we are looking for


    @staticmethod                                               # have to use the staticmethod if we are not using the self attribute
    def find_one(collection, query):                            # defining the find_one method with collection and query ... query is a specfic piece of data
        return Database.DATABASE[collection].find_one(query)    # return the collection and query that we are looking for



# the find and find one methods do the same coding ... we created two methods to do the same action ... makes for more flexible coding
