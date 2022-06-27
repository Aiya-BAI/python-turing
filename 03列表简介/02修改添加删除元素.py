motorcycles = ['honde', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

#方法append()将元素'ducati'添加到了列表末尾
motorcycles.append('ducati')
print(motorcycles)

motorcycles2 = []
motorcycles2.append('honde')
motorcycles2.append('yamaha')
motorcycles2.append('suzuki')
print('\t')
print(motorcycles2)

#使用方法insert()可在列表的任何位置添加新元素
#方法insert()在索引1处添加空间，并将值'ducati'存储到这个地方。这种操作将列表中既有的每个元素都右移一个位置
motorcycles2.insert(1, "ducati")
print(motorcycles2)

#使用del可删除任何位置处的列表元素，条件是知道其索引
del motorcycles2[1]
print(motorcycles2)

#pop的使用，列表末端元素删除但是能够
#如果你要从列表中删除一个元素，且不再以任何方式使用它，就使用del语句；如果你要在删除元素后还能继续使用它，就使用方法pop()
print()
pop_motorcycle = motorcycles2.pop()
print("最后一辆摩托车是：" + pop_motorcycle)
print(motorcycles2)
pop_motorcycle1 = motorcycles2.pop(0)
print("第一辆摩托车是：" + pop_motorcycle1)

#remove()
#方法remove()只删除第一个指定的值。如果要删除的值可能在列表中出现多次，就需要使用循环来判断是否删除了所有这样的值
print()
print(motorcycles)
remove_motor = "yamaha"
motorcycles.remove(remove_motor)
print(motorcycles)


#例子 邀请三人公共进晚餐

guests = ["爸爸", "妈妈", "爷爷","奶奶"]
print("我想邀请" + guests[0] + "共进晚餐")
print("我想邀请" + guests[1] + "共进晚餐")
print("我想邀请" + guests[-2] + "共进晚餐")
print("我想邀请" + guests[-1] + "共进晚餐")
print()

print(guests[3] + "不能赴约")
del guests[3]
guests.append("二姐")
print("列表已更新" )
print(guests)

print()
print("找到了一个更大的餐桌")
guests.insert(0,"大姐")
guests.insert(2,"静瑶")
guests.append("韩磊")
print(guests)
print()

del1 = guests.pop()
print("很遗憾不请你了 " + del1)
del2 = guests.pop()
print("很遗憾不请你了 " + del2)
del3 = guests.pop()
print("很遗憾不请你了 " + del3)
del4 = guests.pop()
print("很遗憾不请你了 " + del4)
print(guests)

print()
del guests[2]
del guests[1]
del guests[0]
print(guests)







