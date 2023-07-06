#set = collection which is unordered, unindexed. No duplicate values

utensiles = {"fork","spoon","knife"}
dishes = {"bowl","plate","cup","knife"}
#print(utensiles)
#print(dishes)
utensiles.add("napkin")
#print(utensiles)
utensiles.remove("fork")
#print(utensiles)
#utensiles.clear()
#print(utensiles)
##dishes.update(utensiles)
##print(dishes)
dinner_table = utensiles.union(dishes)
#print(dinner_table)
print("Utensiles:")
for x in utensiles:
    print(x)
print("Dishes:")
for x in dishes:
    print(dishes)
print("Dinner table:")
for x in dinner_table:
    print (dinner_table)
print(utensiles.difference(dishes))
print(dishes.difference(utensiles))
print(utensiles.intersection(dishes))