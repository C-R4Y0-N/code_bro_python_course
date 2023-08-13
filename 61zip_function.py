#zip(iterables) = List,tuples,stes,etc

usernames = ["Dude","Bro","Mister"]
passwords = ["p@ssword","abc123","guest"]
login_date = ["1/1/2021","1/2/2021","1/3/2023"]

users = zip(usernames, passwords,login_date)

for i in users:
    print (i)