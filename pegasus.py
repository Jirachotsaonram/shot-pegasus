import pygame as py
import time
py.init()
window=py.display.set_mode((1000,600))
py.display.set_caption("Pegasus Game")
icon=py.image.load("1792898.png")
py.display.set_icon(icon)
background=py.image.load("snowymountains.png")
player=py.image.load('1176901-middle-removebg-preview.png')


while True:
    for event in py.event.get():
        if event.type==py.QUIT:
            quit()

    window.blit(background,(0,-360))
    window.blit(player,(0,0))
    py.display.update()
