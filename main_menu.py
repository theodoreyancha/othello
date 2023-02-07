import pygame, sys
from button import Button
import Othello_AI
import Othello_AI_Pruning
import Othello_PVP

pygame.init()

SCREEN = pygame.display.set_mode((1000, 680))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.jpg")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/sewer.ttf", size)

def othello_AI():
    while True:
        SCREEN.fill("black")
        Othello_AI.main()
    
def othello_AI_Pruning():
    while True:
        SCREEN.fill("black")
        Othello_AI_Pruning.main()

def othello_PVP():
    while True:
        SCREEN.fill("black")
        Othello_PVP.main()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("OTHELLO", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(525, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(510, 250), 
                            text_input="AI", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(510, 370), 
                            text_input="AI-Pruning", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON2 = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(510, 490), 
                            text_input="PVP", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(510, 610), 
                            text_input="QUIT", font=get_font(50), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, OPTIONS_BUTTON2, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    othello_AI()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    othello_AI_Pruning()
                if OPTIONS_BUTTON2.checkForInput(MENU_MOUSE_POS):
                    othello_PVP()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()