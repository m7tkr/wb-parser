# conditionals

# `==` means equality
# `is` checks for object identity

# this will print
if True:
  print('condit was true')

#this won't print
if True:
  print('condit was true')

language = 'Python'

if language == 'Python':
  print('lang is python')
elif language == 'Jave':
  print('lang is java')
else:
  print('no match')

# boolean operations
# and : each has to be true
# or : one or the other have to be true
# not : swtich Boolean to opposite

user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
  print('admin page')
else:
  print('bad creds')

if not logged_in:  # evaluates to false
  print('not logged in')
else:
  print('bad attempt')

# object identity `is` vs equal `==`
# two objects can be equal and be the same objects in memory
# two objects can be equal and be diff objects in memory 

a = [1, 2, 3]
b = [1, 2, 3]
# b = a

print(id(a))
print(id(b))
print(a is b)  # false
# print(id(a) == id(b))
print(a == b)  # true

# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.

condition = False

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')
