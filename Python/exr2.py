print('Rock Paper Scissors')
print('Please choose one of them!')
x= input('Player1: ')
y= input('Player2: ')

if x=='Rock'and y=='Scissors':
    print('Player1 wins,, Congratulations')
elif x=='Rock'and y=='Paper':
    print('Player2 wins,, Congratulations!')
if x=='Scissors'and y=='Rock':
    print('Player2 wins,, Congratulations!')
elif x=='Scissors'and y=='Paper':
    print('Player1 wins,, Congratulations')
if x=='Paper' and y=='Rock':
    print('Player1 wins,, Congratulations')
elif x=='Paper' and y=='Scissors':
    print('Player2 wins,, Congratulations!')
