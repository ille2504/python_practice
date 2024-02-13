mystring = "mystring"

my_string = '''
hello\
my\
name\
is\
string'''

string_1 = 'cisco router'

print(string_1[6])

print(len(string_1))


a = "Cisco Router"

print(a.find('o'))

b = "   mario "

print(b.strip())

c = " ma r i o"
print(c.replace(" ", ""))

d = 'Juniper,Cisco,HP,Avaya,Goto'

print(d.split(","))

print('_'.join(a))

m = 'cisco'
n = 'router'

print(m + n)

print("o" in m)

x = 'my name is %s my age is %d my weight is %.1f' % ('mario', 35, 160.5)
print(x)

y = 'my name is {} my age is {} my weight is {}'.format('mario', 35, 160.5)
print(y)


model = '2004MX'
slot = 4
ios = 12.4

print(f'cisco model: {model}, with {slot} slots, and the ios is {ios}')

slice = 'se/pythontutorial/learn/lecture/11804310#overview'

print(slice[3:17])