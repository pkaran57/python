# Files
# Unicode processing mostly reduces to transferring text data to and from files—text is encoded to bytes when stored in a file, and decoded into characters (a.k.a. code points)
# when read back into memory. Once it is loaded, we usually process text as strings in decoded form only.

f = open('data/data.txt', 'w')       # Make a new file in output mode ('w' is write)
f.write('Hello world!\n This is a great time to be alive!')             # Write strings of characters to it
f.close()                      # Close to flush output buffers to disk

f = open('data/data.txt')           # 'r' (read) is the default processing mode
print('Following is the content of the file - \n', f.read())      # Read entire file into a string

for line in open('data/data.txt') : print("Line : " + line)

file = open('data/data.txt')
while True:
    char = file.read(1)         # Read by character
    if not char: break          # Empty string means end-of-file
    print(char)

print(dir(f))

# Redirecting streams

print("test", "test1", "test2", sep='...', end='\n', file=open('data/outPutData.txt', 'w'))

temp = sys.stdout
sys.stdout = open('data/outPutData.txt', 'a')       # Redirects prints to a file
print('print this out in file')
sys.stdout.close()            # Flush output to disk
sys.stdout = temp