print('Numbers from 1 to 10')
x = 4
n =int(input('Guess the number:'))
while n <= 10:
    n =int(input('Guess the number:'))
    if n == x:
        print('Great! You did it')
        break
    else:
        continue
