# author: Raisie
# date: Oct 13, 2021

import pgzrun
from random import randint

score = 0
WIDTH = 400
HEIGHT = 400

pineapple = Actor("pineapple")

# Create the object in the game
def draw():
  screen.clear()
  pineapple.draw()

# Get a random position for the pineapple
def place_pineapple():
  pineapple.x = randint(0, WIDTH)
  pineapple.y = randint(0, HEIGHT)

# Define the key operation of this game
def on_mouse_down(pos):
  global score
  if pineapple.collidepoint(pos):
    score = score + 1
    print("good shot!" + str(score))
    place_pineapple()
  else:
    print("you missed!")
    quit()

place_pineapple()
pgzrun.go()

# END
