from random import randint
from time import time
WIDTH = 600
HEIGHT = 600
score = 0
game_over=False
#click=False
fox=Actor("fox1")
fox.x=randint(50,(WIDTH-50))
fox.y=randint(50,(HEIGHT-50))

coin = Actor("coin")
coin.pos=200,200

#again=Actor("again")
#again.pos=300,350
def draw():
    screen.fill("green")
    fox.draw()
    coin.draw()
    screen.draw.text("Score: "+str(score),color="black",topleft=(10,10))
    if game_over:
        screen.fill("skyblue")
        screen.draw.text("Time Over! ",topleft=(150,250),fontsize=80)
        screen.draw.text("Final Score: "+str(score),topleft=(185,300),fontsize=40)
        #again.draw()
        
        
def place_coin():
    coin.x=randint(30,(WIDTH-30))
    coin.y=randint(30,(HEIGHT-30))

def time_up():
    global game_over
    game_over= True

#def on_mouse_down(pos):
    #if again.collidepoint(pos):
        #click=True

def update():
    global score,game_over
    if keyboard.left:
        fox.x = fox.x-5
    elif keyboard.right:
        fox.x = fox.x+5
    elif keyboard.up:
        fox.y = fox.y-5
    elif keyboard.down:
        fox.y = fox.y+5

    coin_collected=fox.colliderect(coin)

    if coin_collected:
        score =score +10
        place_coin()
    if game_over and keyboard.space:
        score=0
        game_over=False
        fox.x=randint(50,(WIDTH-50))
        fox.y=randint(50,(HEIGHT-50))
        clock.schedule(time_up, 10.0)
        place_coin()

clock.schedule(time_up, 10.0)
place_coin()
