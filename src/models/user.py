import uuid
from datetime import datetime

from flask import session

from src.common.database import Database
from src.models.blog import Blog


class User(object):                                                                     # creating class User
    def __init__(self, email, password, _id=None):                                      # initializing the parameters .. email , password , _id ,
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id                             # using uuid to generate a random id for User if _id is none ... else geneerate the already exsisting _id


    # BASICALLY these three parameters belong to the User class ... we use init with self, (parameter) to initliazie these parameters



    @classmethod                                                                        # bounds our get by email method to the User class
    def get_by_email(cls, email):                                                       # defining the get by email method ... parameters are cls (User class) , email
        data = Database.find_one("users", {"email": email})                             # variable data bound to the Database class from database.py ... using find_one method to access users collection and finding the email query
        if data is not None:                                                            # using if statement ... if data returned is not None
            return cls(**data)                                                          # then return the parameters in the cls (Users class) based on the variable data ... must use ** on the variable data

    # BASICALLY this method will search the mongo database for the users collection .. then search for the specific email we are looking for within the users collection ...
    # if the email isn't None .. then we will return the parameters in the User class



    @classmethod                                                                        # bounds our method to the User class
    def get_by_id(cls, _id):                                                            # defining the get by id method... parameters are cls (User class) , _id
        data = Database.find_one("users", {"_id": _id})                                 # same concept as get by email method except for the _id
        if data is not None:                                                            # if data is not None then the data in _id will return
            return cls(**data)

    # BASICALLY this method will search the mongo database for the users collection .. then it will search for the specfic _id we are looking for whtin the users collection
    # if the _id is isn't None .. then we will return the parameters in the User class


    @staticmethod                                                                       # dont need self so we add staticmethod
    def login_valid(email, password):                                                   # defining the login valid method w/ email , password as parameters ... checks whether a users email matches the password they sent us
        user = User.get_by_email(email)                                                 # created variable user bound to User class.. User class uses get by email method to retrive the email
        if user is not None:                                                            # using if statement ... if data from user is not none then ...
            return user.password == password                                            # password from database matches password from login valid method
        return False                                                                    # if user returns none its False

    # BASICALLY this method matches the password thats saved into the mongo database with the password user inputs


    @classmethod                                                                         # bounds our method to the User class
    def register(cls, email, password):                                                  #  definied the register method with cls (User class), email, password as parameters.....will register new users
        user = cls.get_by_email(email)                                                   # created variable user bound to cls (User class) using the get by email method .. method will access the email data to retrieving email
        if user is None:                                                                 # if statement .. if user returns None that means it doesnt exsist so we can register a new email
            new_user = cls(email, password)                                              # variable new_user bound to cls (User class) with email and password parameters ...
            new_user.save_to_mongo()                                                     # variable new user using saved to mongo to save the email / password
            session['email'] = email                                                     # session is a flask builtin .... stores email into session with its own unique id ... for security purposes
            return True                                                                  # since user is None we want this data to return true
        else:                                                                            # if user returns then it exisit
            return False                                                                 # so it will return false .. therefore this coding will not execute

    # BASICALLY this method will first search if a email exist .. if is doesnt exist .. then the new user information is saved into the mongo db ... if email does exsit .. then this method will return False



    @staticmethod                                                                       # dont need self so we add staticmethod
    def login(user_email):                                                              # defining the login method with user_email as parameter
        session['email'] = user_email                                                   # session is a flask builtin .. session contains the email which we bound to the variable user_email
                                                                                        # login valid is called before this method


    @staticmethod                                                                       # dont need self so we add staticmethod
    def logout():                                                                       # defining the logout method doesnt require any parameters
        session['email'] = None                                                         # using session which contains email bound to the value None



    def get_blogs(self):                                                                # defining get blogs method with only self as parameter
        return Blog.find_by_author_id(self._id)                                         # return the data from the Blog class using its find by author id .. returns all the blogs with that author id



    def new_blog(self, title, description):                                             # defining the new blog method with self , title , description as parameters
        blog = Blog(author=self.email,                                                  # created variable blog bound to the Blog class which accessing the respectful paramteres .. title / description dont use self
                    title=title,                                                        # the title / description will be entered by the user .. the users email is the author ... author id is the _id
                    description=description,
                    author_id=self._id)
        blog.save_to_mongo()                                                            # variable blog will use the save to mongo method from the Blog class

    # Basically this method is to create a new blog then save it to the mongo database .. title / description are the two parameters that user can input so they have no self.


    @staticmethod                                                                 # dont need self so we add staticmethod
    def new_post(blog_id, title, content, date):                                  # defining the new post method with the 4 following parameters
        blog = Blog.from_mongo(blog_id)                                           # created variable blog bound to the Blog class which is using its from mongo method to find the blog_id from the mongo database
        blog.new_post(title=title,                                                # variable blog using the new post method from the Blog class with the following parameters
                      content=content,
                      date=date)



    def json(self):                                                                     # defining the json method with only self as parameter
        return {"email": self.email,
                "_id": self._id,
                "password": self.password}                                              # we want to return the email , _id , and the password from the mongo database



    def save_to_mongo(self):                                                        # defining the save to mongo method with only self as parameter
        Database.insert("users", self.json())                                       # Database class using its insert method to save the email _id password from the json method into the users collection