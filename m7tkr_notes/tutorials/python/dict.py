# this is a dict
# value may be any data type

student = {'name' : 'John', 'age' : 25, 'courses' : ['math', 'science']}

print(student['name'])  # access specific key

print(student['phone'])  # will return an error
print(student.get('phone'))  # return 'None' instead of an error
print(student.get('phone', 'Not Found'))  # return 'Not Found' instead of 'None'

student['phone'] = '1234-5678'  # creates new dict key value pair
student['name'] = 'mhmmd'  # will update existing dict key value

# update multiple values at a time
student.update({'name' : 'bakr', 'courses' : ['fikh', 'hadith']})

# delete key / value
del student['age']

age = student.pop['age']  # pops age key and returns it into var
print(age)

print(len(student))  # length of dict
print(student.keys())  # prints all of the keys of dict
print(student.values())  # prints all of the values of dics
print(student.items())  # prints keys and values

# looping thrgh dics keys
for key in student:
  print(key)  # prints only dict keys

# looping thrgh keys and values
for key, value in student.items():
  print(key, value) 
