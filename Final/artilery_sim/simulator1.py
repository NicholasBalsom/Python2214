# import calculator
import pygame
import geopy

# pygame setup
pygame.init()
WIDTH, HEIGHT = 400, 100
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.scrap.init()

WHITE, BLACK = (255,255,255), (0,0,0)
STAN_FONT = pygame.font.SysFont("Times New Roman", 15) #STANdard font

FPS = 60

def main():
    state_switch_box = pygame.Rect(250,HEIGHT/2-30,100,20)
    input_state = "Your lat/long and Altitude"
    coord_active = True
    coord_box = pygame.Rect(50,HEIGHT/2-10,300,20)
    coord_text = ""
    clock = pygame.time.Clock()
    running = True
    while running:
        # poll for events
        for event in pygame.event.get():
            keys_pressed = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                running = False
            # proccesing inputs for textbox
            elif event.type == pygame.MOUSEBUTTONDOWN and coord_box.collidepoint(event.pos) == True:
                coord_active = True
                coord_text = ""
            elif event.type == pygame.KEYDOWN and coord_active == True:
                if event.key == pygame.K_RETURN:
                    coord_text = ""
                elif event.key == pygame.K_BACKSPACE:
                    coord_text = coord_text[:-1]
                elif keys_pressed[pygame.K_LCTRL] and keys_pressed[pygame.K_v]:
                    coord_text += str(pygame.scrap.get(pygame.SCRAP_TEXT)).strip("b'x0\\")
                else:
                    coord_text += event.unicode
            elif event.type == pygame.MOUSEBUTTONDOWN and state_switch_box.collidepoint(event.pos) == True:
                if input_state == "Your lat/long and Altitude":
                    input_state = "Target lat/long and Altitude"
                else:
                    input_state = "Your lat/long and Altitude"

        # fill the screen with a color to wipe away anything from last frame
        WIN.fill("white")
        #renders textbox and assosciated text
        coord_text_surf = STAN_FONT.render(coord_text, True,"black")
        WIN.blit(coord_text_surf,(coord_box))
        pygame.draw.rect(WIN,"black",(coord_box),1)

        state_switch_surf = STAN_FONT.render("Switch Mode", True, "black")
        WIN.blit(state_switch_surf,(state_switch_box))
        pygame.draw.rect(WIN,"black",state_switch_box,1)
        input_state_surf = STAN_FONT.render(input_state, True, "black")
        WIN.blit(input_state_surf, (50,HEIGHT/2-30,300,20))

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()