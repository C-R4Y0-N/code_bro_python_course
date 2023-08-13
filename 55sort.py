#sort() method = used with lists
#sort() function = used with iterables

#students = ["Miguel","Zapato","Gabriel","Julian","Perro"]

#students.sort()
#
#for i in students:
#    print(i)
#    
#students.sort(reverse=True)
#
#for i in students:
#    print(i)
#students = ("Miguel","Zapato","Gabriel","Julian","Perro")
#sorted_students = sorted(students)
#sorted_students = sorted(students,reverse=True)
#for i in sorted_students:
#    print (i)

#students = [("Julian","F",60),("Zapato","A",33),("Gabriel","D",36),("Miguel","B",20),("Perro","C",78)]
#
#grade = lambda grades:grades[0]
#students.sort(key=grade)
#
#for i in students:
#    print(i)
#    
#grade = lambda grades:grades[1]
#students.sort(key=grade)
#
#for i in students:
#    print(i)
#
#grade = lambda grades:grades[2]
#students.sort(key=grade)
#
#for i in students:
#    print(i)
students = (("Julian","F",60),("Zapato","A",33),("Gabriel","D",36),("Miguel","B",20),("Perro","C",78))
age = lambda age:age[2]
sorted_students = sorted(students, key=age)
for i in sorted_students:
    print(i)