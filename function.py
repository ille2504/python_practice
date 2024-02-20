x = "hello everybody"

def myfirst_function(x):
    'hello function for help'
    print(x)

myfirst_function(x)


def mysecond_function(x, y):
    print('hello ' + x )
    print('hello ' + y)

mysecond_function('python', 'java')

def my_sum(x, y, z):
    res = (x + y) * z
    return res 
    

print(my_sum(x = 1, y = 2, z = 3))

def my_func(x, *args):
    print(x)
    for i in args:
        print(i)

my_func('hello', 'bye', 'chao')

def my_func1(**kwarg):
    print(kwarg)

my_func1(James = 1, Mario = 2)


def my_func2():
    global my_var
    my_var = 10
    print(my_var)

my_func2()
my_var = 20
print(my_var * 10)

import syntax_error

print('hola')

print(syntax_error.my_var_mo)

print(syntax_error.my_function())