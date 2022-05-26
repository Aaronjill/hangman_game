import random
import os
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo
print(logo)
end_of_game = False
chosen_word = random.choice(word_list)

lives=6


c_w_l=[]
b=''
for n in chosen_word:
  c_w_l.append('_')


while end_of_game == False:
  guess = input("Guess a letter: ").lower() 
  os.system('cls')
  print(logo)   
  l=0
  for n in chosen_word:
    if n == guess:
      c_w_l[l]=n
    l+=1
  if guess not in c_w_l:
    lives-=1
    if lives == 0:
      print('\nYou lose')
      print(f'Pssst, the solution is {chosen_word}.')
      end_of_game=True
  print(stages[lives])
  print(f"{' '.join(c_w_l)}")
  print('\nlive remaining =',lives)
  if '_' not in c_w_l:
    end_of_game = True
    print('You Won')
