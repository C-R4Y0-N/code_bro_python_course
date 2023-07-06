#function = a block of code which is executed only when it is called.

def hello(frist_name,last_name,age):
    print("Hello "+frist_name+" "+last_name)
    print("You are "+str(age)+" years old")
    print("Have a nice day!")
    
def say_hello():
    print("Hi!")

frist_name=input("Which is your frist name:")
last_name=input("Which is your last name:")
age=int(input("Which is your age: "))
hello(frist_name,last_name,age)
say_hello()