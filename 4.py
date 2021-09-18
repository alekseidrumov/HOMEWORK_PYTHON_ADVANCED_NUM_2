spisok = ['I do','the same','thing','i told','you','that','i never','would']
x = 0
for i in spisok:
    x = x + 1
    if x % 2 == 0:
        print(i[::-1])