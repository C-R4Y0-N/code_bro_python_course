#lamba parameters:expression

#def double(x):
#    return x * 2
#
#print(double(5))

double= lambda x: x*2
multiply = lambda x, y: x * y
add = lambda x,y,z: x+y+z
full_name = lambda frist_name, last_name: frist_name+" "+last_name
age_check = lambda age:True if age >= 18 else False
print(double(5))
print(multiply(5,6))
print(add(5,6,7))
print(full_name ("Juanito","Perez"))
print(full_name ("Juanito","Perez"))
print(age_check (18))
print(age_check (17))




