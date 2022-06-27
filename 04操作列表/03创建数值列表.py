
#函数range()让Python从你指定的第一个值开始数，并在到达你指定的第二个值后停止，因此输出不包含第二个值（这里为5）
for value in range(1, 5):
    print(value)

print()
for value in range(6):
    print(value)


numbers = list(range(5))
print(numbers)

numbers = list(range(2, 11, 2))
print(numbers)

list1 = []
for number in range(1, 11):
    list1.append(number ** 2)
print(list1)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))


list2 = [value**2 for value in range(1,11)]
print(list2)

#例子：
for value in range(1, 21):
    print(value, end=",")

print()
list3 = [value for value in range(1, 1000000)]
print(max(list3))
print(min(list3))
print(sum(list3))

#奇数
list4= [value for value in range(1, 20, 2)]
print(list4)

list5 = [value for value in range(3, 31, 3)]
print(list5)

#立方
list6 = [value**3 for value in range(1, 11)]
print(list6)



