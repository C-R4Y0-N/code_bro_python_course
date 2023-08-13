#squares = []
#for i in range (1,11):
#    squares.append(i * i)
#print(squares)

#now with list comprehesion
#list = [expression for item in iterable]

#squares = [i * i for i in range (1,11)]
#print(squares)
#------------------------------------------------------
#students = [100,90,80,70,60,50,40,30,0]
#passed_students = list(filter(lambda x: x>=60, students))
#print(passed_students) 

#now with list comprehesion
#list = [expression (if/else) for item in iterable]

students = [100,90,80,70,60,50,40,30,0]
#passed_students=[i for i in students if i>=60]
passed_students=[i if i >= 60 else "FAILED" for i in students]
print(passed_students)