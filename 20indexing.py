#index operator [] = gives access to a sequence's element (str,list,tuples)

name = "bro code!"

if(name[0].islower()):
    name=name.capitalize()
    
print(name)

frist_name=name[:3].upper()
last_name = name[4:].lower()
last_character = name[-1]

print(frist_name)
print(last_name)
print(last_character)