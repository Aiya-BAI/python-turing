while True:
    try:
        first_num = int(input('input first number:'))
    except:
        print('输入的不是数')
    else:
        if first_num == 'q':
            break
    try:
        second_num = int(input('input secong number:'))
    except:
        print('输入的不是数')
    else:
        if second_num == 'q':
            break
    print(f'resule = {first_num + second_num}')






