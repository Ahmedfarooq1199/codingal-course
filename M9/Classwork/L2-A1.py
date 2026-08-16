file = open('Codingal.txt','r')
print(file.read())
file.close()

file = open('Codingal.txt','r')
print("\nRead in parts \n")
print(file.read(8))
file.close()

file = open('Codingal.txt','a')
file.write("\n Hi! I am a koala. I am 3 years old.")
file.close()
