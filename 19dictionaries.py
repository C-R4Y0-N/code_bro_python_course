#dictionary = A changable, unordered collection of unique key: value pairs Fast because they use hashing, allow us to success a value quickly 
capitals={
    'Usa':'Washinton DC',
    'India':'New Delhi',
    'China':'Benjing',
    'Rusia':'Moscow',
    }

print(capitals['China'])
print(capitals['India'])
print(capitals['Rusia'])
print(capitals['Usa'])
#print (capitals.get['Germany'])
print(capitals.keys())
print(capitals.values())
print(capitals.items())
for key,value in capitals.items:
    print(key, value)
capitals.update({'Germany':'Berlin'})
capitals.update({'Usa':'Las Vegas'})
capitals.pop('China')
for key,value in capitals.items:
    print(key, value)
capitals.clear()