filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f'{filename} not found')

else:
    words = contents.split()
    num_word = len(words)
    print(num_word)