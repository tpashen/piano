from pygame import*
from settings import WINDOW_WIDTH, WINDOW_HEIGHT, WHITE, KEYS
from keys import create_key_rects, draw_keys
from sounds import load_sounds
from buttons import Button

init()
screen = display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
running = True

sounds = load_sounds(KEYS)
key_rects = create_key_rects(len(KEYS))
keys_list =  list(KEYS.keys())
my_font = font.SysFont("Arial", 24)
pressed_keys = set()
while running:
    draw_keys(screen, key_rects, pressed_keys)
    display.flip()
    
    for e in event.get():
        if e.type == QUIT:
            running = False
    screen.fill(WHITE)
    
    display.update()
