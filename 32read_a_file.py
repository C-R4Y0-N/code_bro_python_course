try: 
    with open('texto.txt') as file:
        print(file.read())
except FileNotFoundError:
    print("Eso archivo no existe chamaco tonto")