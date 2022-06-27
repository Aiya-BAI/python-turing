def greet_users(names):
    for name in names:
        msg = 'hello,' + name.title() + '!'
        print(msg)

usernames = ['haahahha', 'l;kajd', 'lkadshf']
greet_users(usernames)

# # 修改列表
# # 要打印的设计
# designs = ['iphone case', 'robot pendant', 'dodecahedron']
# models = []
# # 模拟打印，移动到models
# while designs:
#     models.append(designs.pop())
#
# for com_models in models:
#     print(com_model)
# print(model)

# 修改成函数

def print_models(undesigns, models):

    while undesigns:
        models.append(undesigns.pop())
    return models


def show_model(models):

    for com_model in models:
        print(com_model, end="\t")

undesigns = ['iphone case', 'robot pendant', 'dodecahedron']
models = []

show_model(print_models(undesigns[:], models))# 传递列表副本
print(f'\n{undesigns}')
print()

show_model(print_models(undesigns, models))
print(undesigns)










