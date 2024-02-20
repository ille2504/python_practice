myfile = open('/Users/jmillescas/python_practice/info.txt', 'r')
print(myfile.mode)
a = myfile.read().split('\n')
print(list(a))
myfile.seek(0)
print(myfile.read(5))
myfile.seek(0)
print(myfile.readlines())
myfile.seek(0)
for i in myfile.readlines():
    print(i)


newfile = open('/Users/jmillescas/python_practice/info2.txt', 'w+')
newfile.write('appending info \nin the info2.txt again')
newfile.close()

newfile = open('/Users/jmillescas/python_practice/info2.txt', 'a+')
newfile.write('\nread and write test \n')
newfile.close()

print(newfile.closed)

with open('/Users/jmillescas/python_practice/info2.txt', 'w+') as f:
    f.write('hello python')