#nested loops = The "inner loop" will finish all of it's iteration before finishing one iteration of the "outer loop"
rows=int(input("How many rows: "))
columns=int(input("How many columns: "))
symbol=input("Select a symbol: ")
for i in range (rows):
    for i in range (columns):
        print(symbol,end="")
    print ()