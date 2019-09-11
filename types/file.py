""" Files
Unicode processing mostly reduces to transferring text data to and from files—text is encoded to bytes when stored in a file, and decoded into characters (a.k.a. code points) when read back into memory. Once it is loaded, we usually process text as strings in decoded form only.

Files are buffered and seekable

By default, output files are always buffered, which means that text you write may not be transferred from memory to disk immediately—closing a file, or running its flush method, forces the buffered data to disk. You can avoid buffering with extra open arguments, but it may impede performance. Python files are also random-access on a byte offset basis—their seek method allows your scripts to jump around to read and write at specific locations.

close is often optional: auto-close on collection

Calling the file close method terminates your connection to the external file, releases its system resources, and flushes its buffered output to disk if any is still in memory. As discussed in Chapter 6, in Python an object’s memory space is automatically reclaimed as soon as the object is no longer referenced anywhere in the program. When file objects are reclaimed, Python also automatically closes the files if they are still open (this also happens when a program shuts down). This means you don’t always need to manually close your files in standard Python, especially those in simple scripts with short runtimes, and temporary files used by a single line or expression.

On the other hand, including manual close calls doesn’t hurt, and may be a good habit to form, especially in long-running systems. Strictly speaking, this auto-close-on-collection feature of files is not part of the language definition—it may change over time, may not happen when you expect it to in interactive shells, and may not work the same in other Python implementations whose garbage collectors may not reclaim and close files at the same points as standard CPython. In fact, when many files are opened within loops, Pythons other than CPython may require close calls to free up system resources immediately, before garbage collection can get around to freeing objects. Moreover, close calls may sometimes be required to flush buffered output of file objects not yet reclaimed. For an alternative way to guarantee automatic file closes, also see this section’s later discussion of the file object’s context manager, used with the with/as statement in Python 2.6, 2.7, and 3.X.
"""

import sys

file_name = 'data/data.txt'

# write to file
f = open(file_name, 'w')       # Make a new file in output mode ('w' is write)
f.write('Hello world!\n This is a great time to be alive!')             # Write strings of characters to it
f.close()                      # Close to flush output buffers to disk

# read from file
f = open(file_name)           # 'r' (read) is the default processing mode
print('Following is the content of the file - \n', f.read())      # Read entire file into a string

# iterate through each line in the file
for line in open(file_name): print("Line : " + line)

# iterate through file char by char
file = open(file_name)
while True:
    char = file.read(1)         # Read by character
    if not char: break          # Empty string means end-of-file
    print(char, end='')        # Line already has a \n


print(dir(f))

# Redirecting streams
print("test", "test1", "test2", sep='...', end='\n', file=open('data/outPutData.txt', 'w'))

temp = sys.stdout
sys.stdout = open('data/outPutData.txt', 'a')       # Redirects prints to a file
print('print this out in file')
sys.stdout.close()            # Flush output to disk
sys.stdout = temp

print('Will output to the standard output/console and NOT the file')
