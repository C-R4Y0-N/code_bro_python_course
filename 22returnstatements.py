#return statement = Functions send Python values/object back to the caller. Thes values are know as the function's return value

def multiply (number1,number2):
    return number1 * number2

a=int(input("Ingress a number:"))
b=int(input("Ingress another number:"))
x = multiply(a,b)
print(x)

#Other way:
#deg multiply (number1, number2)
    #result = number1* number2
    #return result

#print(multiply(6,8))
