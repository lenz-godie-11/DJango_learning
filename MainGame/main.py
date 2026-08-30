import pygame 
import random


#creating the game environment 

x = pygame.init()

width_of_screen = 900
height_of_screen = 600

gameWindow = pygame.display.set_mode((width_of_screen,height_of_screen))
pygame.display.set_caption("python snake game PythonGeeks") 
pygame.display.update()

clock = pygame.time.Clock()

def score_on_screen(text,color,x,y): 
    screen_text = font.render(text, True , color) 
    gameWindow.blit(screen_text,[x,y])


    def welcome(): game_exit = False while not game_exit:
         gameWindow.fill((255,182,193)) 
         score_on_screen("Welcome to snakes game by PythonGeeks",black,90,250)
         score_on_screen("Press spacebar to play",black,232,290) 
         for event in pygame.event.get():
              if event.type==pygame.QUIT: 
                  game_exit = True if event.type==pygame.KEYDOWN: 
                  if event.key==pygame.K_SPACE: game()
                  pygame.display.update() 
                  clock.tick(60)