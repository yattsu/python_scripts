import time
import datetime
import os

def main():
  os.system('clear')

  current_time = datetime.datetime.now().time()
  current_time = str(current_time).split('.')[0]
  print(current_time)

  time.sleep(1)

if __name__ == '__main__':
  while True:
    main()