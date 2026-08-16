with open('Codingal.text', 'w') as file:
    file.write("Hi! I am penguin and i love to code.\n")
    file.write("Hi! I am penguin")


with open('Codingal.text', 'r') as file:
    data = file.readlines()
    print(data)
    print("Words in this files are....")
    for line in data:
        print(line)
        word = line.split()
        print (word)