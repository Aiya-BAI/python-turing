prompt = 'if you tell us who you are, we can personalize the messages you see.'
prompt += '\nWhat is your first name: '

name = input(prompt)
print(name)


age = input('How old are you? ')
print(age)
print(type(age))

age = int(age)
print(type(age))


#10的整数
number = int(input("输入一个数："))
if number%10 == 0:
    print('这个数是10的整数')
else:
    print(f"{number}不是10的整数")

