print('Numbers from 1 to 10')
x = 4
n =int(input('Guess the number:'))
while True:
    if n>10 or n<1 :
        print('Numbers should be between 1 and 10')
        n =int(input('Guess the number:'))
    else:
        while n!=x:
            n =int(input('Guess the number:'))
        else:
            print('Great! You did it')
            break
