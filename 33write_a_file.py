text = "When eres:\nSoy "

with open('testo.txt','w') as file:
    file.write(text)
    
# add text

text = "\nBut NO "

with open('testo.txt','a') as file:
    file.write(text)