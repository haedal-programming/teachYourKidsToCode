import pygame
import random

BLACK = (0,0,0)
pygame.init()
screen = pygame.display.set_mode([800,600])
pygame.display.set_caption("스마일리 터트리기")
mousedown = False
keep_going = True
clock = pygame.time.Clock()
pic = pygame.image.load("smiley.png")
colorkey = pic.get_at((0,0))
pic.set_colorkey(colorkey)
sprite_list = pygame.sprite.Group()
