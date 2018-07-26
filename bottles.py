import time
import os

def clear():
  system = os.system
  system('clear')

def bottle_number():
  clear()

  prompt = 'How many bottles: '
  choice = input(prompt)

  while choice.strip() == '' or not choice.isdigit():
    clear()
    print('Let\'s try that again :)')
    choice = input(prompt)

  return int(choice)

def main():
  bottles = bottle_number()

  for bottle in reversed(range(1, bottles + 1)):
    time.sleep(0.5)
    clear()
    if bottle == 1:
      print('{} bottle!'.format(bottle))
    else:
      print('{} bottles!'.format(bottle))
    time.sleep(1)

    if bottle == 1:
      sequence_one = '{0} bottle of beer on the wall, {0} bottle of beer!'.format(bottle)
      sequence_two = 'Take one down and pass it around, no more bottles of beer on the wall.'
    else:
      sequence_one = '{0} bottles of beer on the wall, {0} bottles of beer!'.format(bottle)
      sequence_two = 'Take one down and pass it around, {} bottles of beer on the wall.'.format(bottle - 1)
    
    sequence_one = sequence_one.split()
    cache = []
    for word in sequence_one:
      clear()
      cache.append(word)
      print(' '.join(cache))
      time.sleep(0.2)

    time.sleep(0.2)
    sequence_two = sequence_two.split()
    cache = []
    for word in sequence_two:
      clear()
      cache.append(word)
      print(' '.join(sequence_one))
      print(' '.join(cache))
      time.sleep(0.2)

if __name__ == '__main__':
  main()