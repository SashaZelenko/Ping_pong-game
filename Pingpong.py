from pygame import *
from random import randint

score = 0
lost = 0 
# score = 0
max_lost = 3
goal = 10
life = 3


speed_x = 10 
speed_y = 10  

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5: 
            self.rect.y -= self.speed  
        if keys[K_DOWN] and self.rect.y < 620:  
            self.rect.y += self.speed 

  
    def update_l(self):
        keys = key.get_pressed() 
        if keys[K_w] and self.rect.y > 5: 
            self.rect.y -= self.speed 
        if keys[K_s] and self.rect.y <520:
            self.rect.y += self.speed  


win_width = 700
win_height = 500
window = display.set_mode((700, 500))
display.set_caption('Ping_pong')
background = transform.scale(image.load("megastol.png"), (win_width, win_height))

game = True 
finish = False 
clock = time.Clock()  

rocket1 = Player('platform.png', 30, 200, 50, 150, 7)
rocket2 = Player('platform.png', 620, 200, 50, 150, 7)
ball = GameSprite("balll.png", 200, 200, 50, 50, 50)

clock = time.Clock()
FPS = 60


font.init()
font = font.SysFont('Arial', 30)
lose1 = font.render('PLAYER 1 LOSE! PLAYER 2 WIN!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE! PLAYER 1 WIN!', True, (180, 0, 0))

game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.blit(background,(0, 0))
        rocket1.update_l()  
        rocket2.update_r() 
        ball.rect.x += speed_x 
        ball.rect.y += speed_y  

        if sprite.collide_rect(rocket1, ball) or sprite.collide_rect(rocket2, ball):
            speed_x *= -1
            speed_y *= 1 

        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *= -1 

        
        if ball.rect.x < 0:
            finish = True 
            window.blit(lose1, (200, 200)) 
            game_over = True 

       
        if ball.rect.x > win_width:
            finish = True 
            window.blit(lose2, (200, 200))  
            game_over = True  

        rocket1.update_l()
        rocket1.reset()
        rocket2.update_r()
        rocket2.reset()
        ball.update()
        ball.reset()
        clock.tick(40)
        display.update()
        clock.tick(FPS)