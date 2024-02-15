dict1 = {'vendor': 'cisco', 'model':"2600", 'IOS':'12.4', 'Ports':'4'}
d1 = {1:'first elemente', 2: 'second element'}

print(len(d1) == 2)

print(d1[2])

dict1['RAM'] = '256'
print(dict1)


print(dict1.keys())
print(dict1.values())
print(dict1.items())

