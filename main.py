import sys
import pygame

order = 1
total = pow(pow(order, 2), 2)

pygame.init()
window_size = (800, 800)
pygame.display.set_caption("Hilbert Curve Example")

screen = pygame.display.set_mode(window_size, pygame.HWSURFACE | pygame.DOUBLEBUF)
clock = pygame.time.Clock()


while True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()


    pygame.display.flip()
    clock.tick(60)
