import pygame
import random
import sys

pygame.init()
screen = pygame.display.set_mode((720,600))

c1 = random.randint(0,255)
c2 = random.randint(0,255)
c3 = random.randint(0,255)

clock = pygame.time.Clock()
while True:
	for ev in pygame.event.get():
		if ev.type == pygame.QUIT:
			pygame.quit()
			

	if 0 < c1 < 255:
		c1 += 1
	elif c1 >= 255:
		c1 -= 255
	elif c1 <= 0:
		c1 += 3

	clock.tick(60)
	screen.fill((c1,c2,c3))
	pygame.display.update()
