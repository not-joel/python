# I/O with basic files

my_file = open('myfile.txt') # default - 'r' read
my_file = open('myfile.txt', 'w')
my_file.write('Hello World')
my_file.close()
# my_file = open('wrong_file.txt')
print(my_file.read())
print('--->', my_file.read())
my_file.seek(0)
print(my_file.read())
my_file.seek(0)
print(my_file.readline())
my_file.seek(0)
print(my_file.readlines())

my_file.close()

# alternate ways for:
my_file = open('myfile.txt')

with open('myfile.txt') as my_new_file:
    contents = my_new_file.read()
    
# no need to worry about close()
print('CONTENTS -->', contents)

# write
with open('myfile1.txt', mode='+w') as new_file:
    new_contents = new_file.read()
    new_file.write('FOURTH LINE')

# append
with open('myfile1.txt', mode='+a') as new_file:
    new_contents = new_file.read()
    new_file.write('\nFIFTH LINE')
    
with open('myfile1.txt', mode='r') as new_file:
    new_contents = new_file.read()
    print('READ ---->', new_contents)

print('NEW_FILE:', new_contents)

with open('sample.txt', mode='w') as f:
    f.write('FOURTH LINE')
