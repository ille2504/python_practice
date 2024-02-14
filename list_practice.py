list = ['cisco', 'hp', 'avaya', 10, 10.5, -11]
list1 = [100, 99, 88, 35, 400, 1, 34]
list2 = [59, 90, 88, 76, 34, 12, 1]
print(len(list))
print(list[1])
list[1] = 'Asterisk'


list.append("HP")

del list[3]
list.pop(5)
list.remove('cisco')
list.insert(3, 'Cisco')
list.extend(list1)
list1.sort()
print(list1)
list1.reverse()
print(sorted(list2))
print(sorted(list2, reverse = True))
print(list1)
print(list)

total = list + list1
print(total)

var = ['cisco', 'hp', 'avaya', 'HP', 'Asterisk']

print(var[0:3])