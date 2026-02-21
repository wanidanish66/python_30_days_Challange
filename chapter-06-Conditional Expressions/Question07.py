# this program checks if the post entered by the user is talking about micro or not.

post = input("Enter the post: ")

if "Micro".lower() in post.lower():
    print("This post is talking about micro.")
else:
    print("This post is not talking about micro.")