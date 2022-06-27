def animals_read(filename):

    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except:
        # print(f'{filename} not exit')
        pass
    else:
        print(contents)


animals_read('cats.txt')
animals_read('dogs.txt')
