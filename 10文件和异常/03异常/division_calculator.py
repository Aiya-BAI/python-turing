try:
    print(5/0)
except ZeroDivisionError:
    print('you can not divide by zero')

print('Give me two numbers, and i will divide them.')
print('Enter q to quit')

while True:
    first_nember = input('\nFirst Number:')
    if first_nember == 'q':
        break
    second_number = input('Second Number:')
    if second_number == 'q':
        break
    answer = int(first_nember) / int(second_number)
    print(answer)