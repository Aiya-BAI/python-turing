current_nmuber = 1
while current_nmuber <= 5:
    print(current_nmuber)
    current_nmuber += 1

prompt = "enter 'quit' to end the program: "

active = True          #标志

while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)










