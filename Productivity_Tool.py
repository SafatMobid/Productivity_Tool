import pygame

pygame.init()

window_size = (600, 600) # Control Window Size
screen = pygame.display.set_mode((window_size)) #Create window
#screen = pygame.display.set_mode(window_size, pygame.NOFRAME) #Create borderless screen

#Using border for now for quicker exit till I create a close button

# Create a semi-transparent black surface
overlay = pygame.Surface(window_size, pygame.SRCALPHA)
overlay.fill((0, 0, 0, overlay.full)) #150

# Draw the overlay on the screen
screen.blit(overlay, (0,0))
pygame.display.flip()

# Event loop to keep the window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()