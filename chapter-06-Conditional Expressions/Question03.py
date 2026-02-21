# this program checks if the comment is a spam comment or not entered by the user.

spam = input("enter the comment you want to check:")

if "make a lot of money" in spam :
    print("This is a spam comment.")
elif "buy now" in spam:
        print("This is a spam comment.")
elif "subscribe this" in spam:
        print("This is a spam comment.")
else:
    print("This is not a spam comment.")