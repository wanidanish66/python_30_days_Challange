# this is a simple program to greet all the names in the list starts with "s"

l1 = ["micro", "soham", "sahil", "roy"]

for i in l1:
    if i.lower().startswith("s"):
        print("hello", i)