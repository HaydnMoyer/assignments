import pygame
pygame.init()
# clock = pygame.time.Clock()
screenname = pygame.display.set_mode((1900, 1050))
# my_image = pygame.image.load("images/puck_small.png")
# image_rect = my_image.get_rect( center=(320,240))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

screenname.fill((100, 200, 100))
# image_rect.x += 1  # Move the image to the right

# if image_rect.x > screen.get_width(): # if the image goes off the right side of the screen,
 #image.rect.x = -image_rect.width  # move it back to the left side of the screen
 #screen.blit(my_image, image_rect)
 pygame.display.flip()
 #clock.tick(60)  # Limit the frame rate to 60 FPS
 