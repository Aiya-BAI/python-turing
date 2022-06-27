def get_formatted_name(first_name, last_name):
    """返回全名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name('bai', 'yunce')
print(musician)


def get_name(first_name, last_name, middle_name=''):

    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

print(get_name('bai', 'yun', 'ce'))
print(get_name('bai', 'yun'))


#返回字典
def build_person(first_name, last_name):
    """返回一个字典，其中包含一个人的信息"""
    person = {
        'first': first_name,
        'last': last_name
    }
    return person

print(build_person('bai', 'yunce'))
print()

while True:
    print("write your name: ")
    print("按q键退出")
    f_name = input("first_name: ")
    if f_name == 'q':
        break
    l_name = input("last_name: ")
    if l_name == "q":
        break

    print(get_name(f_name, l_name))

















