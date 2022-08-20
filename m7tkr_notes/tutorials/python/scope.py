'''
LEGB
Local, Enclosing, Global, Built-in
'''

import builtins

print(dir(builtins))

# built-in ex
list = [34, 342, 12, 55]


def min():
    ''' this overwrittes python builtins func min()
    so be carefull, further uses of min will throw an
    error'''

    pass


# print(min(list))  # min is python built-in

# here is a global scope
x = 'global x'


# local scope inside function
def test():
    # global x  # tells python we're working w/ global x
    # don't use global too much, makes code hard to read
    y = 'local y'  # var y lives only inside test()
    x = 'local x'  # new local var x, global x is not overwritten
    print(y)
    print(x)


test()
# print(y)  # err cause no y is defined in global, but locally in test()
print(x)  # okay cause x is define in global


# another local scope ex
def test(z):
    print(z)


test('local z')


# enclosing
def outer():  # this func is enclosing to inner()
    x = 'outer x'

    def inner():
        nonlocal x  # same as global x in non-enclosing funs
        x = 'inner x'
        print(x)

    inner()
    print(x)


outer()
