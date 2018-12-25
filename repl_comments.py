from hashlib import sha256

print("Welcome to the program which memorises your comments.")

mypassword = "219aeb43c0cc62089487cc77c6603b760edac4d616186e6fea5d0aa8122f49c2"
#Password Protection has been taken from this link:
#https://bitbucket.org/damienjadeduff/hashing_example/raw/master/hash_password.py

def create_hash(password):
    pw_bytestring = password.encode()
    return sha256(pw_bytestring).hexdigest()
    
your_comments_list = []
while(len(your_comments_list >=0)):
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
    else:
        print("This password is wrong, please try again.")

