fn = open('Codingal.txt', 'r')
fn1 = open('CodingalUpdated.txt', 'w')

cont = fn.readlines()
print(cont)
for i in range(1, len(cont)+1):
    if(i % 2 != 0):
        fn1.write(cont[i-1])


fn1.close()

fn1 = open('CodingalUpdated.txt', 'r')
cont1 = fn1.read()
print(cont1)
fn.close()
fn1.close()