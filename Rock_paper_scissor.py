Computer_choice = 'scissor'
user_choice = input('Do you want - rock, paper, or scissor?\n')

if Computer_choice == user_choice:
    print('Tie')
elif user_choice == 'rock' and Computer_choice == 'scissor':
    print('Win')
elif user_choice == 'paper' and Computer_choice == 'rock':
    print('Win')
elif user_choice == 'scissor' and Computer_choice == 'paper':
    print('Win')
else:
    print('You lose')
    