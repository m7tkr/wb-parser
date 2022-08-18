# loops and iterations

nums = [1, 3, 4, 6, 7]

for num in nums:  # w/ each iteration num is different
  print(num)

# break : gets you out of the loop when condition is met
for num in nums:
  if num == 3: 
    print('Found')
    break
  print(num)

# continue : skips to the next iteration of the loop
for num in nums:
  if num == 3: 
    print('Found')
    continue
  print(num)

# loop inside loop
# sometimes time consuming
for num in nums:
  for letter in 'abs':
    print(num, letter)

# range()
for i in range(10):
  print(i)  # starts from 0, 10 is not included

for i in range(1, 10):  # starts from 1, 10 not included
  print(i)

# for loop : iterates over each item
# while loop : iterates while condition is TRUE, or break
x = 0

while x < 10:
  print(x)
  x += 1

# break is possible within while loop
while x < 10:
  if x == 5:
    break
  print(x)
  x += 1

# infinite loop
# Ctrl-C to get out
while True:
  print(73)
