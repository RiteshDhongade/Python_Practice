import random
Computer_choice = random.choice(['scissor', 'rock', 'paper'])
user_choice = input('Do you want - rock, paper, or scissor?\n')

if Computer_choice == user_choice:
    print('Tie')
elif user_choice == 'rock' and Computer_choice == 'scissor':
    print('Win,the computer had' + Computer_choice)
elif user_choice == 'paper' and Computer_choice == 'rock':
    print('Win,the computer had' + Computer_choice)
elif user_choice == 'scissor' and Computer_choice == 'paper':
    print('Win,the computer had  ' + Computer_choice)
else:
    print('You lose, the computer had  ' + Computer_choice)
    