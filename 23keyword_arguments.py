#keyword argument = arguments preceded by an identifier when we pass them to a function. The order of the arguments doesn't matter, unlike positional arguments 
#                   Pythons knowa the names of the arguments that our function receives

def hello(frist,middle,last):
    print("Hello",frist,middle,last)

hello(last="Code",middle="Dude",frist="Bro")