# functions
#DRY : Don't Repeat Yourself

# pass means to leave func free for now
def hello_func():
  pass

# exec func
hello_func()

print(hello_func)  # prints locations of a func

print(hello_func()) # display result of a func

def hello_func():
  print('hello, func')

hello_func()  # prints hello, func

#DRY : Don't Repeat Yourself

def hello_func():
  return 'hello, world'  # returns a value which can be assigned to a variable later

print(hello_func().upper())  # chaining is possible when function returns a value

# parameters in func
def hello_func(greeting):
  return f'{greeting}'

hello_func('hello, func')

# default parameters
def hello_func(greeting, name = 'JR'):
  return f'{greeting}, {name}'

print(hello_func('Hello'))  # displays w/ default name = 'JR'
print(hello_func('Hi', name = 'Mhmmd'))  # default values can be changed

# positional args have to come before keyword arguments
# accept any number of them w/ *

def student_info(*args, **kwargs):
  print(args)
  print(kwargs)

student_info('math', 'logic', name='bakr', age=20)

# unpacking args and kwargs
courses = ['math', 'logic']
info = {'name' : 'bakr', 'age' : 20}

student_info(*courses, **info)

# docstrings go after func definition
# are in triple quotes `"""`
# explains what a func does in man page

def hello_world():
  """Prints Hello, World!"""
  print('Hello, World!')
