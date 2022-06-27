with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)

print(contents.strip())


with open('C:\\Users\\BAI\\Desktop\\ceshi.txt') as file:
    content = file.read()
print(f'{content}\n')


filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.strip())


print('==========================================')
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip())



