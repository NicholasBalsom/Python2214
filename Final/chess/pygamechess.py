import pygame
import os

# pygame setup
pygame.init()

WIDTH, HEIGHT = 1280, 720
PIECE_WIDTH, PIECE_HEIGHT = 40, 55

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CHESS")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FPS = 60

BORDER = pygame.Rect(WIDTH / 2 - 5, 0, 10, HEIGHT)
BOARD = pygame.transform.scale(pygame.image.load(os.path.join('Final-Project', 'chess', 'assets', 'chessboard.png')), (720, 720))

def draw_window():
    WIN.blit(BOARD, (WIDTH/2-360, 0))


def main():
    clock = pygame.time.Clock()
    running = True

    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        # fill the screen with a color to wipe away anything from last frame
        

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(FPS)  # limits FPS

        draw_window()

    pygame.quit()

if __name__ == "__main__":
    main()