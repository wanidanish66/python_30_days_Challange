import pyjokes

# this prints pyjokes.
joke = pyjokes.get_joke()
print(joke)

'''
so this is how you can use modules in python. 
you can import any module and use its functions. 
in this case we imported pyjokes and used its get_joke() function to get a joke and print it.
you can also import specific functions from a module like this:
from pyjokes import get_joke
joke = get_joke()
'''