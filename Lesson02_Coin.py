# Author: Raisie
# Date: Oct 15, 2021

import pgzrun
from random import randint

#varibles
WIDTH = 400
HEIGHT = 400
score = 0
game_over = False

#actors
background = Actor('background')
background.pos = 150, 150

coin = Actor('coin')
coin.pos = 200, 200

fox = Actor ('fox')
fox.pos = 150, 150

def draw():
  background.draw()
  coin.draw()
  fox.draw()
  screen.draw.text("Score: " + str(score), color="black", topleft=(50,10))

def place_coin():
  coin.x = randint(20, (WIDTH - 20))
  coin.y = randint(20, (HEIGHT - 20))

def time_up():
  pass

def update():
  xv = (keyboard.right - keyboard.left)*3
  yv = (keyboard.up - keyboard.down)*3


pgzrun.go()
