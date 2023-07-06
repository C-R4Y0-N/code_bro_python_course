#nested function calls: function calls inside other functions calls innermost functioncs calls are resolved frist returned value is used as argument for the next outer function

#num = input("Enter a whole positive number: ")
#num = float(num)
#num = abs(num)
#num = round(num)
#print(num)

print(round(abs(float(input("Enter a whole positive number")))))