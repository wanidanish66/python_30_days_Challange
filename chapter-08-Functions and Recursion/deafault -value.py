# this is a function which greets the user by deafault value set by the user

def greet(name, ending="thank you"):
    print("good day",name, ending)

greet("harry","thanks")  # the ending will be thanks in the function body as as specified
greet("micro")           # the ending will be thank you in the function body as deafault parameter value set by the user