new_file = open('my_file.txt', 'x')
new_file.close()

import os
print('check if my file exist or not...')
if os.path.exists('my_file.txt'):
    os.remove('my_file.txt')
    print("my_file.txt,is removed")
else:
    print("my_file.txt, does not exist")

my_file = open('my_file.txt', 'w')
my_file.write("Hello! This is a sample file.\n")
my_file.close()