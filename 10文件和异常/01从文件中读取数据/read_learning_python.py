filename = 'learning_python.txt'

with open(filename) as file_object:
    contents = file_object.read()
print(contents)

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip)

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip())


print('-============================================')
with open(filename) as file_object:
    messages1 = file_object.readlines()
    print(type(messages1))
    print(messages1)
    messages2 = file_object.read()
    print(type(messages2))
    print(messages2)
    messages3 = file_object.readline()
    print(type(messages3))
    print(messages3)


for message in messages1:

    print(message.strip().replace('python', 'C'))
