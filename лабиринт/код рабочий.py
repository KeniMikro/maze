
from pygame import *
from random import randint

window = display.set_mode((1400, 1000))
display.set_caption('ТЫ НЕ ПРОЙДЕЕЕЕЕЕШЬ!!!!')


background = transform.scale(image.load("фон2.jpg"), (1400, 1000))

#путь до лотка

#спрайт1 - кот
#спрайт2 - злая собака



mixer.init()
mixer.music.load('котопесни.mpeg')
mixer.music.play(-1)
mixer.music.set_volume(0.1)




game = True
finish = False

x1 = 350
y1 = 700
mouse_num = 0
micetext = 'Колличество мышей:' + str(mouse_num)
font.init()
text = font.Font(None, 100)
text2 = font.Font(None, 30)
win = text.render('YOU LOSSEEEE. Joke ^_^', True, (0,255,0))
mouse_num = 0
micetext = 'Количество мышей:' + str(mouse_num)
mice_count = text2.render(micetext, True, (0,0,0))
lose = text.render('YOU FAIL HAHAHHAHAHA!', True, (255,0,0))
cheater = text.render('OH! ARE YOU A CHEATER?!', True, (255,215,0))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_w, player_h):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_w, player_h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()

        if key_pressed[K_UP]:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN]:
            self.rect.y += self.speed
        if key_pressed[K_LEFT]:
            self.rect.x -= self.speed
        if key_pressed[K_RIGHT] :
            self.rect.x += self.speed
    def cheat(self):
        if self.rect.x <= 5 or self.rect.x >= 1300 or self.rect.y <= 5 or self.rect.y >= 900:
            return True
class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.x <= 700:
           self.direction = "right"
        if self.rect.x >= 1250:
           self.direction = "left"
        if self.direction == "left":
           self.rect.x -= self.speed
        else:
           self.rect.x += self.speed

kot = Player("котик_перс.png", 70, 550, 0.6, 80, 80)      
cobaka = Enemy("гав-гав.png", 900, 550, 1, 150, 120)      
lotok = GameSprite("цель_лоток.png", 1230, 800, 10, 120, 110)  

mousee1 = GameSprite("мышь.jpg", 300, 550, 10, 70, 70)  
mousee2 = GameSprite("мышь.jpg", 300, 300, 10, 70, 70)
mousee3 = GameSprite("мышь.jpg", 550, 300, 10, 70, 70)
mousee4 = GameSprite("мышь.jpg", 550, 100, 10, 70, 70)
mousee5 = GameSprite("мышь.jpg", 750, 100, 10, 70, 70)
mousee6 = GameSprite("мышь.jpg", 750, 500, 10, 70, 70)
mousee7 = GameSprite("мышь.jpg", 850, 800, 10, 70, 70)
mousee8 = GameSprite("мышь.jpg", 950, 100, 10, 70, 70)
mousee9 = GameSprite("мышь.jpg", 1200, 100, 10, 70, 70)
mousee10 = GameSprite("мышь.jpg", 1200, 500, 10, 70, 70)

wall1 = GameSprite('стенааааааа.jpeg', 30, 700, 0, 460, 90) 
wall2 = GameSprite('стенаправа.jpeg', 400, 400, 0, 90, 300) 
wall3 = GameSprite('стенаправа.jpeg', 130, 200, 0, 90, 300) 
wall4 = GameSprite('стенааааааа.jpeg', 170, 200, 0, 330, 90) 
wall5 = GameSprite('стенааааааа.jpeg', 400, 400, 0, 230, 90)
wall6 = GameSprite('стенаправа.jpeg', 630, 200, 0, 90, 780) 
wall7 = GameSprite('стенаправа.jpeg', 380, 5, 0, 120, 250) 
wall8 = GameSprite('стенааааааа.jpeg', 380, 0, 0, 470, 90)
wall9 = GameSprite('стенаправа.jpeg', 850, 0, 0, 90, 790) 
wall10 = GameSprite('стенааааааа.jpeg', 630, 900, 0, 460, 90)
wall11 = GameSprite('стенаправа.jpeg', 1050, 200, 0, 90, 790) 
wall12 = GameSprite('стенааааааа.jpeg', 880, 0, 0, 470, 90)
wall13 = GameSprite('стенаправа.jpeg', 1300, 0, 0, 110, 750) 

walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9, wall10, wall12, wall13]

mice_list = [mousee1,mousee2,mousee3,mousee4,mousee5,mousee6,mousee7,mousee8,mousee9,mousee10,]

mouse_sound = ["звук мышь1.mp3","звук мышь2.mp3","звук мышь3.mp3","звук мышь4.mp3","звук мышь5.mp3","звук мышь6.mp3","звук мышь7.mp3","звук мышь8.mp3","звук мышь9.mp3","звук мышь10.mp3",]
while game:
    if finish != True:
        window.blit(background, (0,0))
        mousee1.reset()
        mousee2.reset()
        mousee3.reset()
        mousee4.reset()
        mousee5.reset()
        mousee6.reset()
        mousee7.reset()
        mousee8.reset()
        mousee9.reset()
        mousee10.reset()
        for micee in mice_list:
            if sprite.collide_rect(kot, micee):
                micee.rect.x += 2000
                mouse_num += 1
                micetext = 'Количество мышей:' + str(mouse_num)
                mice_count = text2.render(micetext, True, (0,0,0))
                window.blit(mice_count, (10, 10))
                    
                num_ms = len(mouse_sound)
                ms = randint(0, num_ms-1)
                pisk = mixer.Sound (mouse_sound[ms] )
                mouse_sound.remove(mouse_sound[ms])
                pisk.set_volume(0.3)
                pisk.play()

                    
            else:
                window.blit(mice_count, (10, 10))

            for walll in walls:
                if sprite.collide_rect(kot, walll):
                    finish = True
                    background = transform.scale(image.load("фон поражение.jpg"), (1400, 1000))
                    window.blit(background, (0,0))
                    window.blit(lose, (200, 500))
                    mixer.music.load('айай.mp3')
                    mixer.music.play()
                    mixer.music.set_volume(20)

        if finish != True:
            if sprite.collide_rect(kot, lotok) and mouse_num == 10:
                finish = True
                background = transform.scale(image.load("фон победа.jpg"), (1400, 1000))
                window.blit(background, (0,0))
                mixer.music.load('музыка победа.mp3')
                mixer.music.play()
                mixer.music.set_volume(20)
                background = transform.scale(image.load("фон чит.jpg"), (1400, 1000))
                

                window.blit(win, (200, 500))

            elif sprite.collide_rect(kot, cobaka):
                finish = True
                background = transform.scale(image.load("фон поражение.jpg"), (1400, 1000))
                window.blit(background, (0,0))

                
                window.blit(lose, (200, 500))
                mixer.music.load('айай.mp3')
                mixer.music.play()
                mixer.music.set_volume(20)
            elif kot.cheat():
                finish = True
                mixer.music.load('читер.mp3')
                mixer.music.play()
                mixer.music.set_volume(20)
                background = transform.scale(image.load("фон чит.jpg"), (1400, 1000))
                window.blit(background, (0,0))
                
                window.blit(cheater, (200, 500))
            else:
                
                wall2.reset()
                wall1.reset()
                wall4.reset()
                wall3.reset()
                wall5.reset()
                wall6.reset()
                wall7.reset()
                wall8.reset()
                wall9.reset()
                wall10.reset()
                wall11.reset()
                wall12.reset()
                wall13.reset()

                
                

                cobaka.update()
                cobaka.reset()
                lotok.reset()
                kot.update()
                kot.reset()
              
    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()

    