import random

def choose():
  prompt = 'How many dices to roll: '
  choice = input(prompt)
  while not choice.isdigit() or int(choice) < 1:
      choice = input(prompt)

  return choice

def main():
  choice = choose()
  dices = []
  choice = choice
  for number in range(int(choice)):
    dice = random.choice(range(1, 7))
    dices.append(dice)

  length = len(dices)
  dices = ', '.join(str(item) for item in dices)

  if length > 1:
    print('The dices are: ' + dices)
  else:
    print('The result is: ' + dices)

if __name__ == '__main__':
  main()