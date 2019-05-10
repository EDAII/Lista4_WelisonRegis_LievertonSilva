import pygame

SCREEN_W, SCREEN_H = 800, 600

def main():
    pygame.init()
    pygame.display.set_caption("Sort Visualizer")

    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    # screen_w, screen_h = screen.get_size()

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        
        pygame.display.update()
        

if __name__ == '__main__':
    main()