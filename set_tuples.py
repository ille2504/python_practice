listr = ['cisco', 'hp', 'avaya', 'HP', 'Asterisk']

new_set = set(listr)
print(new_set)

print('avaya' in new_set)

set1 = {1, 4, 78, 90, 45}
set2 = {67, 45, 34}

print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.union(set2))
set1.pop()
print(set1)

list1 = [100, 99, 88, 35, 400, 1, 34]
list2 = [59, 90, 88, 76, 34, 12, 1]

fro1 = frozenset(list1)
fro2 = frozenset(list2)

print(fro1)

my_tuple = (1, 4, 6, 9, 23, 35)
print(my_tuple)

print(my_tuple.count(1))

tuple1 = ('cisco', '2600', '12.4')
(vendor, model, IOS) = tuple1

print(vendor)

(a, b, c) = (1, 2, 3)
print(a)

r = range(10)
print(list(r))

print(list(r)[2:5])

r1 = range(10, 100, 10)

print(list(r1).index(30))