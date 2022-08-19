# Tue 16 Aug 2022 15:05:31 MSK

message = 'hello world'
greeting = 'Hello, Terra\'form'
greeting_2 = "Hello, Terra'form"
msg_2 = """Print
exact"""

# access index from to
print(len(msg_2[0:5]))

# we allowed to leave start/end indecies
print(msg_2[:5])
print(msg_2[5:])

# applying methods
print(msg_2.lower())
print(msg_2.count('print'))
print(msg_2.find('print'))
print(message.replace('world', ', earth'))

# concat
msg_3 = message + msg_2

# using format
msg_4 = '{}, {}. Welcome!'.format(message, msg_2)

# using f-string
msg_5 = f'{message.upper()}, {msg_2}. Hello, again'

print(dir(message))  # show available methods
print(help(str.lower))  # run on class and gives bigger output
