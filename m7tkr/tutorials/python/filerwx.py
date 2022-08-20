# file objects

# r : open for reading
# w : open for writing
# a : open for appendind
# r+ : open for reading and writing
# rb : read image in binary
# wb : write image in binary

f = open('./filedir/lorem.txt', 'r')  # default is 'r'

print(f.name)
print(f.mode)

f.close()  # we have to close files after we're done

# context mananger automatically closes file, you don't have to worry about it
# work w/ file within cont mngr
with open('./filedir/lorem2.txt', 'r') as f2:
    f2_contents = f2.read()
    # f2.readlines : returns list with items as single lines of a file
    # f2.readline : returns the first line of a file, repeating returns the 2nd
    # line
    print(f2_contents)  # add end='' if you see blank line

    # ---------------------------
    for line in f2:
        ''' this iterates over file lines'''

        print(line, end='')
    # ---------------------------

    # ---------------------------
    size_to_read = 10  # specify in var to not overload memory
    # f2.read(size_to_read)  # read only 1st 100 chars of a file

    while len(f2_contents) > 0:
        print(f2_contents, end='')
        f2_contents = f2.read(size_to_read)
    # -------------------------

    # ---------------------------
    f2_contents = f2.read(size_to_read)
    print(f2_contents)

    f2.seek(0)  # this jumps to beginning of the file, specify whatever u want

    f2_contents = f2.read(size_to_read)
    print(f2_contents)  # won't pick up leftover due to seek()
    # ---------------------------

# f2.read()  # err cause cont mngr already closed file

with open('./filedir/lorem3.txt', 'w') as f3:
    # if no file in dir, new will be created

    f3.write('loremipsum')
    f3.seek(0)
    f3.write('ipsumlorem')  # this will overwrite what was before due to seek

with open('./filedir/lorem4.txt', 'r') as f4:
    with open('./filedir/lorem4_copy.txt', 'w') as fw4:
        for line in f4:
            fw4.write(line)
