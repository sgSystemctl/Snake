# Example file showing a circle moving on screen
from time import sleep
import pygame
from snake import Snake

SCREEN_W = 400
SCREEN_H = 400
SCREEN_COLOR = "black"

#color
white = (255,255,255)
black = (0,0,0)
blue = (0,0,0xff)

# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
clock = pygame.time.Clock()
snake = Snake(SCREEN_H,SCREEN_W)
running = True

FONT_SIZE = 48
#creazione menu
font = pygame.font.Font(None,FONT_SIZE)

#creazione buttoni
start_button_text = font.render("Gioca",True,white)
option_button_text = font.render("Opzioni",True,white)
end_button_text = font.render("Esci",True,white)

#schermata vittoria
final_font = pygame.font.Font(None,100)
win = final_font.render("HAI VINTO",True,white)
defeat = final_font.render("HAI PERSO",True,white)

rect_win = win.get_rect(center=(SCREEN_W/2,SCREEN_H/2))
rect_lose = defeat.get_rect(center=(SCREEN_W/2,SCREEN_H/2))

#Involucro dei bottoni
start_button_rect = start_button_text.get_rect(center=(SCREEN_W/2,(SCREEN_H/3)+FONT_SIZE))
option_button_rect = option_button_text.get_rect(center=(SCREEN_W/2,(SCREEN_H/3)+FONT_SIZE*2))
end_button_rect = end_button_text.get_rect(center=(SCREEN_W/2,(SCREEN_H/3)+FONT_SIZE*3))

def drawCell(i,j,c):
    if c == '.': return
    color = {'M': 'red', 'T':'green', 'D':'darkgreen'}[c]
    pygame.draw.circle(screen, color, (3+j*10,3+i*10), 5)

game = False

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Controllo del clic sui bottoni
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if start_button_rect.collidepoint(event.pos):
                game = True
            if end_button_rect.collidepoint(event.pos):
                running = False

    #disegno bottoni
    if not game:
        screen.blit(start_button_text,start_button_rect)
        screen.blit(option_button_text,option_button_rect)
        screen.blit(end_button_text,end_button_rect)
        pygame.display.flip()

    screen.fill(SCREEN_COLOR)

    if game:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            snake.direction("w")
        elif keys[pygame.K_s]:
            snake.direction("s")
        elif keys[pygame.K_a]:
            snake.direction("a")
        elif keys[pygame.K_d]:
            snake.direction("d")

        if not snake.move():
            screen.blit(defeat,rect_lose)
            running = False
            pygame.display.flip()
            sleep(1)    
            continue

        if snake.win():
            screen.blit(win,rect_win)
            running = False
            pygame.display.flip()
            sleep(1)
            continue


        # usa drawCell per disegnare ogni cella della griglia di gioco
        snake.draw(drawCell)

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(10+snake.score) / 1000

pygame.quit()
