#

# from database import Database                                     # from the database.py file import the Database class
# import uuid                                                       # importing uuid module (unique universal identifier)
# import datetime                                                   # importing the datetime module
#
#
# class Post(object):
#
#     def __init__(self, blog_id, title, content, author, date=datetime.datetime.utcnow(), id=None):     # we added 6 more parameters to initialize ... this makes for better coding ... easier to change/edit
#         self.blog_id = blog_id                                              # this parameter is for the blog that our post is in .. so we need the blog id
#         self.title = title                                                  # title of the post
#         self.content = content                                              # the content of the post
#         self.author = author                                                # the author of the post
#         self.created_date = date                                            # datetime module will date when the post was created ...
#         self.id = uuid.uuid4().hex if id is None else id                    # will produce a random unique id for each post ...
#                                                                             # we set id=None in the parameters so the uuid can work
#
#
#     def save_to_mongo(self):                                     # defining the method save to mongo ... with self parameter
#         Database.insert(collection='posts',                      # accessing the Database class to us the insert method
#                         data=self.json())                        # inserting all the data from the json function into the 'posts' collection
#                                                                  # the 'posts' collection is saved into a database called terminal-blog ..
#                                                                  # the database is stored in the mongodb server
#                                                                  # so this method basucally saves the data into the database we created
#
#
#     def json(self):                                              # defining the method json. only self is needed as a parameter.
#         return {                                                 # when this method is called .. it will return the following data
#             'id': self.id,                                       # this method is basically to have all the parameters LINE20 for our post in one function
#             'blog_id': self.blog_id,                             # so if we call the json method is already contains all our information for the users post
#             'author': self.author,
#             'content': self.content,
#             'title': self.title,
#             'created_date': self.created_date
#         }
#
#
#     @classmethod                                                               # using class method ... in this case the class we are using is Post
#     def from_mongo(cls, id):                                                   # defining the method from_mongo with cls and id as parameter
#         post_data = Database.find_one(collection='posts', query={'id': id})    # creating variable post data bound to the Database class which is using the method find.one to access the posts collection
#                                                                                # will find the id of the post ... # example : Post.from_mongo('123') ... this method will find the query which uses 123 as an id
#         return cls(blog_id=post_data['blog_id'],                               # the post with the following data will be returned
#                    title=post_data['title'],
#                    content=post_data['content'],
#                    author=post_data['content'],
#                    date=post_data['created_date'],
#                    id=post_data['id'])
#
#
#
#
#     @staticmethod                                                                              # if we dont use self ... must use this method
#     def from_blog(id):                                                                         # defining the from blog method with id as parameter
#         return [post for post in Database.find(collection='posts', query={'blog_id': id})]     # using for statement
#                                                                                                # we want to return all the posts that are in a specific blog
#                                                                                                # we use the Database class which is using the find method
#                                                                                                # this method will find the blog_id and then return all posts in the blog


print()


#SAME CODING FROM TERMINAL PROJECT POST.PY FILE SLIGHTLY EDITED
import uuid
from src.common.database import Database
import datetime


class Post(object):
    def __init__(self, blog_id, title, content, author, created_date=datetime.datetime.utcnow(), _id=None):      # changed date into created_date
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.created_date = created_date                                                            # changed date into created_date
        self._id = uuid.uuid4().hex if _id is None else _id


    def save_to_mongo(self):
        Database.insert(collection='posts', data=self.json())

    def json(self):
        return {
            '_id': self._id,
            'blog_id': self.blog_id,
            'author': self.author,
            'content': self.content,
            'title': self.title,
            'created_date': self.created_date
         }

    @classmethod
    def from_mongo(cls, id):
        post_data = Database.find_one(collection='posts', query={'_id': id})
        return cls(**post_data)                                                                 # **post_data is equalvaleint to LINES 43-48 in previous coding
                                                                                                # makes for better coding

    @staticmethod
    def from_blog(id):
        return [post for post in Database.find(collection='posts', query={'blog_id': id})]



# CHANGED all the id into _id in order to override mongos default id that is given
# Dont have to change the id in LINES 93-101
