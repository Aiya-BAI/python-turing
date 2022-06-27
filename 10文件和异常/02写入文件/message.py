filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write('i love sunjingyao\n')
    file_object.write('i love sunjingyao\n')

with open('guest.txt', 'a') as file_object:
    file_object.write(f"{input('input your name:')}\n")

with open('guest_book.txt', 'a') as file_object:
    while True:
        name = input('input your name:')
        if name == 'exit':
            break
        else:
            file_object.write(f'{name}\n')
