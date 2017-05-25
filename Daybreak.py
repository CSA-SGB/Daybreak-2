'''
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>
'''

'''
Samantha Bennefield
5/7/17
Mr. Davis
Daybreak (Top-down dungeon crawler)
Version 6
'''

#Make enemy sprite
#Check room
#Collisions

import pygame
import sys
import random
import time

listEnemy=[]
listLaser=[]
leveltime=50
creationTime=leveltime
lives=10
livesSTR=str (lives)
score=0

#Images
player_sprite = pygame.image.load('right_1.png')

room1 = pygame.image.load('square room 1.png')
room2 = pygame.image.load('square room 2.png')
room3 = pygame.image.load('square room 3.png')
room4 = pygame.image.load('square room 4.png')
room5 = pygame.image.load('square room 5.png')
room6 = pygame.image.load('square room 6.png')
room7 = pygame.image.load('square room 7.png')
room8 = pygame.image.load('square room 8.png')
room9 = pygame.image.load('square room 9.png')

vertical_hall = pygame.image.load('vertical hall.png')
horizontal_hall = pygame.image.load('horizontal hall 1.png')
horizontal_hall2 = pygame.image.load('horizontal hall 2.png')

#Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0 , 0)


wait = 7
'''This is a "timer" for enemies to spawn.
The timer is movement based.
Ex. For every 15 steps the player takes a new enemy spawns'''

class Entity(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y
        self.width = width
        self.height = height

        # This makes a rectangle around the entity, used for anything
        # from collision to moving around.
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)


class Character(Entity):
    def __init__(self, x, y, width, height):
        super(Character, self).__init__(x, y, width, height)

        self.image = player_sprite


class Player(Character):
    def __init__(self, x, y, width, height):
        super(Player, self).__init__(x, y, width, height)

        self.y_change = 0
        self.y_dist = 1.5

        self.x_change = 0
        self.x_dist = 1.5

    def MoveKeyDown(self, key):
        if (key == pygame.K_UP):
            self.y_change += -self.y_dist
        elif (key == pygame.K_DOWN):
            self.y_change += self.y_dist
        elif (key == pygame.K_LEFT):
            self.x_change += -self.x_dist
        elif (key == pygame.K_RIGHT):
            self.x_change += self.x_dist
        elif (key == pygame.K_SPACE):
            bullet = Bullet(player.rect.x+90, player.rect.y+59, 10, 10)
            all_sprites_list.add(bullet)
            listLaser.append(bullet)

    def MoveKeyUp(self, key):
        if (key == pygame.K_UP):
            self.y_change += self.y_dist
        elif (key == pygame.K_DOWN):
            self.y_change += -self.y_dist
        elif (key == pygame.K_LEFT):
            self.x_change += self.x_dist
        elif (key == pygame.K_RIGHT):
            self.x_change += -self.x_dist

    def update(self):
        self.rect.move_ip(self.x_change, 0)
        self.rect.move_ip(0, self.y_change)


class Enemy(Entity):
    def __init__(self, x, y, width, height):
        super(Enemy, self).__init__(x, y, width, height)

        self.image = pygame.Surface([width, height])
        self.image.fill(RED)

        self.x_direction = 5

        self.speed = 1

    def update(self):
        if player.x > self.x:
            self.x += 3

        if player.x < self.x:
            self.x -= 3

        if player.y > self.y:
            self.y += 3

        if player.y < self.y:
            self.y -= 3

        self.rect.x -= self.speed

class Bullet(Entity):
    def __init__(self, x, y, width, height):
        super(Bullet, self).__init__(x, y, width, height)

        self.image = pygame.Surface([width, height])
        self.image.fill(RED)

        self.x_direction = 1
        self.y_direction = 0

        self.speed = 3

    def update(self):
        self.rect.move_ip(self.speed * self.x_direction,
                          self.speed * self.y_direction)

        if self.rect.x > WIDTH: #<---If it goes off the screen
            self.kill()


pygame.init()

WIDTH = 700
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Daybreak")

clock = pygame.time.Clock()

player = Player(20, HEIGHT / 2, 20, 50)

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(player)


def checkKill(all):
    global lives
    for i in all:
        if i.rect.colliderect(player.rect):
            all.remove(i)
            i.remove(all_sprites_list)
            killed=True
            print('dead')
            lives-=1
            print(lives)


def laserHit(asteroids,lasers):
    global score
    for i in asteroids:
        for x in listLaser:
            if i.rect.colliderect(x):
                i.remove(all_sprites_list)
                x.remove(all_sprites_list)
                asteroids.remove(i)
                lasers.remove(x)
                score+=100
                print(score)


def createEnemy(creationTime, leveltime):
    height = random.randint(10, top_bound)
    x = Enemy(WIDTH, height, 20, 20)
    listEnemy.append(x)
    all_sprites_list.add(x)
    leveltime -= 1

height = random.randint(40, 50)
First = Enemy(WIDTH, height, 20, 20)
listEnemy.append(First)

all_sprites_list.add(First)


fontObj = pygame.font.Font('freesansbold.ttf', 32)

livesText = fontObj.render("Lives:"+livesSTR, 1, (RED))

#Score Text
textSurfaceObj = fontObj.render('Score:'+str(score), True, RED)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (590, 30)

#Lives Text
textSurfaceObj2 = fontObj.render('Lives:'+str(lives), True, RED)
textRectObj2 = textSurfaceObj2.get_rect()
textRectObj2.center = (80, 30)


end_lvl1 = False
end_lvl2 = False
end_lvl3 = False
end_lvl4 = False
end_lvl4_2 = False
end_lvl5 = False
end_lvl6 = False
end_lvl7 = False
end_lvl8 = False
end_lvl9 = False

hall_1_2 = False
hall_1_3 = False
hall_1_4 = False
hall_2_5 = False
hall_3_6 = False
hall_4_5 = False
hall_4_6 = False
hall_5_8 = False
hall_4_9 = False
hall_6_9 = False


start_screen=False
while (start_screen==False):
    screen.fill(BLACK)
    textSurfaceObj4 = fontObj.render('Daybreak', True, RED)
    textRectObj4 = textSurfaceObj4.get_rect()
    textRectObj4.center = (360, 100)

    textSurfaceObj5 = fontObj.render('Press ENTER to start', True, RED)
    textRectObj5 = textSurfaceObj4.get_rect()
    textRectObj5.center = (340, 300)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            start_screen=True

    screen.blit(textSurfaceObj4, textRectObj4)
    screen.blit(textSurfaceObj5, textRectObj5)
    pygame.display.flip()


end_it2=False
while (end_it2==False):
    screen.fill(BLACK)

    #Text for Instructions Screen
    instruction  = fontObj.render("Instructions:", 1, RED)
    instruction2 = fontObj.render("Up arrow = Move up", 1, RED)
    instruction3 = fontObj.render("Left arrow = Move left", 1, RED)
    instruction4 = fontObj.render("Down arrow = Move down", 1, RED)
    instruction5 = fontObj.render("Right arrow = Move right", 1, RED)
    instruction6 = fontObj.render("Space bar = Attack", 1, RED)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            end_it2 = True

    #Bliting all instructions text
    screen.blit(instruction, (100, 50))
    screen.blit(instruction2, (100, 100))
    screen.blit(instruction3, (100, 130))
    screen.blit(instruction4, (100, 160))
    screen.blit(instruction5, (100, 190))
    screen.blit(instruction6, (100, 220))
    pygame.display.flip()

end_it3 = False
while (end_it3 == False):
    screen.fill(BLACK)

    # Text for "Story" Screen
    story_text = fontObj.render("You've woken up in a mysterious castle.", 1, WHITE)
    story_text2 = fontObj.render("You're not sure how you got here.", 1, WHITE)
    story_text3 = fontObj.render("Find the portal to escape!", 1, WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            end_it3 = True

    # Bliting all story text
    screen.blit(story_text, (90, 50))
    screen.blit(story_text2, (100, 80))
    screen.blit(story_text3, (100, 110))
    pygame.display.flip()

while (end_lvl1 == False):
    laserHit(listEnemy, listLaser)
    checkKill(listEnemy)


    screen.fill(BLACK)
    screen.blit(room1, (0, 0))
    screen.blit(livesText, (0, 450))

    for event in pygame.event.get():
        right_bound = 400
        left_bound = 0
        top_bound = 400
        bottom_bound = 0

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.KEYDOWN:
                player.MoveKeyDown(event.key)
        elif event.type==pygame.KEYUP:
            player.MoveKeyUp(event.key)

        if wait > 0:
            wait=wait-1
            print(wait)
        else:
            createEnemy(creationTime, leveltime)
            wait = 7

        player.rect.move_ip(player.x_change, 0)
        player.rect.move_ip(0, player.y_change)

        if player.rect.x < 0:
            player.rect.x = 0
            print("x @ 0")
            print("leaving to 2")
            listEnemy[:] = []
            end_lvl9 = True
            end_lvl6 = True
            end_lvl3 = True

            hall_1_3 = True
            hall_1_4 = True
            hall_3_6 = True
            hall_4_6 = True
            hall_6_9 = True

            end_lvl1 = True
            
        elif player.rect.x > right_bound - player.width:
            player.rect.x = right_bound - player.width
            print("x @ right")
            listEnemy[:] = []
            end_lvl2 = True
            end_lvl5 = True
            end_lvl8 = True

            hall_1_2 = True
            hall_1_4 = True
            hall_2_5 = True
            hall_4_5 = True
            hall_5_8 = True

            end_lvl1 = True
            
        elif player.rect.y < 0:
            player.rect.y = 0
            print("y @ 0")
            print("lvl1")
            listEnemy[:] = []
            end_lvl2 = True
            end_lvl3 = True
            end_lvl5 = True
            end_lvl6 = True
            end_lvl8 = True
            end_lvl9 = True

            hall_1_2 = True
            hall_1_3 = True
            hall_2_5 = True
            hall_3_6 = True
            hall_4_5 = True
            hall_4_6 = True
            hall_5_8 = True
            hall_6_9 = True

            end_lvl1 = True

        if player.rect.y > top_bound - player.height:
            player.rect.y = top_bound - player.height
            print("y @ top")

    for ent in all_sprites_list:
        ent.update()

    all_sprites_list.draw(screen)

    pygame.display.flip()

player.x = 0
while (hall_1_2 == False):
    laserHit(listEnemy, listLaser)
    checkKill(listEnemy)


    screen.fill(BLACK)
    screen.blit(horizontal_hall, (0, 0))
    screen.blit(livesText, (0, 450))

    for event in pygame.event.get():
        right_bound = 650
        left_bound = 0
        top_bound = 400
        bottom_bound = 0

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.KEYDOWN:
                player.MoveKeyDown(event.key)
        elif event.type==pygame.KEYUP:
            player.MoveKeyUp(event.key)

        if wait > 0:
            wait=wait-1
            print(wait)
        else:
            createEnemy(creationTime, leveltime)
            wait = 7

        player.rect.move_ip(player.x_change, 0)
        player.rect.move_ip(0, player.y_change)

        if player.rect.x < 0:
            player.rect.x = 0
            print("x @ 0")
            listEnemy[:] = []
            hall_1_2 = True
            
        elif player.rect.x > right_bound - player.width:
            player.rect.x = right_bound - player.width
            print("x @ right")
            
        elif player.rect.y < 0:
            player.rect.y = 0
            print("y @ 0")
            print("hall 1 2")

        if player.rect.y > top_bound - player.height:
            player.rect.y = top_bound - player.height
            print("y @ top")

    for ent in all_sprites_list:
        ent.update()

    all_sprites_list.draw(screen)

    pygame.display.flip()

player.x = 650
while (hall_1_3 == False):
    laserHit(listEnemy, listLaser)
    checkKill(listEnemy)


    screen.fill(BLACK)
    screen.blit(horizontal_hall2, (0, 0))
    screen.blit(livesText, (0, 450))

    for event in pygame.event.get():
        right_bound = 650
        left_bound = 0
        top_bound = 400
        bottom_bound = 0

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.KEYDOWN:
                player.MoveKeyDown(event.key)
        elif event.type==pygame.KEYUP:
            player.MoveKeyUp(event.key)

        if wait > 0:
            wait=wait-1
            print(wait)
        else:
            createEnemy(creationTime, leveltime)
            wait = 7

        player.rect.move_ip(player.x_change, 0)
        player.rect.move_ip(0, player.y_change)

        if player.rect.x < 0:
            player.rect.x = 0
            print("x @ 0")
            
        elif player.rect.x > right_bound - player.width:
            player.rect.x = right_bound - player.width
            print("x @ right")
            listEnemy[:] = []
            hall_1_3 = True
            
        elif player.rect.y < 0:
            player.rect.y = 0
            print("y @ 0")
            print("hall 1 3")

        if player.rect.y > top_bound - player.height:
            player.rect.y = top_bound - player.height
            print("y @ top")

    for ent in all_sprites_list:
        ent.update()

    all_sprites_list.draw(screen)

    pygame.display.flip()

player.y = 650
while (hall_1_4 == False):
    laserHit(listEnemy, listLaser)
    checkKill(listEnemy)


    screen.fill(BLACK)
    screen.blit(vertical_hall, (0, 0))
    screen.blit(livesText, (0, 450))

    for event in pygame.event.get():
        right_bound = 400
        left_bound = 0
        top_bound = 650
        bottom_bound = 0

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.KEYDOWN:
                player.MoveKeyDown(event.key)
        elif event.type==pygame.KEYUP:
            player.MoveKeyUp(event.key)

        if wait > 0:
            wait=wait-1
            print(wait)
        else:
            createEnemy(creationTime, leveltime)
            wait = 7

        player.rect.move_ip(player.x_change, 0)
        player.rect.move_ip(0, player.y_change)

        if player.rect.x < 0:
            player.rect.x = 0
            print("x @ 0")
            
        elif player.rect.x > right_bound - player.width:
            player.rect.x = right_bound - player.width
            print("x @ right")
            
        elif player.rect.y < 0:
            player.rect.y = 0
            print("y @ 0")
            print("hall 1 4")
            listEnemy[:] = []
            hall_1_4 = True

        if player.rect.y > top_bound - player.height:
            player.rect.y = top_bound - player.height
            print("y @ top")

    for ent in all_sprites_list:
        ent.update()

    all_sprites_list.draw(screen)

    pygame.display.flip()

player.x = 400
while (end_lvl2 == False):
    laserHit(listEnemy, listLaser)
    checkKill(listEnemy)


    screen.fill(BLACK)
    screen.blit(room2, (0, 0))
    screen.blit(livesText, (0, 450))

    for event in pygame.event.get():
        right_bound = 400
        left_bound = 0
        top_bound = 400
        bottom_bound = 0

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.KEYDOWN:
                player.MoveKeyDown(event.key)
        elif event.type==pygame.KEYUP:
            player.MoveKeyUp(event.key)

        if wait > 0:
            wait=wait-1
            print(wait)
        else:
            createEnemy(creationTime, leveltime)
            wait = 7

        player.rect.move_ip(player.x_change, 0)
        player.rect.move_ip(0, player.y_change)

        if player.rect.x < 0:
            player.rect.x = 0
            print("x @ 0")
            
        elif player.rect.x > right_bound - player.width:
            player.rect.x = right_bound - player.width
            print("x @ right")
            
        elif player.rect.y < 0:
            player.rect.y = 0
            print("y @ 0")
            print("lvl 2")
            listEnemy[:] = []
            end_lvl2 = True

        if player.rect.y > top_bound - player.height:
            player.rect.y = top_bound - player.height
            print("y @ top")

    for ent in all_sprites_list:
        ent.update()

    all_sprites_list.draw(screen)

    pygame.display.flip()

player.x = 0
while (end_lvl3 == False):
    laserHit(listEnemy, listLaser)
    checkKill(listEnemy)


    screen.fill(BLACK)
    screen.blit(room3, (0, 0))
    screen.blit(livesText, (0, 450))

    for event in pygame.event.get():
        right_bound = 400
        left_bound = 0
        top_bound = 400
        bottom_bound = 0

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.KEYDOWN:
                player.MoveKeyDown(event.key)
        elif event.type==pygame.KEYUP:
            player.MoveKeyUp(event.key)

        if wait > 0:
            wait=wait-1
            print(wait)
        else:
            createEnemy(creationTime, leveltime)
            wait = 7

        player.rect.move_ip(player.x_change, 0)
        player.rect.move_ip(0, player.y_change)

        if player.rect.x < 0:
            player.rect.x = 0
            print("x @ 0")
            
        elif player.rect.x > right_bound - player.width:
            player.rect.x = right_bound - player.width
            print("x @ right")
            
        elif player.rect.y < 0:
            player.rect.y = 0
            print("y @ 0")
            print("lvl 3")
            listEnemy[:] = []
            end_lvl3 = True

        if player.rect.y > top_bound - player.height:
            player.rect.y = top_bound - player.height
            print("y @ top")

    for ent in all_sprites_list:
        ent.update()

    all_sprites_list.draw(screen)

    pygame.display.flip()

player.x = 200
player.y = 200
while (end_lvl4 == False):
    laserHit(listEnemy, listLaser)
    checkKill(listEnemy)


    screen.fill(BLACK)
    screen.blit(room4, (0, 0))
    screen.blit(livesText, (0, 450))

    for event in pygame.event.get():
        right_bound = 400
        left_bound = 0
        top_bound = 400
        bottom_bound = 0

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.KEYDOWN:
                player.MoveKeyDown(event.key)
        elif event.type==pygame.KEYUP:
            player.MoveKeyUp(event.key)

        if wait > 0:
            wait=wait-1
            print(wait)
        else:
            createEnemy(creationTime, leveltime)
            wait = 7

        player.rect.move_ip(player.x_change, 0)
        player.rect.move_ip(0, player.y_change)

        if player.rect.x < 0:
            player.rect.x = 0
            print("x @ 0")
            
        elif player.rect.x > right_bound - player.width:
            player.rect.x = right_bound - player.width
            print("x @ right")
            
        elif player.rect.y < 0:
            player.rect.y = 0
            print("y @ 0")
            print("lvl4")
            listEnemy[:] = []
            end_lvl4 = True

        if player.rect.y > top_bound - player.height:
            player.rect.y = top_bound - player.height
            print("y @ top")

    for ent in all_sprites_list:
        ent.update()

    all_sprites_list.draw(screen)

    pygame.display.flip()

player.y = 650
while (hall_2_5 == False):
    laserHit(listEnemy, listLaser)
    checkKill(listEnemy)


    screen.fill(BLACK)
    screen.blit(vertical_hall, (0, 0))
    screen.blit(livesText, (0, 450))

    for event in pygame.event.get():
        right_bound = 400
        left_bound = 0
        top_bound = 650
        bottom_bound = 0

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.KEYDOWN:
                player.MoveKeyDown(event.key)
        elif event.type==pygame.KEYUP:
            player.MoveKeyUp(event.key)

        if wait > 0:
            wait=wait-1
            print(wait)
        else:
            createEnemy(creationTime, leveltime)
            wait = 7

        player.rect.move_ip(player.x_change, 0)
        player.rect.move_ip(0, player.y_change)

        if player.rect.x < 0:
            player.rect.x = 0
            print("x @ 0")
            
        elif player.rect.x > right_bound - player.width:
            player.rect.x = right_bound - player.width
            print("x @ right")
            
        elif player.rect.y < 0:
            player.rect.y = 0
            print("y @ 0")
            print("hall 2 5")
            listEnemy[:] = []
            hall_2_5 = True

        if player.rect.y > top_bound - player.height:
            player.rect.y = top_bound - player.height
            print("y @ top")

    for ent in all_sprites_list:
        ent.update()

    all_sprites_list.draw(screen)

    pygame.display.flip()

player.y = 650
while (hall_3_6 == False):
    laserHit(listEnemy, listLaser)
    checkKill(listEnemy)


    screen.fill(BLACK)
    screen.blit(vertical_hall, (0, 0))
    screen.blit(livesText, (0, 450))

    for event in pygame.event.get():
        right_bound = 400
        left_bound = 0
        top_bound = 650
        bottom_bound = 0

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.KEYDOWN:
                player.MoveKeyDown(event.key)
        elif event.type==pygame.KEYUP:
            player.MoveKeyUp(event.key)

        if wait > 0:
            wait=wait-1
            print(wait)
        else:
            createEnemy(creationTime, leveltime)
            wait = 7

        player.rect.move_ip(player.x_change, 0)
        player.rect.move_ip(0, player.y_change)

        if player.rect.x < 0:
            player.rect.x = 0
            print("x @ 0")
            
        elif player.rect.x > right_bound - player.width:
            player.rect.x = right_bound - player.width
            print("x @ right")
            
        elif player.rect.y < 0:
            player.rect.y = 0
            print("y @ 0")
            print("hall 3 6")
            listEnemy[:] = []
            hall_3_6 = True

        if player.rect.y > top_bound - player.height:
            player.rect.y = top_bound - player.height
            print("y @ top")

    for ent in all_sprites_list:
        ent.update()

    all_sprites_list.draw(screen)

    pygame.display.flip()

player.y = 400
while (end_lvl5 == False):
    laserHit(listEnemy, listLaser)
    checkKill(listEnemy)


    screen.fill(BLACK)
    screen.blit(room5, (0, 0))
    screen.blit(livesText, (0, 450))

    for event in pygame.event.get():
        right_bound = 400
        left_bound = 0
        top_bound = 400
        bottom_bound = 0

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.KEYDOWN:
                player.MoveKeyDown(event.key)
        elif event.type==pygame.KEYUP:
            player.MoveKeyUp(event.key)

        if wait > 0:
            wait=wait-1
            print(wait)
        else:
            createEnemy(creationTime, leveltime)
            wait = 7

        player.rect.move_ip(player.x_change, 0)
        player.rect.move_ip(0, player.y_change)

        if player.rect.x < 0:
            player.rect.x = 0
            print("x @ 0")
            
        elif player.rect.x > right_bound - player.width:
            player.rect.x = right_bound - player.width
            print("x @ right")
            listEnemy[:] = []
            end_lvl8 = True

            hall_5_8 = True

            end_lvl5 = True
            
        elif player.rect.y < 0:
            player.rect.y = 0
            print("y @ 0")
            print("lvl5")
            listEnemy[:] = []
            end_lvl4 = True
            end_lvl7 = True

            hall_4_5 = True
            hall_4_6 = True
            hall_4_9 = True
            
            end_lvl5 = True

        if player.rect.y > top_bound - player.height:
            player.rect.y = top_bound - player.height
            print("y @ top")

    for ent in all_sprites_list:
        ent.update()

    all_sprites_list.draw(screen)

    pygame.display.flip()

player.y = 400
while (end_lvl6 == False):
    laserHit(listEnemy, listLaser)
    checkKill(listEnemy)


    screen.fill(BLACK)
    screen.blit(room6, (0, 0))
    screen.blit(livesText, (0, 450))

    for event in pygame.event.get():
        right_bound = 400
        left_bound = 0
        top_bound = 400
        bottom_bound = 0

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.KEYDOWN:
                player.MoveKeyDown(event.key)
        elif event.type==pygame.KEYUP:
            player.MoveKeyUp(event.key)

        if wait > 0:
            wait=wait-1
            print(wait)
        else:
            createEnemy(creationTime, leveltime)
            wait = 7

        player.rect.move_ip(player.x_change, 0)
        player.rect.move_ip(0, player.y_change)

        if player.rect.x < 0:
            player.rect.x = 0
            print("x @ 0")
            listEnemy[:] = []
            end_lvl9 = True

            hall_6_9 = True

            end_lvl6 = True
            
        elif player.rect.x > right_bound - player.width:
            player.rect.x = right_bound - player.width
            print("x @ right")
            
        elif player.rect.y < 0:
            player.rect.y = 0
            print("y @ 0")
            print("lvl6")
            listEnemy[:] = []
            end_lvl4 = True
            end_lvl7 = True
            end_lvl6 = True

            hall_4_5 = True
            hall_4_6 = True
            hall_4_9 = True
            
            end_lvl6 = True

        if player.rect.y > top_bound - player.height:
            player.rect.y = top_bound - player.height
            print("y @ top")

    for ent in all_sprites_list:
        ent.update()

    all_sprites_list.draw(screen)

    pygame.display.flip()

player.x = 0
while (hall_4_5 == False):
    laserHit(listEnemy, listLaser)
    checkKill(listEnemy)


    screen.fill(BLACK)
    screen.blit(horizontal_hall2, (0, 0))
    screen.blit(livesText, (0, 450))

    for event in pygame.event.get():
        right_bound = 650
        left_bound = 0
        top_bound = 400
        bottom_bound = 0

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.KEYDOWN:
                player.MoveKeyDown(event.key)
        elif event.type==pygame.KEYUP:
            player.MoveKeyUp(event.key)

        if wait > 0:
            wait=wait-1
            print(wait)
        else:
            createEnemy(creationTime, leveltime)
            wait = 7

        player.rect.move_ip(player.x_change, 0)
        player.rect.move_ip(0, player.y_change)

        if player.rect.x < 0:
            player.rect.x = 0
            print("x @ 0")
            
        elif player.rect.x > right_bound - player.width:
            player.rect.x = right_bound - player.width
            print("x @ right")
            listEnemy[:] = []
            hall_4_5 = True
            
        elif player.rect.y < 0:
            player.rect.y = 0
            print("y @ 0")
            print("hall 4 5")

        if player.rect.y > top_bound - player.height:
            player.rect.y = top_bound - player.height
            print("y @ top")

    for ent in all_sprites_list:
        ent.update()

    all_sprites_list.draw(screen)

    pygame.display.flip()

player.x = 650
while (hall_4_6 == False):
    laserHit(listEnemy, listLaser)
    checkKill(listEnemy)


    screen.fill(BLACK)
    screen.blit(horizontal_hall, (0, 0))
    screen.blit(livesText, (0, 450))

    for event in pygame.event.get():
        right_bound = 650
        left_bound = 0
        top_bound = 400
        bottom_bound = 0

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.KEYDOWN:
                player.MoveKeyDown(event.key)
        elif event.type==pygame.KEYUP:
            player.MoveKeyUp(event.key)

        if wait > 0:
            wait=wait-1
            print(wait)
        else:
            createEnemy(creationTime, leveltime)
            wait = 7

        player.rect.move_ip(player.x_change, 0)
        player.rect.move_ip(0, player.y_change)

        if player.rect.x < 0:
            player.rect.x = 0
            print("x @ 0")
            listEnemy[:] = []
            hall_4_6 = True
            
        elif player.rect.x > right_bound - player.width:
            player.rect.x = right_bound - player.width
            print("x @ right")
            
        elif player.rect.y < 0:
            player.rect.y = 0
            print("y @ 0")
            print("hall 4 6")

        if player.rect.y > top_bound - player.height:
            player.rect.y = top_bound - player.height
            print("y @ top")

    for ent in all_sprites_list:
        ent.update()

    all_sprites_list.draw(screen)

    pygame.display.flip()

player.x = 200
player.y = 200
while (end_lvl4_2 == False):
    laserHit(listEnemy, listLaser)
    checkKill(listEnemy)


    screen.fill(BLACK)
    screen.blit(room4, (0, 0))
    screen.blit(livesText, (0, 450))

    for event in pygame.event.get():
        right_bound = 400
        left_bound = 0
        top_bound = 400
        bottom_bound = 0

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.KEYDOWN:
                player.MoveKeyDown(event.key)
        elif event.type==pygame.KEYUP:
            player.MoveKeyUp(event.key)

        if wait > 0:
            wait=wait-1
            print(wait)
        else:
            createEnemy(creationTime, leveltime)
            wait = 7

        player.rect.move_ip(player.x_change, 0)
        player.rect.move_ip(0, player.y_change)

        if player.rect.x < 0:
            player.rect.x = 0
            print("x @ 0")
            
        elif player.rect.x > right_bound - player.width:
            player.rect.x = right_bound - player.width
            print("x @ right")
            
        elif player.rect.y < 0:
            player.rect.y = 0
            print("y @ 0")
            print("lvl 4 2")
            listEnemy[:] = []
            end_lvl4_2 = True

        if player.rect.y > top_bound - player.height:
            player.rect.y = top_bound - player.height
            print("y @ top")

    for ent in all_sprites_list:
        ent.update()

    all_sprites_list.draw(screen)

    pygame.display.flip()

player.y = 650
while (hall_4_9 == False):
    laserHit(listEnemy, listLaser)
    checkKill(listEnemy)


    screen.fill(BLACK)
    screen.blit(vertical_hall, (0, 0))
    screen.blit(livesText, (0, 450))

    for event in pygame.event.get():
        right_bound = 400
        left_bound = 0
        top_bound = 650
        bottom_bound = 0

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.KEYDOWN:
                player.MoveKeyDown(event.key)
        elif event.type==pygame.KEYUP:
            player.MoveKeyUp(event.key)

        if wait > 0:
            wait=wait-1
            print(wait)
        else:
            createEnemy(creationTime, leveltime)
            wait = 7

        player.rect.move_ip(player.x_change, 0)
        player.rect.move_ip(0, player.y_change)

        if player.rect.x < 0:
            player.rect.x = 0
            print("x @ 0")
            
        elif player.rect.x > right_bound - player.width:
            player.rect.x = right_bound - player.width
            print("x @ right")
            
        elif player.rect.y < 0:
            player.rect.y = 0
            print("y @ 0")
            print("hall 4 9")
            listEnemy[:] = []
            hall_4_9 = True

        if player.rect.y > top_bound - player.height:
            player.rect.y = top_bound - player.height
            print("y @ top")

    for ent in all_sprites_list:
        ent.update()

    all_sprites_list.draw(screen)

    pygame.display.flip()

    while (hall_5_8 == False):
        laserHit(listEnemy, listLaser)
        checkKill(listEnemy)


    screen.fill(BLACK)
    screen.blit(vertical_hall, (0, 0))
    screen.blit(livesText, (0, 450))

    for event in pygame.event.get():
        right_bound = 400
        left_bound = 0
        top_bound = 650
        bottom_bound = 0

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.KEYDOWN:
                player.MoveKeyDown(event.key)
        elif event.type==pygame.KEYUP:
            player.MoveKeyUp(event.key)

        if wait > 0:
            wait=wait-1
            print(wait)
        else:
            createEnemy(creationTime, leveltime)
            wait = 7

        player.rect.move_ip(player.x_change, 0)
        player.rect.move_ip(0, player.y_change)

        if player.rect.x < 0:
            player.rect.x = 0
            print("x @ 0")
            
        elif player.rect.x > right_bound - player.width:
            player.rect.x = right_bound - player.width
            print("x @ right")
            
        elif player.rect.y < 0:
            player.rect.y = 0
            print("y @ 0")
            print("hall 5 8")
            listEnemy[:] = []
            hall_5_8 = True

        if player.rect.y > top_bound - player.height:
            player.rect.y = top_bound - player.height
            print("y @ top")

    for ent in all_sprites_list:
        ent.update()

    all_sprites_list.draw(screen)

    pygame.display.flip()

player.y = 650
while (hall_6_9 == False):
    laserHit(listEnemy, listLaser)
    checkKill(listEnemy)


    screen.fill(BLACK)
    screen.blit(vertical_hall, (0, 0))
    screen.blit(livesText, (0, 450))

    for event in pygame.event.get():
        right_bound = 400
        left_bound = 0
        top_bound = 650
        bottom_bound = 0

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.KEYDOWN:
                player.MoveKeyDown(event.key)
        elif event.type==pygame.KEYUP:
            player.MoveKeyUp(event.key)

        if wait > 0:
            wait=wait-1
            print(wait)
        else:
            createEnemy(creationTime, leveltime)
            wait = 7

        player.rect.move_ip(player.x_change, 0)
        player.rect.move_ip(0, player.y_change)

        if player.rect.x < 0:
            player.rect.x = 0
            print("x @ 0")
            
        elif player.rect.x > right_bound - player.width:
            player.rect.x = right_bound - player.width
            print("x @ right")
            
        elif player.rect.y < 0:
            player.rect.y = 0
            print("y @ 0")
            print("hall 6 9")
            listEnemy[:] = []
            hall_6_9 = True

        if player.rect.y > top_bound - player.height:
            player.rect.y = top_bound - player.height
            print("y @ top")

    for ent in all_sprites_list:
        ent.update()

    all_sprites_list.draw(screen)

    pygame.display.flip()

player.y = 400
while (end_lvl7 == False):
    laserHit(listEnemy, listLaser)
    checkKill(listEnemy)


    screen.fill(BLACK)
    screen.blit(room7, (0, 0))
    screen.blit(livesText, (0, 450))

    for event in pygame.event.get():
        right_bound = 400
        left_bound = 0
        top_bound = 400
        bottom_bound = 0

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.KEYDOWN:
                player.MoveKeyDown(event.key)
        elif event.type==pygame.KEYUP:
            player.MoveKeyUp(event.key)

        if wait > 0:
            wait=wait-1
            print(wait)
        else:
            createEnemy(creationTime, leveltime)
            wait = 7

        player.rect.move_ip(player.x_change, 0)
        player.rect.move_ip(0, player.y_change)

        if player.rect.x < 0:
            player.rect.x = 0
            print("x @ 0")
            
        elif player.rect.x > right_bound - player.width:
            player.rect.x = right_bound - player.width
            print("x @ right")
            
        elif player.rect.y < 0:
            player.rect.y = 0
            print("y @ 0")
            print("lvl7")

        if player.rect.y > top_bound - player.height:
            player.rect.y = top_bound - player.height
            print("y @ top")

    for ent in all_sprites_list:
        ent.update()

    all_sprites_list.draw(screen)

    pygame.display.flip()

player.y = 400
while (end_lvl8 == False):
    laserHit(listEnemy, listLaser)
    checkKill(listEnemy)


    screen.fill(BLACK)
    screen.blit(room8, (0, 0))
    screen.blit(livesText, (0, 450))

    for event in pygame.event.get():
        right_bound = 400
        left_bound = 0
        top_bound = 400
        bottom_bound = 0

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.KEYDOWN:
                player.MoveKeyDown(event.key)
        elif event.type==pygame.KEYUP:
            player.MoveKeyUp(event.key)

        if wait > 0:
            wait=wait-1
            print(wait)
        else:
            createEnemy(creationTime, leveltime)
            wait = 7

        player.rect.move_ip(player.x_change, 0)
        player.rect.move_ip(0, player.y_change)

        if player.rect.x < 0:
            player.rect.x = 0
            print("x @ 0")
            
        elif player.rect.x > right_bound - player.width:
            player.rect.x = right_bound - player.width
            print("x @ right")
            
        elif player.rect.y < 0:
            player.rect.y = 0
            print("y @ 0")
            print("lvl8")

        if player.rect.y > top_bound - player.height:
            player.rect.y = top_bound - player.height
            print("y @ top")

    for ent in all_sprites_list:
        ent.update()

    all_sprites_list.draw(screen)

    pygame.display.flip()

player.y = 400
while (end_lvl9 == False):
    laserHit(listEnemy, listLaser)
    checkKill(listEnemy)


    screen.fill(BLACK)
    screen.blit(room9, (0, 0))
    screen.blit(livesText, (0, 450))

    for event in pygame.event.get():
        right_bound = 400
        left_bound = 0
        top_bound = 400
        bottom_bound = 0

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.KEYDOWN:
                player.MoveKeyDown(event.key)
        elif event.type==pygame.KEYUP:
            player.MoveKeyUp(event.key)

        if wait > 0:
            wait=wait-1
            print(wait)
        else:
            createEnemy(creationTime, leveltime)
            wait = 7

        player.rect.move_ip(player.x_change, 0)
        player.rect.move_ip(0, player.y_change)

        if player.rect.x < 0:
            player.rect.x = 0
            print("x @ 0")
            
        elif player.rect.x > right_bound - player.width:
            player.rect.x = right_bound - player.width
            print("x @ right")
            
        elif player.rect.y < 0:
            player.rect.y = 0
            print("y @ 0")
            print("lvl9")

        if player.rect.y > top_bound - player.height:
            player.rect.y = top_bound - player.height
            print("y @ top")

    for ent in all_sprites_list:
        ent.update()

    all_sprites_list.draw(screen)

    pygame.display.flip()

#Game Loop
while True:

    laserHit(listEnemy, listLaser)
    checkKill(listEnemy)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYUP:
            player.MoveKeyUp(event.key)
        elif event.type == pygame.KEYDOWN:
            player.MoveKeyDown(event.key)

        if wait > 0:
            wait=wait-1
            print(wait)
        else:
            createEnemy(creationTime, leveltime)
            wait = 15


    for ent in all_sprites_list:
        ent.update()

    screen.fill(BLACK)
    screen.blit(livesText, (0, 450))


    all_sprites_list.draw(screen)

    creationTime -= 1

    pygame.display.flip()

    clock.tick(60)
