import pygame as py
import win32api
import win32con
import win32gui

py.init() 
window_screen = py.display.set_mode((700, 450))
hwnd = py.display.get_wm_info()["window"]
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
                        | win32con.WS_EX_LAYERED)
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(255, 0, 128), 0, win32con.LWA_COLORKEY)
font = py.font.SysFont("Times New Roman", 54)
text = []
text.append((font.render("Transparent Window", 0, (255, 100, 0)), (20, 10))) 
text.append((font.render("Press Esc to close the window", 0, (255, 100, 100)), (20, 250)))

def show_text(): 
    for t in text:
        window_screen.blit(t[0], t[1])

done = 0
while not done: 
    for event in py.event.get(): 
        if event.type == py.QUIT: 
            done = 1			
        if event.type == py.KEYDOWN: 
            if event.key == py.K_ESCAPE: 
                done = 1
    window_screen.fill((255,0,128)) 
    show_text() 
    py.display.update()