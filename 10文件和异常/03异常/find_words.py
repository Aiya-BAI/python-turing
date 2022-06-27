from word_count import count_words

filename = 'little_women.txt'
count_words(filename)

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except:
    print(f'{filename} not exit')
else:
    print(contents.count('my'))
    print(contents.lower().count('my'))