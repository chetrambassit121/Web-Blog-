# from flask import Flask               # from flask import the Flask class
#                                       # flask is a framework development we will use for our app
#                                       # so we are creating a flask application
#
# app = Flask(__name__)                 # we created variable app ... bound to ... the class Flask ...
#                                       # ... class contains pycharm built in variable called __name__
#                                       # it is standard to use __name__ with Flask ... helps to define our app
#
#
# @app.route('/')                       # this LINE is a standard route www.mysite.com/api/
#                                       # api stands for (Application Programming Interface)
#                                       # the forward slash in quotes acts as a empty end point
#
# def hello_method():                   # defining method that will execute when we access the endpoint ('/') .. we can access with browser or mobile
#     return "Hello, world!"            # when used this method will return hello world!
#
# if __name__ == '__main__':            # another requirement to run the Flask app we want to create
#     app.run(port=5000)                # the app variable with .run() function will run our app
#                                       # we can change the port number to make a different link



#  WHEN this coding is executed ...  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit) ... will print
#  WHEN you click on the link ... a new browser will open with the string 'hello world' printed


print()



# from flask import Flask               # from flask import the Flask class
#                                       # flask is a framework development we will use for our app
#                                       # so we are creating a flask application
#
# app = Flask(__name__)                 # we created variable app ... bound to ... the class Flask ...
#                                       # ... class contains pycharm built in variable called __name__
#                                       # it is standard to use __name__ with Flask ... helps to define our app
#
#
# @app.route('/')                       # this LINE is a standard route www.mysite.com/api/
#                                       # api stands for (Application Programming Interface)
#                                       # the forward slash in quotes acts as a empty end point
#
# def hello_method():                   # defining method that will execute when we access the endpoint ('/') .. we can access with browser or mobile
#     return "Hello, world!"            # when used this method will return hello world!
#
# if __name__ == '__main__':            # another requirement to run the Flask app we want to create
#     app.run(port=4995)                # the app variable with .run() function will run our app
#                                       # we can change the port number to make a different link



#  WHEN this coding is executed ...  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit) ... will print
#  WHEN you click on the link ... a new browser will open with the string 'hello world' printed
# SAME results as previous example but with different port number ... EDITED LINE 48



print()



# from flask import Flask, render_template       # Flask is a framework development we will use for our app, added render template as well
#
# app = Flask(__name__)         # we created variable app ... bound to ... the class Flask ...
#                               # ... class contains pycharm built in variable called __name__
#                               # it is standard to use __name__ with Flask ... helps to define our app
#
# @app.route('/')               # creating API (Application Programming Interface) endpoints that we will use
#                               # the forward slash in quotes acts as a empty end point
#                               # LINE7 will bring us to www.mysite.com/api/
#
# def hello_method():           # defining method that will execute when we access the endpoint ('/') .. we can access with browser or mobile
#     return render_template('login.html')    # will return the login html we created .. render_template is a flask builtin and is needed for this
#
# if __name__ == '__main__':    # another requirement to run the Flask app we want to create
#     app.run(port=4995)        # app variable with .run() function will run the port number ... in this case its 4995
#                               # we can also change the 5000 to 4995 or w.e port number we want



# EDITED LINE 74 by ADDING login.html file in LINE74 .... this will open up the page 127.0.0.1:4995 ...
# two white boxes and submit button will be displayed ...
# one box for user email and one for user password ... login.html file in LINE74



print()



# from flask import Flask, render_template, request, session  # Flask is a framework development we will use for our app, added render template, request, and session
#
# from src.models.user import User                         # importing the User class and all the methods involved
#
# app = Flask(__name__)         # we created variable app ... bound to ... the class Flask ...
#                               # ... class contains pycharm built in varible called __name__
#                               # it is standard to use __name__ with Flask ... helps to define our app
#
# @app.route('/')               # creating API (Application Programming Interface) endpoints that we will use
#                               # the forward slash in quotes acts as a empty end point
#                               # LINE7 will bring us to www.mysite.com/api/
# def hello_method():           # defining method that will execute when we access the endpoint ('/') .. we can access with browser or mobile
#     return render_template('login.html')    # will return the html we created .. render_template is a flask builtin and is needed for this
#
#
# @app.route('/login', methods=['POST'])          # now accessing the login.html file we created while using POST as a method for security purposes
# def login_user():             # defining the login_user method
#     email = request.form['email']       # variable email bound to request function ... requesting the form with the (feild) name='email' in it
#     password = request.form['password'] # variable password bound to request function ... requesting the form with the (feild) name='password'
#
#     if User.login_valid(email, password):  # if statement .. User class using the login_valid method based on email / password
#         User.login(email)                  # will use login method if email/password is valid
#
#     return render_template("profile.html", email=session['email'])  # return the profile.html in template package .. profile.html has access to email variable ..
#                                                                     # email variable bound the session of the email
#
#
# if __name__ == '__main__':                # another requirement to run the Flask app we want to create
#     app.run(port=4995, debug=True)        # LINE96 variable with .run() function will run our app ...
#                                           # we can also change the 5000 to 4995 or w.e port number we want
#                                           # debug = true will show us if there are any errors with web application
#
#
#
# #this coding will allow user to finally input there email and password ... we will get somewhat of a login result
# # if we run multiple times we will recieve an error



print()



# from flask import Flask, render_template, request, session  # Flask is a framework development we will use for our app, added render template, request, and session
# from src.models.user import User                         # importing the User class and all the methods involved
# from src.common.database import Database


# app = Flask(__name__)         # we created variable app ... bound to ... the class Flask ...
#                               # ... class contains pycharm built in varible called __name__
#                               # it is standard to use __name__ with Flask ... helps to define our app
#
# app.secret_key = 'jose'       # sets a secure secret key with password of our choosing ... also requirement

# @app.route('/')               # creating API (Application Programming Interface) endpoints that we will use
#                               # the forward slash in quotes acts as a empty end point
#                               # LINE7 will bring us to www.mysite.com/api/
# def hello_method():           # defining method that will execute when we access the endpoint ('/') .. we can access with browser or mobile
#     return render_template('login.html')    # will return the html we created .. render_template is a flask builtin and is needed for this
#
#
#
# @app.before_first_request                   # we call database before we make a request or application ...
# def initialize_database():                  # defining the method
#     Database.initialize()                   # Database class being initialized with initialize() method
#
#
#
# @app.route('/login', methods=['POST'])          # now accessing the login.html file we created while using POST as a method for security purposes
# def login_user():             # defining the login_user method
#     email = request.form['email']       # variable email bound to request function ... requesting the form with the (feild) name='email' in it
#     password = request.form['password'] # variable password bound to request function ... requesting the form with the (feild) name='password'
#
#     if User.login_valid(email, password):  # if statement .. User class using the login_valid method based on email / password
#         User.login(email)                  # will use login method if email/password is valid
#     else:                                  # else
#         session['email'] = None            # using session builtin for email to be bound to the value None ..
#
#
#     return render_template("profile.html", email=session['email'])  # return the profile.html in template package .. profile.html has access to email variable ..
#                                                                     # email variable bound the session of the email
#
#
# if __name__ == '__main__':                # another requirement to run the Flask app we want to create
#     app.run(port=4995, debug=True)        # LINE96 variable with .run() function will run our app ...
#                                           # we can also change the 5000 to 4995 or w.e port number we want
                                            # debug = true will show us if there are any errors with web application



# ADDED LINE 144
# ADDED LINES 154-156
# ADDED 167 - 168
# NOW we can access the 127.0.0.1:4995/login link .. type in an existing email / password ... if valid will login in
# will say "Hello {email}"
# if email / password not valid then pycharm will print "Hello None"



print()



# from flask import Flask, render_template, request, session  # Flask is a framework development we will use for our app, added render template, request, and session
# from src.models.user import User                         # importing the User class and all the methods involved
#


# app = Flask(__name__)         # we created variable app ... bound to ... the class Flask ...
#                               # ... class contains pycharm built in variable called __name__
#                               # it is standard to use __name__ with Flask ... helps to define our app
#
# app.secret_key = 'jose'       # sets a secure secret key with password of our choosing ... also requirement

# @app.route('/')               # creating API (Application Programming Interface) endpoints that we will use
#                               # the forward slash in quotes acts as a empty end point
#                               # LINE7 will bring us to www.mysite.com/api/
# def hello_method():           # defining method that will execute when we access the endpoint ('/') .. we can access with browser or mobile
#     return render_template('login.html')    # will return the html we created .. render_template is a flask builtin and is needed for this
#
#
#
# @app.before_first_request                   # we call database before we make a request or application ...
# def initialize_database():                  # defining the method
#     Database.initialize()                   # Database class being initialized with initialize() method
#
#
#
# @app.route('/login', methods=['POST'])          # now accessing the login.html file we created while using POST as a method for security purposes
# def login_user():                               # defining the login_user method
#     email = request.form['email']               # variable email bound to request function ... requesting the form with the (feild) name='email' in it .. this form is the login.html file
#     password = request.form['password']          # variable password bound to request function ... requesting the form with the (feild) name='password' .. this form is the login.html file
#
#     if User.login_valid(email, password):  # if statement .. User class using the login_valid method based on email / password
#         User.login(email)                  # will use login method if email/password is valid
#     else:                                  # else
#         session['email'] = None            # using session builtin for email to be bound to the value None ..
#
#
#     return render_template("profile.html", email=session['email'])  # return the profile.html in template package .. profile.html has access to email variable ..
#                                                                     # email variable bound the session of the email
#
#
# @app.route('/auth/register', methods=['POST'])                         # this route will now access the register.html file we created and allow posts (coded and hidden from users ... auth means authentication
# def register_user():                                                   # defining the method register user
#     email = request.form['email']                                      # created the variable email bound to request function ... requesting the form with the (feild) name='email' in it .. this form is the login.html file
#     password = request.form['password']                                # created the variable password bound to request function ... requesting the form with the (feild) name='password' .. this form is the login.html file
#
#     User.register(email, password)                                     # using the User classes register method which contains email , password data
#
#     return render_template("profile.html", email=session['email'])     # profile.html in template package has access to email variable ..
#                                                                        # email variable bound the session of the email
#
#
# if __name__ == '__main__':                # another requirement to run the Flask app we want to create
#     app.run(port=4995, debug=True)        # LINE96 variable with .run() function will run our app ...
#                                           # we can also change the 5000 to 4995 or w.e port number we want
#                                           # debug = true will show us if there are any errors with web application
#
#
#
# ADDED LINES 235 - 243 this route will allow new users to register



print()



# from flask import Flask, render_template, request, session  # Flask is a framework development we will use for our app, added render template, request, and session
# from src.models.user import User                            # importing the User class and all the methods involved
#


# app = Flask(__name__)                                       # we created variable app ... bound to ... the class Flask ...
#                                                             # ... class contains pycharm built in variable called __name__
#                                                             # it is standard to use __name__ with Flask ... helps to define our app
#
# app.secret_key = 'jose'                                     # sets a secure secret key with password of our choosing ... also requirement

# @app.route('/')                                             # creating API (Application Programming Interface) endpoints that we will use
#                                                             # the forward slash in quotes acts as a empty end point
#                                                             # LINE7 will bring us to www.mysite.com/api/
# def hello_method():                                         # defining method that will execute when we access the endpoint ('/') .. we can access with browser or mobile
#     return render_template('login.html')                    # will return the html we created .. render_template is a flask builtin and is needed for this
#
#
#
# @app.before_first_request                   # we call database before we make a request or application ...
# def initialize_database():                  # defining the method
#     Database.initialize()                   # Database class being initialized with initialize() method
#
#
#
# @app.route('/login', methods=['POST'])          # now accessing the login.html file we created while using POST as a method for security purposes
# def login_user():                               # defining the login_user method
#     email = request.form['email']               # variable email bound to request function ... requesting the form with the (feild) name='email' in it .. this form is the login.html file
#     password = request.form['password']         # variable password bound to request function ... requesting the form with the (feild) name='password' .. this form is the login.html file
#
#     if User.login_valid(email, password):       # if statement .. User class using the login_valid method based on email / password
#         User.login(email)                       # will use login method if email/password is valid
#     else:                                       # else
#         session['email'] = None                 # using session builtin for email to be bound to the value None ..
#
#
#     return render_template("profile.html", email=session['email'])  # return the profile.html in template package .. profile.html has access to email variable ..
#                                                                     # email variable bound the session of the email
#
#
# @app.route('/auth/register', methods=['POST'])                         # this route will now access the register.html file we created and allow posts (coded and hidden from users ... auth means authentication
# def register_user():                                                   # defining the method register user
#     email = request.form['email']                                      # created the variable email bound to request function ... requesting the form with the (feild) name='email' in it .. this form is the login.html file
#     password = request.form['password']                                # created the variable password bound to request function ... requesting the form with the (feild) name='password' .. this form is the login.html file
#
#     User.register(email, password)                                     # using the User classes register method which contains email , password data
#
#     return render_template("profile.html", email=session['email'])     # profile.html in template package has access to email variable ..
#                                                                        # email variable bound the session of the email
#
# @app.route('/blogs/<string:user_id>')                                          # this route is to get to the blogs page based on user_id
# @app.route('/blogs')                                                           # this route is to get to the blogs page when the user.id is None
# def user_blogs(user_id=None):                                                  # definied the user blogs method with the parameter user_id which is bound to the value None
#     if user_id is not None:                                                    # if user id is not none ... basically if a valid user id is found then ...
#         user = User.get_by_id(user_id)                                         # variable user bound to User class .. class is using its get by id method ...method wants to get the user_id
#     else:                                                                      # else statement ... so basiclly if the user id is None then that means we are accessing our own blogs .. if not our own blogs then we will get a error
#         user = User.get_by_email(session['email'])                             # variable user bound to the User class .. class is using its get_by_email method .. method will access the our own email which has to use the flask builtin session
#     blogs = user.get_blogs()                                                   # created  variable blogs bound to user variable .. this variable uses get_blogs method to return blogs
#     return render_template("user_blogs.html", blogs=blogs, email=user.email)   # we will return the following data using render template flask builtin .. accesses templates we created
#                                                                                # return the users_blog.html in template package, along with the lists of blogs, and the users email
#                                                                                # basically this will return a list of blogs that pertains to a specific user.email
#
#
#
# if __name__ == '__main__':                # another requirement to run the Flask app we want to create
#     app.run(port=4995, debug=True)        # LINE96 variable with .run() function will run our app ...
#                                           # we can also change the 5000 to 4995 or w.e port number we want
#                                           # debug = true will show us if there are any errors with web application



# ADDED LINES 308-318  ... this is the blogs route which allows user to view a list of there blogs ..


print()



# from flask import Flask, render_template, request, session  # Flask is a framework development we will use for our app, added render template, request, and session
# from src.models.user import User                            # importing the User class and all the methods involved
#


# app = Flask(__name__)                                       # we created variable app ... bound to ... the class Flask ...
#                                                             # ... class contains pycharm built in variable called __name__
#                                                             # it is standard to use __name__ with Flask ... helps to define our app
#
# app.secret_key = 'jose'                                     # sets a secure secret key with password of our choosing ... also requirement

# @app.route('/')                                             # creating API (Application Programming Interface) endpoints that we will use
#                                                             # the forward slash in quotes acts as a empty end point
#                                                             # LINE7 will bring us to www.mysite.com/api/
# def hello_method():                                         # defining method that will execute when we access the endpoint ('/') .. we can access with browser or mobile
#     return render_template('login.html')                    # will return the html we created .. render_template is a flask builtin and is needed for this
#
#
#
# @app.before_first_request                   # we call database before we make a request or application ...
# def initialize_database():                  # defining the method
#     Database.initialize()                   # Database class being initialized with initialize() method
#
#
#
# @app.route('/login', methods=['POST'])          # now accessing the login.html file we created while using POST as a method for security purposes
# def login_user():                               # defining the login_user method
#     email = request.form['email']               # variable email bound to request function ... requesting the form with the (feild) name='email' in it .. this form is the login.html file
#     password = request.form['password']         # variable password bound to request function ... requesting the form with the (feild) name='password' .. this form is the login.html file
#
#     if User.login_valid(email, password):       # if statement .. User class using the login_valid method based on email / password
#         User.login(email)                       # will use login method if email/password is valid
#     else:                                       # else
#         session['email'] = None                 # using session builtin for email to be bound to the value None ..
#
#
#     return render_template("profile.html", email=session['email'])  # return the profile.html in template package .. profile.html has access to email variable ..
#                                                                     # email variable bound the session of the email
#
#
# @app.route('/auth/register', methods=['POST'])                         # this route will now access the register.html file we created and allow posts (coded and hidden from users ... auth means authentication
# def register_user():                                                   # defining the method register user
#     email = request.form['email']                                      # created the variable email bound to request function ... requesting the form with the (feild) name='email' in it .. this form is the login.html file
#     password = request.form['password']                                # created the variable password bound to request function ... requesting the form with the (feild) name='password' .. this form is the login.html file
#
#     User.register(email, password)                                     # using the User classes register method which contains email , password data
#
#     return render_template("profile.html", email=session['email'])     # profile.html in template package has access to email variable ..
#                                                                        # email variable bound the session of the email
#
# @app.route('/blogs/<string:user_id>')                                          # this route is to get to the blogs page based on user_id
# @app.route('/blogs')                                                           # this route is to get to the blogs page when the user.id is None
# def user_blogs(user_id=None):                                                  # definied the user blogs method with the parameter user_id which is bound to the value None
#     if user_id is not None:                                                    # if user id is not none ... basically if a valid user id is found then ...
#         user = User.get_by_id(user_id)                                         # variable user bound to User class .. class is using its get by id method ...method wants to get the user_id
#     else:                                                                      # else statement ... so basiclly if the user id is None then that means we are accessing our own blogs .. if not our own blogs then we will get a error
#         user = User.get_by_email(session['email'])                             # variable user bound to the User class .. class is using its get_by_email method .. method will access the our own email which has to use the flask builtin session
#     blogs = user.get_blogs()                                                   # created  variable blogs bound to user variable .. this variable uses get_blogs method to return blogs
#     return render_template("user_blogs.html", blogs=blogs, email=user.email)   # we will return the following data using render template flask builtin .. accesses templates we created
#                                                                                # return the users_blog.html in template package, along with the lists of blogs, and the users email
#                                                                                # basically this will return a list of blogs that pertains to a specific user.email
#
#
# @app.route('/posts/<string:blog_id>')                                                               # this route is for the posts which are accessed based on the blog_id
# def blog_posts(blog_id):                                                                            # creating the blog_posts method with blog_id as a parameter
#     blog = Blog.from_mongo(blog_id)                                                                 # creating variable blog  bound to the class Blog which is using its from_mongo method to access the blog_id
#     posts = blog.get_posts()                                                                        # creating posts variable bound to the variable blog which is using the get posts method to get the post
#
#     return render_template('posts.html', posts=posts, blog_title=blog.title, blog_id=blog._id)      # we will return the following data using render template flask builtin .. accesses templates we created
#                                                                                                     # the post will be displayed .. starting with blog title ....


#
# if __name__ == '__main__':                # another requirement to run the Flask app we want to create
#     app.run(port=4995, debug=True)        # LINE96 variable with .run() function will run our app ...
#                                           # we can also change the 5000 to 4995 or w.e port number we want
#                                           # debug = true will show us if there are any errors with web application



# ADDED LINES 399 - 405 this is the route to access our posts



print()



# from flask import Flask, render_template, request, session  # Flask is a framework development we will use for our app, added render template, request, and session
# from src.models.user import User                            # importing the User class and all the methods involved
#


# app = Flask(__name__)                                       # we created variable app ... bound to ... the class Flask ...
#                                                             # ... class contains pycharm built in variable called __name__
#                                                             # it is standard to use __name__ with Flask ... helps to define our app
#
# app.secret_key = 'jose'                                     # sets a secure secret key with password of our choosing ... also requirement

# @app.route('/')                                             # creating API (Application Programming Interface) endpoints that we will use
#                                                             # the forward slash in quotes acts as a empty end point
#                                                             # LINE7 will bring us to www.mysite.com/api/
# def hello_method():                                         # defining method that will execute when we access the endpoint ('/') .. we can access with browser or mobile
#     return render_template('login.html')                    # will return the html we created .. render_template is a flask builtin and is needed for this
#
#
#
# @app.before_first_request                   # we call database before we make a request or application ...
# def initialize_database():                  # defining the method
#     Database.initialize()                   # Database class being initialized with initialize() method
#
#
#
# @app.route('/login', methods=['POST'])          # now accessing the login.html file we created while using POST as a method for security purposes
# def login_user():                               # defining the login_user method
#     email = request.form['email']               # variable email bound to request function ... requesting the form with the (feild) name='email' in it .. this form is the login.html file
#     password = request.form['password']         # variable password bound to request function ... requesting the form with the (feild) name='password' .. this form is the login.html file
#
#     if User.login_valid(email, password):       # if statement .. User class using the login_valid method based on email / password
#         User.login(email)                       # will use login method if email/password is valid
#     else:                                       # else
#         session['email'] = None                 # using session builtin for email to be bound to the value None ..
#
#
#     return render_template("profile.html", email=session['email'])  # return the profile.html in template package .. profile.html has access to email variable ..
#                                                                     # email variable bound the session of the email
#
#
# @app.route('/auth/register', methods=['POST'])                         # this route will now access the register.html file we created and allow posts (coded and hidden from users ... auth means authentication
# def register_user():                                                   # defining the method register user
#     email = request.form['email']                                      # created the variable email bound to request function ... requesting the form with the (feild) name='email' in it .. this form is the login.html file
#     password = request.form['password']                                # created the variable password bound to request function ... requesting the form with the (feild) name='password' .. this form is the login.html file
#
#     User.register(email, password)                                     # using the User classes register method which contains email , password data
#
#     return render_template("profile.html", email=session['email'])     # profile.html in template package has access to email variable ..
#                                                                        # email variable bound the session of the email
#
# @app.route('/blogs/<string:user_id>')                                          # this route is to get to the blogs page based on user_id
# @app.route('/blogs')                                                           # this route is to get to the blogs page when the user.id is None
# def user_blogs(user_id=None):                                                  # definied the user blogs method with the parameter user_id which is bound to the value None
#     if user_id is not None:                                                    # if user id is not none ... basically if a valid user id is found then ...
#         user = User.get_by_id(user_id)                                         # variable user bound to User class .. class is using its get by id method ...method wants to get the user_id
#     else:                                                                      # else statement ... so basiclly if the user id is None then that means we are accessing our own blogs .. if not our own blogs then we will get a error
#         user = User.get_by_email(session['email'])                             # variable user bound to the User class .. class is using its get_by_email method .. method will access the our own email which has to use the flask builtin session
#     blogs = user.get_blogs()                                                   # created  variable blogs bound to user variable .. this variable uses get_blogs method to return blogs
#     return render_template("user_blogs.html", blogs=blogs, email=user.email)   # we will return the following data using render template flask builtin .. accesses templates we created
#                                                                                # return the users_blog.html in template package, along with the lists of blogs, and the users email
#                                                                                # basically this will return a list of blogs that pertains to a specific user.email
#
#
# @app.route('/blogs/new', methods=['POST', 'GET'])                           # this route (aka endpoint) has access to two methods ... if POST is used then user submitted a post
#                                                                             # if its GET user will be presented with a form to write a new blog
# def create_new_blog():                                                      # defining the create new blog method
#     if request.method == 'GET':                                             # using flask builtin request.method .. if method is GET
#         return render_template('new_blog.html')                             # the new_blog.html form/page will return ... user can fill out this form to create blog
#     else:                                                                   # this else statement means POST was the selected method ...
#         title = request.form['title']                                       # title is return
#         description = request.form['description']                           # description is returned
#         user = User.get_by_email(session['email'])                          # User email is returned
#
#         new_blog = Blog(user.email, title, description, user._id)           # creating variable new_blog bound to the Blog class which contains the respectful parameters
#         new_blog.save_to_mongo()                                            # the variable new_blog is then saved with the save to mongo method which is in the Blog class
#
#         return make_response(user_blogs(user._id))                          # we then return the data in the users blog method
#                                                                             # make_response is a flask builtin method used to return the data from another method
#
#
# @app.route('/posts/<string:blog_id>')                                                               # this route is for the posts which are accessed based on the blog_id
# def blog_posts(blog_id):                                                                            # creating the blog_posts method with blog_id as a parameter
#     blog = Blog.from_mongo(blog_id)                                                                 # creating variable blog  bound to the class Blog which is using its from_mongo method to access the blog_id
#     posts = blog.get_posts()                                                                        # creating posts variable bound to the variable blog which is using the get posts method to get the post
#
#     return render_template('posts.html', posts=posts, blog_title=blog.title, blog_id=blog._id)      # we will return the following data using render template flask builtin .. accesses templates we created
#                                                                                                     # the post will be displayed .. starting with blog title ....
#
# #
# if __name__ == '__main__':                # another requirement to run the Flask app we want to create
#     app.run(port=4995, debug=True)        # LINE96 variable with .run() function will run our app ...
#                                           # we can also change the 5000 to 4995 or w.e port number we want
#                                           # debug = true will show us if there are any errors with web application



#ADDED lines 490 - 504 ... the route for new blogs to be created
# now we have a route /blogs/new that will allow us to create the new blog with a title and description window to input our data



print()



# from flask import Flask, render_template, request, session  # Flask is a framework development we will use for our app, added render template, request, and session
# from src.models.user import User                            # importing the User class and all the methods involved
#


# app = Flask(__name__)                                       # we created variable app ... bound to ... the class Flask ...
#                                                             # ... class contains pycharm built in variable called __name__
#                                                             # it is standard to use __name__ with Flask ... helps to define our app
#
# app.secret_key = 'jose'                                     # sets a secure secret key with password of our choosing ... also requirement

# @app.route('/')                                             # creating API (Application Programming Interface) endpoints that we will use
#                                                             # the forward slash in quotes acts as a empty end point
#                                                             # LINE7 will bring us to www.mysite.com/api/
# def hello_method():                                         # defining method that will execute when we access the endpoint ('/') .. we can access with browser or mobile
#     return render_template('login.html')                    # will return the html we created .. render_template is a flask builtin and is needed for this
#
#
#
# @app.before_first_request                   # we call database before we make a request or application ...
# def initialize_database():                  # defining the method
#     Database.initialize()                   # Database class being initialized with initialize() method
#
#
#
# @app.route('/login', methods=['POST'])          # now accessing the login.html file we created while using POST as a method for security purposes
# def login_user():                               # defining the login_user method
#     email = request.form['email']               # variable email bound to request function ... requesting the form with the (feild) name='email' in it .. this form is the login.html file
#     password = request.form['password']         # variable password bound to request function ... requesting the form with the (feild) name='password' .. this form is the login.html file
#
#     if User.login_valid(email, password):       # if statement .. User class using the login_valid method based on email / password
#         User.login(email)                       # will use login method if email/password is valid
#     else:                                       # else
#         session['email'] = None                 # using session builtin for email to be bound to the value None ..
#
#
#     return render_template("profile.html", email=session['email'])  # return the profile.html in template package .. profile.html has access to email variable ..
#                                                                     # email variable bound the session of the email
#
#
# @app.route('/auth/register', methods=['POST'])                         # this route will now access the register.html file we created and allow posts (coded and hidden from users ... auth means authentication
# def register_user():                                                   # defining the method register user
#     email = request.form['email']                                      # created the variable email bound to request function ... requesting the form with the (feild) name='email' in it .. this form is the login.html file
#     password = request.form['password']                                # created the variable password bound to request function ... requesting the form with the (feild) name='password' .. this form is the login.html file
#
#     User.register(email, password)                                     # using the User classes register method which contains email , password data
#
#     return render_template("profile.html", email=session['email'])     # profile.html in template package has access to email variable ..
#                                                                        # email variable bound the session of the email
#
# @app.route('/blogs/<string:user_id>')                                          # this route is to get to the blogs page based on user_id
# @app.route('/blogs')                                                           # this route is to get to the blogs page when the user.id is None
# def user_blogs(user_id=None):                                                  # definied the user blogs method with the parameter user_id which is bound to the value None
#     if user_id is not None:                                                    # if user id is not none ... basically if a valid user id is found then ...
#         user = User.get_by_id(user_id)                                         # variable user bound to User class .. class is using its get by id method ...method wants to get the user_id
#     else:                                                                      # else statement ... so basiclly if the user id is None then that means we are accessing our own blogs .. if not our own blogs then we will get a error
#         user = User.get_by_email(session['email'])                             # variable user bound to the User class .. class is using its get_by_email method .. method will access the our own email which has to use the flask builtin session
#     blogs = user.get_blogs()                                                   # created  variable blogs bound to user variable .. this variable uses get_blogs method to return blogs
#     return render_template("user_blogs.html", blogs=blogs, email=user.email)   # we will return the following data using render template flask builtin .. accesses templates we created
#                                                                                # return the users_blog.html in template package, along with the lists of blogs, and the users email
#                                                                                # basically this will return a list of blogs that pertains to a specific user.email
#
#
# @app.route('/blogs/new', methods=['POST', 'GET'])                           # this route (aka endpoint) has access to two methods ... if POST is used then user submitted a new blog
#                                                                             # if its GET user will be presented with a form to write a new blog .. blog_id in string form required so we know which blog to access
# def create_new_blog():                                                      # defining the create new blog method
#     if request.method == 'GET':                                             # using flask builtin request.method .. if method is GET
#         return render_template('new_blog.html')                             # the new_blog.html form/page will return ... user can fill out this form to create blog
#     else:                                                                   # this else statement means POST was the selected method ...
#         title = request.form['title']                                       # title is return
#         description = request.form['description']                           # description is returned
#         user = User.get_by_email(session['email'])                          # User email is returned
#
#         new_blog = Blog(user.email, title, description, user._id)           # creating variable new_blog bound to the Blog class which contains the respectful parameters
#         new_blog.save_to_mongo()                                            # the variable new_blog is then saved with the save to mongo method which is in the Blog class
#
#         return make_response(user_blogs(user._id))                          # we then return the data in the users blog method
#                                                                             # make_response is a flask builtin method used to return the data from another method
#
#
# @app.route('/posts/<string:blog_id>')                                                               # this route is for the posts which are accessed based on the blog_id
# def blog_posts(blog_id):                                                                            # creating the blog_posts method with blog_id as a parameter
#     blog = Blog.from_mongo(blog_id)                                                                 # creating variable blog  bound to the class Blog which is using its from_mongo method to access the blog_id
#     posts = blog.get_posts()                                                                        # creating posts variable bound to the variable blog which is using the get posts method to get the post
#
#     return render_template('posts.html', posts=posts, blog_title=blog.title, blog_id=blog._id)      # we will return the following data using render template flask builtin .. accesses templates we created
#                                                                                                     # the post will be displayed .. starting with blog title ....

#
# @app.route('/posts/new/<string:blog_id>', methods=['POST', 'GET'])          # this route (aka endpoint) has access to two methods ... if POST is used then user submitted a post
#                                                                             # if its GET user will be presented with a form to write a new blog .. blog_id in string form required so we know which blog to access
# def create_new_post(blog_id):                                               # defining the create new blog method with blog id as parameter
#     if request.method == 'GET':                                             # using flask builtin request.method .. if method is GET
#         return render_template('new_post.html', blog_id=blog_id)            # the new_post.html form/page will return blog_id required here to access the respectful blog ... user can fill out this form to create post
#     else:                                                                   # this else statement means POST was the selected method ...
#         title = request.form['title']                                       # title is return
#         content = request.form['content']                                   # content is returned
#         user = User.get_by_email(session['email'])                          # User email is returned
#
#         new_post = Post(blog_id, title, content, user._id)                  # creating variable new_post bound to the Post class which contains the respectful parameters
#         new_post.save_to_mongo()                                            # the variable new_post is then saved with the save to mongo method which is in the Post class
#
#         return make_response(blog_posts(blog_id))                          # we then return the data in the users blog method
#                                                                            # make_response is a flask builtin method used to return the data from another method
#
#
#
# if __name__ == '__main__':                # another requirement to run the Flask app we want to create
#     app.run(port=4995, debug=True)        # LINE96 variable with .run() function will run our app ...
#                                           # we can also change the 5000 to 4995 or w.e port number we want
#                                           # debug = true will show us if there are any errors with web application
#
#
#
#ADDED LINES 621 - 635 route for new posts ... thus /posts/new/<string:blog_id>'





print()




from flask import Flask, render_template, request, session, make_response
from src.common.database import Database
from src.models.user import User
from src.models.blog import Blog
from src.models.post import Post

app = Flask(__name__)         # we created variable app ... bound to ... the class Flask ...
                              # ... class contains pycharm built in varible called __name__
                              # it is standard to use __name__ with Flask ... helps to define our app
app.secret_key = 'jose'       # sets a secure secret key with password of our choosing



@app.route('/')
def home_template():
    return render_template('home.html')



@app.route('/login')                                # 127.0.0.1:4995/Login         # creating API (Application Programming Interface) endpoints that we will use
                                                    # the forward slash (/) login accesses the login template
                                                    # will bring us to www.mysite.com/api/
def login_template():                               # defining function that will execute when we access ('/login') .. we can access with browser or mobile
    return render_template('login.html')            # we will return the following data using render template flask builtin .. accesses templates we created
                                                    # will return the login html we created .. render_template is a flask builtin and is needed for this



@app.route('/register')    # # 127.0.0.1:4995/Register
def register_template():
    return render_template('register.html')



@app.before_first_request                   # we call database before we make a request or application ...
def initialize_database():                  # defining the method
    Database.initialize()                   # Database class being initialized with initialize() method



@app.route('/auth/login', methods=['POST'])          # this route will now access the login.html file we created and allow posts (coded and hidden from users) ... auth means authenticates
def login_user():             # defining the login_user function
    email = request.form['email']       # variable email bound to request function ... requesting the form email
    password = request.form['password']  # variable password bound to request function ... requesting the form password

    if User.login_valid(email, password):  # if statement with User class from user.py file ...
        User.login(email)                  # will use login method if email/password is valid
    else:
        session['email'] = None                # if the email is not valid it will default to None .. so only correct email can login

    return render_template("profile.html", email=session['email'])  # we will return the following data using render template flask builtin .. accesses templates we created
                                                                    # profile.html in template package has access to email variable ..
                                                                    # email variable bound the session of the email



@app.route('/auth/register', methods=['POST'])      # this route will now access the register.html file we created and allow posts (coded and hidden from users ... auth means authentication
def register_user():               # function to register users
    email = request.form['email']  # variable email bound to request function ... requesting the form email
    password = request.form['password']  # variable password bound to request function ... requesting the form password

    User.register(email, password)     # using the User classes register method which contains email , password data

    return render_template("profile.html", email=session['email'])  # we will return the following data using render template flask builtin .. accesses templates we created
                                                                    # profile.html in template package has access to email variable ..
                                                                    # email variable bound the session of the email



@app.route('/blogs/<string:user_id>')                                          # this route is to get to the blogs page based on user_id
@app.route('/blogs')                                                           # this route is to get to the blogs page when the user.id is None
def user_blogs(user_id=None):                                                  # definied the user blogs method with the parameter user_id which is bound to the value None
    if user_id is not None:                                                    # if user id is not none ... basically if a valid user id is found then ...
        user = User.get_by_id(user_id)                                         # variable user bound to User class .. class is using its get by id method ...method wants to get the user_id
    else:                                                                      # else statement ... so basiclly if the user id is None then that means we are accessing our own blogs .. if not our own blogs then we will get a error
        user = User.get_by_email(session['email'])                             # variable user bound to the User class .. class is using its get_by_email method .. method will access the our own email which has to use the flask builtin session
    blogs = user.get_blogs()                                                   # created  variable blogs bound to user variable .. this variable uses get_blogs method to return blogs
    return render_template("user_blogs.html", blogs=blogs, email=user.email)   # we will return the following data using render template flask builtin .. accesses templates we created
                                                                               # return the users_blog.html in template package, along with the lists of blogs, and the users email
                                                                               # basically this will return a list of blogs that pertains to a specific user.email



@app.route('/blogs/new', methods=['POST', 'GET'])                           # this route (aka endpoint) has access to two methods ... if POST is used then user submitted a post
                                                                            # if its GET user will be presented with a form to write a new blog
def create_new_blog():                                                      # creating new function
    if request.method == 'GET':                                             # using flask builtin request.method .. if method is GETun flat earth paintings
        return render_template('new_blog.html')                             # the new_blog.html form/page will return ... un flat earth paintingsuser can fill out this form to create blog
    else:                                                                   # this else statement means POST was the selected method ...
        title = request.form['title']                                       # title is return
        description = request.form['description']                           # description is returned
        user = User.get_by_email(session['email'])                          # User email is returned

        new_blog = Blog(user.email, title, description, user._id)           # creating variable new_blog bound to the Blog class which contains the respectful parameters
        new_blog.save_to_mongo()                                            # the variable new_blog is then saved with the respectful method

        return make_response(user_blogs(user._id))                          # we then return the users_blog function LINE 191
                                                                            # make_response is a flask builtin method




@app.route('/posts/<string:blog_id>')        # this route is for the posts which are accessed based on the blog_id
def blog_posts(blog_id):                     # creating the blog_posts method with blog_id as a parameter
    blog = Blog.from_mongo(blog_id)          # creating variable blog  bound to the class Blog which is using its from_mongo method to access the blog_id
    posts = blog.get_posts()                 # creating posts variable bound to the variable blog which is using the get posts method to get the post

    return render_template('posts.html', posts=posts, blog_title=blog.title, blog_id=blog._id)      # we will return the following data using render template flask builtin .. accesses templates we created
                                                                                                    # the post will be displayed .. starting with blog title ....




@app.route('/posts/new/<string:blog_id>', methods=['POST', 'GET'])    # this route (aka endpoint) has access to two methods ... if POST is used then user submitted a post
                                                      # if its GET user will be presented with a form to write a new blog
def create_new_post(blog_id):                                # creating new function
    if request.method == 'GET':                        # using flask builtin request.method .. if method is GET
        return render_template('new_post.html', blog_id=blog_id)       # the new_blog.html form/page will return ... user can fill out this form to create blog
    else:                                               # this else statement means POST was the selected method ...
        title = request.form['title']                   # title is return
        content = request.form['content']               # description is returned
        user = User.get_by_email(session['email'])     # User email is returned

        new_post = Post(blog_id, title, content, user.email)       #creating variable new_blog bound to the Blog class which contains the respectful parameters
        new_post.save_to_mongo()                                        # the variable new_blog is then saved with the respectful method

        return make_response(blog_posts(blog_id))                        # we then return the users_blog function LINE 191
                                                                            # make_response is a flask builtin method



if __name__ == '__main__':    # another requirment to run the Flask app we want to create
    app.run(port=5000, debug=True)        # LINE3 variable with .run() function will run our app ...
                              # we can also change the 5000 to 4995 or w.e port number we want




# this coding does the following

# 1) we have a /login page which allows existing users to input there email / password ...
#    if successful it will read Hello "email"
# 2) if users email / password does not exist it will read Hello "None"
# 3) we have a /register page which allows new users to input there email / password information .. this will create the account
#    once you click "sign up" .. it will print Hello "email"
# 4) we have a /blogs page that can only be accessed if a user is logged in ... will print "email" blogs
# 5) we have a posts page that can be accessed if a user is logged in ... and in the user is on there blogs
#    user can click on sample title link to get to posts ... if there are no posts will print a string saying ni posts yet



