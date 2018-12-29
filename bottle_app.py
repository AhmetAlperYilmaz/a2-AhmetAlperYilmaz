
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
            %s
            %s
            </body>
        </html>
    """ % (title,text,back)
    return page

mypassword = "219aeb43c0cc62089487cc77c6603b760edac4d616186e6fea5d0aa8122f49c2"
#Password Protection has been taken from this link:
#https://bitbucket.org/damienjadeduff/hashing_example/raw/master/hash_password.py

your_comments_list=""

@route('/password')
def password():
    password="""
    <form action="/comment" method="get">
    <fieldset>Please enter your password to be able to comment:<br>
    <input type="text" name="password">
    <input type="submit" value="Enter"></fieldset>
    </form><br>
    """
<<<<<<< HEAD
    backs="""<a href="/">Return To Webpage</a>"""
=======
    backs="""<a href="/index.html">Return To Webpage</a>"""
>>>>>>> dcc01da77f979c1dc89bf99d2a6ae3027a296073
    return htmlify("Password for Website",password,backs)


@route('/comment')
def comment():
    password_confirm = request.GET["password"]
    mypass = create_hash(password_confirm)
    comment="""
    <form action="/comments" method="get">
    <fieldset>Your comment:<br>
    <input type="text name="yourcomment"><br>
    <input type="submit" value="submit">
    </fieldset>
    </form> """
    backs="""<a href="/password">Return Back</a>"""
    if mypass == mypassword:
<<<<<<< HEAD
        return htmlify("Commentable Website",mycomment,backs)
=======
        return htmlify("Commentable Website",comment,backs)
>>>>>>> dcc01da77f979c1dc89bf99d2a6ae3027a296073
    else:
        return htmlify("Warning","Your password is wrong",backs)

@route('/comments')
def comment_of_website():
<<<<<<< HEAD
    comment_op = request["mycomment"]
    global your_comments_list
    your_comments_list = your_comments_list + comment_op
    backs="""<a href="/password">Return Back</a>"""
    return htmlify("Commentable Website",your_comments_list,backs)
=======
    comment_s = request.GET["comment"]
    global your_comments_list
    your_comments_list = your_comments_list + comment_s
<<<<<<< HEAD
    links="""<a href="/password">Return To Webpage</a>"""
    return htmlify("Commentable Website",your_comments_list,links)
>>>>>>> 82fbc617a76b20e048bd2efd5067143f24b8d1c2
=======
    backs="""<a href="/password">Return Back</a>"""
    return htmlify("Commentable Website",your_comments_list,backs)
>>>>>>> dcc01da77f979c1dc89bf99d2a6ae3027a296073

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
