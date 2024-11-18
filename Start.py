import pygame
import sys
import random
import time

light_blue = pygame.Color(99, 213, 255)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
navy_blue = pygame.Color(0, 0, 100)
yellow = pygame.Color(255, 255, 0)
orange = pygame.Color(255, 200, 124)

# constants
screen_width = 1280
screen_height = 720
size_block = 80
bot_size_block = 30
size_card = 5
announce_time = 0.5
range_number = 50
# img
blue_screen = pygame.image.load("picture/background.png")
mark_pic = pygame.image.load("picture/star.png")
yellow_button = pygame.image.load("picture/button.png")
glow_button = pygame.image.load("picture/button_click.png")
BINGO = pygame.image.load("picture/BINGO.png")
chest = pygame.transform.scale(pygame.image.load("picture/chest.png"), (301.8, 300))
crab = pygame.transform.scale(pygame.image.load("picture/crab.png"), (170.6, 240))
fish = pygame.transform.scale(pygame.image.load("picture/fish.png"), (200, 200))
octopus = pygame.transform.scale(pygame.image.load("picture/octopus.png"), (200, 200))
sand = pygame.image.load("picture/sand.png")
seahorse = pygame.transform.scale(pygame.image.load("picture/seahorse.png"), (153, 240))
seaweed = pygame.image.load("picture/seaweed.png")
seaweed2 = pygame.image.load("picture/seaweed2.png")
shark = pygame.transform.scale(pygame.image.load("picture/shark.png"), (150, 150))
seahorse2 = pygame.transform.scale(pygame.image.load("picture/seahorse2.png"), (50, 50))
octopus2 = pygame.transform.scale(pygame.image.load("picture/octopus2.png"), (50, 50))
crab2 = pygame.transform.scale(pygame.image.load("picture/crab2.png"), (60, 60))
shark2 = pygame.transform.scale(pygame.image.load("picture/shark2.png"), (250, 250))
pause_screen = pygame.transform.scale(
    pygame.image.load("picture/pause.png"), (690, 490)
)


def bot_mark(mark):
    return pygame.transform.scale(
        pygame.image.load("picture/" + mark + ".png"), (30, 30)
    )


def bot_banner(banner):
    return pygame.transform.scale(
        pygame.image.load("picture/" + banner + ".png"), (150, 30)
    )


# เพิ่มภาพ

# start game
screen = pygame.display.set_mode((screen_width, screen_height))


# font
def font(size):
    return pygame.font.Font("font/Merriweather-Black.ttf", size)
