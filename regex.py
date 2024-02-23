import re

mystr = 'You cant lear any programming language you want, some of them are: Phyton2, Phyton3, Java, JavaScript or PHP'

a = re.search(r'^\w{3}\s\w{4}', mystr)
print('this: ' ,a)


a = re.search(r'PHP\Z', mystr)
print(a)

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

a = re.findall(r"\d\d\.\d{2}\.[0-9][0-9]\.[0-9]{1,3}", arp)

b = re.sub(r"\d" , "7", arp)
print(b)

regex_str = "123.456.789   0 PYTHON 3"
regex = re.sub(r"(.+?)\s\s[0-1]\s\w{6}\s[0-9]$", "%", regex_str)

print(regex)