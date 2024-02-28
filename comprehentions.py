list1 = []
for i in range(10):
    list1.append(i)
print(list1)

list2 = [i for i in range(10)]
print(list2)

list3 = [i ** 2 for i in range(10) if i >5]
print(list3)

set1 = {i for i in range(10)}
print(set1)

dict1 = {i : i for i in range(10)}
print(dict1)

print(list(i * 10 for i in range(11) if i >= 7))


a = lambda x, y : x * y 
print(a(2, 10))

b = lambda mylits: [x * y for x in range(10) for y in range(5)] + mylits
print(b([100, 101, 102]))

def product(a):
    return a * 10

r1 = range(10)

print(list(map(product, r1)))

from itertools import *

list1 = [1, 2, 3, 'a', 'b', 'c']
list2 = [101, 102, 103, 'x', 'y', 'z']

print(list(chain(list1, list2)))

for i in count(10, 2.5):
    if i < 50:
        print(i)
    else:
        break

print(list(islice(range(10), 2, 9, 2)))


def my_decorator(target_function):
    def function_wrapper():
        return "Python is: " + target_function()
    return function_wrapper

@my_decorator
def target_function():
    return 'cool'

print(target_function())

