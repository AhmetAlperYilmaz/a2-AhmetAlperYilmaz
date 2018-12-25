
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

def htmlify(title,text,link):
    page = """
        <!doctype html>
        <html lang="en">
            <head>
                <meta charset="utf-8" />
                <title>%s</title>
            </head>
            <body>
            %s
            %s
            </body>
        </html>
    """ % (title,text,link)
    return page

mypassword = "219aeb43c0cc62089487cc77c6603b760edac4d616186e6fea5d0aa8122f49c2"
#Password Protection has been taken from this link:
#https://bitbucket.org/damienjadeduff/hashing_example/raw/master/hash_password.py

your_comments_list=""

@route('/password')
def password_for_comment():
    password="""
    <form action="/comment" method="get">
    <fieldset>Please enter your password to be able to comment:<br>
    <input type="text" name="password">
    <input type="submit" value="Enter"></fieldset>
    </form><br>
    """
    links="""<a href="/">Return To Webpage</a>"""
    return htmlify("Password for Website",password,links)

@route('/comment')
def comment():
    password_confirm = request["password"]
    mypass = create_hash(password_confirm)
    mycomment="""
    <form action="/comments" method="get">
    <fieldset>Your comment:<br>
    <input type="text name="yourcomment"><br>
    <input type="submit" value="submit">
    </fieldset>
    </form> """
    links="""<a href"/password">Return To Webpage</a>"""
    if mypass == mypassword:
        return htmlify("Commentable Website",mycomment,links)
    else:
        return htmlify("Warning","Your password is wrong",links)

@route('/comments')
def comment_of_website():
    comment_op = request["comment"]
    global your_comments_list
    your_comments_list = your_comments_list + comment_op
    links="""<a href="/password">Return To Webpage</a>"""
    return htmlify("Commentable Website",your_comments_list,links)

@route('/static/<filename>')
def static_server(filename):
    return static_file(filename, root='./')

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
