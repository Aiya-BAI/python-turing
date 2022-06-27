age = 14
if age > 18:
    print("老了")

if age > 18:
    print('老了')
else:
    print('年轻')

if age < 4:
    print("免费")
elif age < 18 or age >60:
    print("半价")
else:
    print("全价")

#简介写法
if age < 4:
    result = "免费"
elif age < 18:
    result = "半价"
else:
    result = "全价"
print(f'门票规则是{result}')

#省略else
if age < 4:
    result = "免费"
elif age < 18:
    result = "半价"
elif age >=18:
    result = "全价"
print(f'门票规则是{result}')


#例子
# alien_color = input("请输入颜色：")
# if alien_color == 'green':
#     print("get 5")
# else:
#     print("budefen")


age = 88
if age < 2:
    result = "婴儿"
elif age>=2 and age<4:
    result = "幼儿"
elif 4 <= age < 13:
    result = "儿童"
elif 13 <= age < 20:
    result = "青年人"
elif 20 <= age < 65:
    result = "成年人"
elif age >= 56:
    result = "老年人"
print(f'这个人是{result}')


age = 17
if age < 2:
    print("You're a baby!")
elif age < 4:
    print("You're a toddler!")
elif age < 13:
    print("You're a kid!")
elif age < 20:
    print("You're a teenager!")
elif age < 65:
    print("You're an adult!")
else:
    print("You're an elder!")












