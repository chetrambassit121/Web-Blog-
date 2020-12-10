# coding from terminal project BLOG.PY file

# import datetime                                                     # importing the datetime module
# import uuid                                                         # importing uuid module (unique universal identifier)
# from database import Database                                       # from the database.py file import the class Database
# from models.post import Post                                        # from the python package models, access post.py, then import the class Post
#
#
# class Blog(object):                                                 # creating the Blog class with object as parameter
#     def __init__(self, author, title, description, id=None):        # initializing 4 parameters that we want for our Blog class
#         self.author = author                                        # Blog will have a author
#         self.title = title                                          # a title
#         self.description = description                              # a description
#         self.id = uuid.uuid4().hex if id is None else id            # will produce a random unique id for each post ...
#                                                                     # we set id=None in the parameters so the uuid can work
#
#
#     def new_post(self):                                                                  # defining the new_post method with self parameter
#         title = input('enter the posts title: ')                                         # variable title bound to the string .. input (builtin) allows user to enter a title
#         content = input('enter the posts content: ')                                     # variable content bound to the string .. input (builtin) allows user to enter content
#         date = input('enter the date (in format DDMMYYYY), or leave blank: ')            # variable date bound to the string .. input (builtin) allows user to enter a date
#         if date == "":                                                                   # using if statement .. if date is blank then date will be bound to datetime.datetime.utcnow() .. this will get the current date for us
#             date = datetime.datetime.utcnow()                                            # if user is inputting date .. we use strptime(date, "%d%m%Y") ... string parse time
#                                                                                          # this will convert the variable date into a time format using %d%m%Y
#         else:
#             date = datetime.datetime.strptime(date, "%d%m%Y")
#
#                                                                         # creating post variable bound to the Post class which contains 5 parameters
#         post = Post(blog_id=self.id,                                    # this blog_id belongs to the Blog class .. we will get a unique blog id
#                     title=title,                                        # title is from Post class
#                     content=content,                                    # content is from Post class
#                     author=self.author,                                 # this author is from the Blog class
#                     date=date)
#         post.save_to_mongo()                                            # the variable post using the save to mongo method from the Post class .. saves the created post
#
#     def get_posts(self):
#         return Post.from_blog(self.id)                                  # Post class will use the from_blog method containg the self.id parameter from Blog class
#                                                                         # this will return all the posts from the current blog_id
#
#     def save_to_mongo(self):                                            # defining the save to mongo method with self as parameter
#         Database.insert(collection='blogs',                             # accessing the Database class to us the insert method
#                         data=self.json())                               # inserting all the data from the json method into the 'blogs' collection
#
#
#     def json(self):                                                     # defining the json method with self as parameter
#         return {                                                        # when this method is called .. it will return the following data
#             'author': self.author,                                      # this method is basically to have all the parameters LINE9 for our blog in one function
#             'title': self.title,                                        # so if we call the json function it already contains all our information for the users blog
#             'description': self.description,
#             'id': self.id
#         }
#
#
#     @classmethod                                                       # using class method ... in this case the class we are using is Blog
#     def from_mongo(cls, id):                                           # defining the get from mongo method with cls and id as paramter
#         blog_data = Database.find_one(collection='blogs',              # creating variable blog_data bound to the Database class which is using th find_one method to access blogs collection
#                                       query={'id': id})                # accessing the collections blogs .. searching for the id
#
#         return cls(author=blog_data['author'],                         # will return the blog with the following data
#                    title=blog_data['title'],
#                    description=blog_data['description'],
#                    id=blog_data['id'])



print()



#SAME CODING FROM TERMINAL PROJECT BLOG.PY FILE SLIGHTLY EDITED
# REMOVE LINES 19 - 26 not needed for this application
import uuid
import datetime
from src.common.database import Database
from src.models.post import Post


class Blog(object):
    def __init__(self, author, title, description, author_id, _id=None):         # added the author_id to give author a unique id
        self.author = author
        self.author_id = author_id                                               # added author id = author id
        self.title = title
        self.description = description
        self._id = uuid.uuid4().hex if _id is None else _id

    def new_post(self, title, content, date=datetime.datetime.utcnow()):           # added title, content, date as a parameter
        post = Post(blog_id=self._id,
                    title=title,
                    content=content,
                    author=self.author,
                    created_date=date)                                              # changed from date to created date
        post.save_to_mongo()

    def get_posts(self):
        return Post.from_blog(self._id)

    def save_to_mongo(self):
        Database.insert(collection='blogs', data=self.json())

    def json(self):
        return {
            'author': self.author,
            'author_id': self.author_id,                                            # added 'author_id': self.author_id
            'title': self.title,
            'description': self.description,
            '_id': self._id
        }

    @classmethod                                                                    # bounds our method to the Blog class
    def from_mongo(cls, id):
        blog_data = Database.find_one(collection='blogs', query={'_id': id})
        return cls(**blog_data)                                                     # **blog_data is equalvaleint to LINES 59-62 in previous coding , makes for better coding


    #ADDED this method
    @classmethod                                                                    # bounds our method to the Blog class
    def find_by_author_id(cls, author_id):                                          # defining the find by author id method with cls (Blog class) and author id as parameters
        blogs = Database.find(collection='blogs', query={'author_id': author_id})   # created variable blogs bound to the Database class in which the class is using its find method
                                                                                    # find method will access the blogs collection .. and then access the author_id we are searching for
        return [cls(**blog) for blog in blogs]                                      # return the parameters in list form [] from our Blog class based on the author_id
                                                                                    # BASICALLY this method finds blogs based on author id



# CHANGED all the id into _id in order to override mongos default id that is given
# Dont have to change the id in LINES 109 . 110
