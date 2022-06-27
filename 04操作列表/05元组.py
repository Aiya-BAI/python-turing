dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#元组不支持修改'tuple' object does not support item assignment
#dimension[0] = 30

test1 = (1)
print(test1)
test2 = (1,)
print(test2)


for dimension in dimensions:
    print(dimension)

#给元组变量赋值是合法的
dimensions = (400, 50)
print(dimensions)


#例子：自助餐
foods = ('tomato', 'banana', 'potato', 'beer', 'apple')
print()
for food in foods:
    print(f'{food}')
foods = ('pear', 'banana', 'chicken', 'beer', 'apple')
print(foods)






