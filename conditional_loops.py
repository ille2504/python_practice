x = 5
if x > 5:
    print("yes it is, let's double it")
    print( x * 2)
elif x < 5:
    print("no is not")
else:
    print("add a number")
#-----------------------------------
var = ['cisco', 'hp', 'avaya', 'HP', 'Asterisk']
for i in var:
    print(i)

str1 = 'Cisco'
for i in str1:
    print(i)

r = 10
for i in range(r):
    print(i)

for elem in range(len(var)):
    print(var[elem])

for index, element in enumerate(var):
    print(index, element)

for element in var:
    print(element)
else:
    print('for loop finished')
#-----------------------------------
    
x = 1
while x <= 10:
    print(x)
    x += 1

#while True:
#    print('in loop')

y = 'Cisco'
if 'i' in y:
    if len(y) > 3:
        print(y, len(y))

hi = [1, 2, 3]
bye = [2, 3 ,4]

for i in hi:
    for j in bye:
        print(i * j)

x = 1
while x <= 10:
    z = 5
    x += 1
    while z <= 10:
        print(z)
        z += 1

for i in range(10):
    if i >= 7:
        break
    print(i)
print('--------------')
hi = [1, 2, 3]
bye = [10, 20 ,30]

for i in hi:
    print('value of i is:', i)
    for j in bye:
        print('value of j is:', j)
        if j == 20:
            print('before continue')
            break
        print(i * j)
    print('outside the loop inside')

for i in range(10):
    pass 

for i in range(5):
    try:
        print(i/0)
    except ZeroDivisionError as e:
        print(e, 'cero division exception')

j = 0
for i in range(5):
    try:
        print(i/j)
    except ZeroDivisionError as e:
        print(e, 'cero division exception')
    print('code finished')



j = 1
for i in range(5):
    try:
        print(i/j)
    except ZeroDivisionError as e:
        print(e, 'cero division exception')
    except NameError:
        print('name error')
    except ValueError:
        print('value error')
    finally:
        print('code finished')

a = 3
b = 0
try:
    print(a/b)
except ZeroDivisionError:
    print('not allowed')
finally:
    print('program end')

            

