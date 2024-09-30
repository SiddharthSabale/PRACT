import pygame as pg
import sys

pg.init()
screen_width, screen_height = 800, 600
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("Collision Detection and Audio Example")

pg.mixer.init()
collision_sound = pg.mixer.Sound("npc_pain.mp3")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

circle_radius = 30
circle_color = BLUE

def draw_circle(position):
    pg.draw.circle(screen, circle_color, position, circle_radius)

def play_collision_sound():
    collision_sound.play()

def check_collision(circle_pos, rect):
    circle_x, circle_y = circle_pos
    rect_x, rect_y, rect_width, rect_height = rect

    if (circle_x >= rect_x and circle_x <= rect_x + rect_width and
        circle_y >= rect_y and circle_y <= rect_y + rect_height):
        return True
    return False

running = True
while running:
    screen.fill(WHITE)
    
    rect_width, rect_height = 100, 100
    rect_x, rect_y = 350, 250
    pg.draw.rect(screen, RED, (rect_x, rect_y, rect_width, rect_height))

    mouse_pos = pg.mouse.get_pos()
    draw_circle(mouse_pos)

    if check_collision(mouse_pos, (rect_x, rect_y, rect_width, rect_height)):
        play_collision_sound()


    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    pg.display.flip()

pg.quit()
sys.exit()