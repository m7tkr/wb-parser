# this is the list

courses = ['english', 'math', 'history']
courses_2 = ['art', 'logic']
nums = [1, 65, 3, 900]
print(len(courses)) 

# numbering starts from 0
# -1 starts counting from back

print(courses[0])

# selecting range with `:`
# 1st item inclusive 
# 2nd is not

print(courses[0:2])  # selects from 1st, 2nd but not 3rd

print(courses[:2])  # same as above

print(courses[2:])  # from 3rd included way to the end

courses.append('Art')  # append to the end

courses.insert(0, 'Logics')  # insert into specific loca

courses.insert(0, courses_2)  # insert list into list

courses.extend(courses_2)  # take list as an argument to insert its values into another list

courses.remove('math')  # remove item from list

popped = courses.pop()  # by default pops last item from list; pop returns the values which it popped
print(popped)

courses.reverse()  # reverses list items

courses.sort()  # by def sort in abc order
courses.sort(reverse=True) # sorts in xyz order
nums.sort()  # sorts nums in ascending order
print(courses, nums)

sorted_courses = sorted(courses)  # orig list remains unsorted, new sorted list returned
print(sorted_courses)

print(min(nums))  # returns min number in list
print(max(nums))
print(sum(nums))  # sum of numbers in list 

print(courses.index('math'))  # find position of 'math' in list

# use of in operator; true/false

print('math' in courses)

# loop throught items in list

for item in courses:
  print(item)

courst_str = ', '.join(courses)  # creates strng out of list items separated by ', '

new_list = courst_str.split(', ')  # returns new list out of string being splitted in ' - '

# lists are mutable

list_1 = ['history', 'lang', 'rhetorics']
list_2 = list_1

print(list_1)
print(list_2)

list[0] = 'art'

print(list_1)
print(list_2)  # list_2 will follow list_1 changes

# tuples are immutable

tuple_1 = ('history', 'math', 'logic')  # this is immutable

tuple_1[0] = 'litre'  # this throws an error because tuples are immutable
 
# sets are unordered AND have no duplicates

set_1 = {'math', 'chemistry', 'physics'}
print(set_1)  # prder will change w/ each x
 
# sets r used for: 
# (1) test whether value is part of set (membership test)
# (2) remove duplicate values

set_2 = {'john', 'mhmmd', 'bakri', 'mhmmd'}
set_3 = {'kate', 'faysal', 'mhmmd'}

print(set_2)  # second 'mhmmd' won't display in set
print ('math' in set_1)  # sets are the best optimized for mship test

print(set_2.intersection(set_3))  # displays what is common in both sets
print(set_2.difference(set_3))  # displays what is diff in both sets
print(set_2.union(set_3))  # displays union of both sets

# empty list
empty_list = []
empty_list = list()

# empty tuple
empty_tuple = ()
empty_tuple = tuple()

# empty set
empty_set = {}  # this isn't set, but a dict
empty_set = set()  # this is a set
