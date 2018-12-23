
#####################################################################
### Assignment skeleton
### You can alter the below code to make your own dynamic website.
### The landing page for assignment 3 should be at /
#####################################################################

from bottle import route, run, default_app, debug, static_file
from hashlib import sha256

mypassword = "219aeb43c0cc62089487cc77c6603b760edac4d616186e6fea5d0aa8122f49c2"
#Password Protection has been taken from this link:
#https://bitbucket.org/damienjadeduff/hashing_example/raw/master/hash_password.py

def create_hash(password):
    pw_bytestring = password.encode()
    return sha256(pw_bytestring).hexdigest()
    
def htmlify(title,text):
    page = """
        <!doctype html>
        <html lang="en">
            <head>
                <meta charset="utf-8" />
                <title>%s</title>
            </head>
            <body>
            %s
            </body>
            <div><input type="text" style="width: 50"/>><button>Add Comment</button></div>
        </html>
    """ % (title,text)
    return page

def index():
    return htmlify("Commentable Website",
                   "Welcome to the program which memorises your comments.")

your_comments_list = []
while (len(your_comments_list) >= 0):
    listing_number = 1
    your_input = input("Please enter your comment or if you want to exit from the program please write 'exit': ")
    
    if (your_input == "exit"):
    	break
    
    passwordconfirming = input("Please enter your password to memorise your comments.")
    password_hash = create_hash(passwordconfirming)
    
    if (mypassword == password_hash):
      print("Your password has been confirmed.")
    
      your_comments_list.append(your_input)
    print("All of your comments are: ")
    for one_of_your_comment in your_comments_list:
         print(str(listing_number) + "-) " + one_of_your_comment)
         listing_number += 1



def static_file_callback(filename):
    return static_file(filename, root='static')

route('/', 'GET', index)
route('/static/<filename>', 'GET', static_file_callback)



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