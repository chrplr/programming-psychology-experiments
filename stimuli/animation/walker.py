#! /usr/bin/env python
# time-stamp: < mer. 02 oct. 2024 10:05:33 CEST  christophe@pallier.org>

from PIL import Image
import pygame


im = Image.open("foo.png")
w, h = im.size
n_images = 4
w0 = w // n_images

crop_rects = [(i * w0, 0, (i + 1) * w0 - 1, h) for i in range(n_images)]

pygame.init()
screen = pygame.display.set_mode((w0, h))
pygame.display.set_caption("Walker")

pygame_images = []

for i, rect in enumerate(crop_rects):
    crop_im = im.crop(rect)
    image_data = crop_im.tobytes()
    image_dimensions = crop_im.size
    pygame_images.append(pygame.image.fromstring(image_data, image_dimensions, "RGB"))


speed = 4  # img / sec
frame = 0

# loop until the window is closed
quit_button_pressed = False
while not quit_button_pressed:
    screen.blit(pygame_images[frame % n_images], (0, 0))
    pygame.display.flip()
    frame = frame + 1
    pygame.time.wait(1000 // speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_button_pressed = True
        if event.type == pygame.KEYDOWN:
            quit_button_pressed = True

pygame.quit()


