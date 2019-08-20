# Exception Handling

try:
    int('XYZ')
except:
    print('XYZ is not an int!')
else:
    print('This will run if no exception raised')