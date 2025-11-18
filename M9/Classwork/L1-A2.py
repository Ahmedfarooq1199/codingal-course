file_read = open('Codingal.txt', 'r')
print("file in read mode -")
print (file_read.read())
file_read.close()

file_write = open('Codingal.txt', 'w')
file_write.write("file in write mode ....")
file_write.write("Hi! I am penguin. I am 1 year old.")
file_write.close()


file_append = open('Codingal.txt', 'a')
file_append.write("\nfile in append mode ....")
file_append.write("hi! I am panda. I am 2 years old.")
file_append.close()