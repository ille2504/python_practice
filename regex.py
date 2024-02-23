import re

mystr = 'You can lear any programming language you want, some of them are: Phyton2, Phyton3, Java, JavaScript or PHP'

a = re.match('You', mystr)
print(a)
print(a.group())
a = re.match('you', mystr, re.I)
print(a.group())

arp = '192.168.1.2      0     00-0c-29-63-af-d0 vlan#22   L'
b = re.search('00', arp)
print(b.group())
b = re.search(r"(.+?) +(\d) +(.+?)\s{2,}(\w)*", arp)
print(b.group(0))
print(b.group(1))
print(b.group(2))
print(b.group(3))
print(b.group(4))
print(b.groups())
