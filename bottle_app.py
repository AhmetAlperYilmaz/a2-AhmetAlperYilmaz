
#####################################################################
### Assignment skeleton
### You can alter the below code to make your own dynamic website.
### The landing page for assignment 3 should be at /
#####################################################################

from bottle import route, run, default_app, debug, static_file, template, request, Request
from hashlib import sha256

def create_hash(password):
    pw_bytestring = password.encode()
    return sha256(pw_bytestring).hexdigest()

def htmlify(title,text,back):
    page = """
        <!doctype html>
        <html lang="en">
            <head>
                <meta charset="utf-8" />
                <title>%s</title>
            </head>
            <body>
            %s <br>
            %s
            </body>
        </html>
    """ % (title,text,back)
    return page

mypassword = "219aeb43c0cc62089487cc77c6603b760edac4d616186e6fea5d0aa8122f49c2"
#Password Protection has been taken from this link:
#https://bitbucket.org/damienjadeduff/hashing_example/raw/master/hash_password.py

your_comments_list=""

def index_html():
    return static_file('index.html',root="./")

@route('/password')
def password():
    password="""
    <form action="/comment" method="post">
    <fieldset>Please enter your password to be able to comment:<br>
    <input type="text" name="password">
    <input type="submit" value="Enter">
    <h1>Did you like my website?</h1>
    <input type="radio" name="like" value="other" checked> Perfect<br>
    <input type="radio" name="like" value="other"> Good<br>
    <input type="radio" name="like" value="other"> Not bad<br>
    <input type="radio" name="like" value="other"> Bad<br>
    <input type="radio" name="like" value="other"> Awful<br>
    </fieldset></form><br>
    """
    backs="""<a href="/">Return To Webpage</a>"""
    return htmlify("Password for Website",password,backs)

def comment():
    password_confirm = request.POST["password"]
    mypass = create_hash(password_confirm)
    comment="""
    <form action="/comments" method="post">
    <fieldset>Your comment:<br>
    <input type="text" name="comment"><br>
    <input type="submit" value="submit">
    </fieldset>
    </form> """
    backs="""<a href="/password">Return Back</a>"""
    if mypass == mypassword:
        return htmlify("Commentable Website",comment,backs)
    else:
        return htmlify("Warning","Your password is wrong",backs)

def comment_of_website():
    comment_s = request.POST["comment"]
    global your_comments_list
    your_comments_list = your_comments_list + "\n" + comment_s
    backs="""<a href="/password">Return Back</a>"""
    return htmlify("Commentable Website",your_comments_list,backs)

@route('/static/<filename>')                   
def static_file_callback(filename):
    return static_file(filename, root='./')

route("/comment","POST",comment)
route("/comments","POST",comment_of_website)
route("/","GET",index_html)

#####################################################################
### Don't alter the below code.
### It allows this website to be hosted on Heroku
### OR run on your computer.
#####################################################################

# This line makes bottle give nicer error messages
debug(True)
# This line is necessary for running on Heroku
app = default_app()
# The below code is necessary for running this bottle app standalone on your computer.
if __name__ == "__main__":
  run()
