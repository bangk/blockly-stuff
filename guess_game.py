#!/usr/bin/env python
done = None
guess = None
def win():
  global done
  print 'Yes, you got it!'
  done = True

def lose():
  print 'Try again.'

while not done:
  guess = float(raw_input('Guess a number between 1 & 10: '))
  if 7 == guess:
    win()
  else:
    lose()
