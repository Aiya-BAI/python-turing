#sort()让你能够较为轻松地对列表进行排序,按字母,永久的
cars = ["bwm", "audi", "benc", "toyota"]
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

#sorted  保留原来的
print()
cars2 = ["bwm", "audi", "benc", "toyota"]
print("this is original list : ")
print(cars2)
print("this is sorted list : ")
print(sorted(cars2))
print("this is original list: ")
print(cars2)

#倒着打印,reverse()永久性地修改列表元素的排列顺序,可随时恢复到原来的排列顺序
print()
cars3 = ["bwm", "audi", "benc", "toyota"]
print(cars3)
cars3.reverse()
print(cars3)

#列表长度，Python计算列表元素数时从1开始，因此确定列表长度时，你应该不会遇到差一错误
print(len(cars3))
print()

#例子
areas = ["lijiang", "sanya", "zhangjiakou", "chongqing", "chengdu"]
print(sorted(areas))
print(sorted(areas, reverse=True))#传参
print(areas)
print()

areas.reverse()
print(areas)
areas.reverse()
print(areas)
print()

areas.sort()
print(areas)
areas.sort(reverse=True)
print(areas)














