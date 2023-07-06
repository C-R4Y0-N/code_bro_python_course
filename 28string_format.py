# str.format()= optional method that gives users more control when displaying output

number = 1000

print("The number pi is {:.3f}".format(number)) #Cantidad de decimales
print("The number pi is {:,}".format(number))#Coma cada tres numeros
print("The number pi is {:b}".format(number))#Binario
print("The number pi is {:o}".format(number))#octal number
print("The number pi is {:X}".format(number))#hexidecimal
print("The number pi is {:E}".format(number))#Scientific notation

animal = "cow"
item = "moon"
#
#print("The {} jumped over the {}".format(animal,item))
#print("The {0} jumped over the {1}".format(animal,item)) #postitional argument
#print("The {1} jumped over the {0}".format(animal,item)) #positional argument
#print("The {animal} jumped over the {item}".format(animal="cow",item="moon")) #keyword argument

text="The {} jumped over the {}"
print(text.format(animal,item))

new_name="Bro"
print("Hello, my name is {}".format(new_name))
print("Hello, my name is {:10}. Nice to meet you".format(new_name))
print("Hello, my name is {:<10}. Nice to meet you".format(new_name))
print("Hello, my name is {:>10}. Nice to meet you".format(new_name))
print("Hello, my name is {:^10}. Nice to meet you".format(new_name))


