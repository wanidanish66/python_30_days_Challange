a = 89    # the global value of a is 89

def fun():
    # we can change the global value of a  by using global key word like this
    global a    # the value of a is changed from 89 to 45
    a = 45
    print(a)

fun()
print(a)