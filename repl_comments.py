print("Welcome to the program which memorises your comments.")
your_comments_list = []
while (len(your_comments_list) >= 0):
    listing_number = 1
    your_input = input("Please enter your comment: ")
    your_comments_list.append(your_input)
    print("All of your comments are: ")
    for one_of_your_comment in your_comments_list:
        print(str(listing_number) + "-) " + one_of_your_comment)
        listing_number += 1

