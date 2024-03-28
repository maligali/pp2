import pygame as pg
import time

pg.init()
taspa=pg.mixer.music.load("compass.mp3")
kairat=pg.mixer.music.queue('stargazing.mp3')
fujii=pg.mixer.music.queue("sw.mp3")
clock = pg.time.Clock()
pg.mixer.music.play(-1) 
screen=pg.display.set_mode((1200,800))

songlist=["compass.mp3", "stargazing.mp3","sw.mp3"]
curr_song=None

run=True
play=False
i=0
while run:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            run=False
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_SPACE:
                play=not play
                if play:
                    pg.mixer.music.pause()
                else:
                    pg.mixer.music.unpause()
            elif event.key==pg.K_RIGHT:
                i+=1
                if i>=len(songlist):
                    i=i-len(songlist)
                pg.mixer.music.load(songlist[i])
                pg.mixer.music.play()
            elif event.key==pg.K_LEFT:
                i=i-1
                if i<0:
                    i=i+len(songlist)
                pg.mixer.music.load(songlist[i])
                pg.mixer.music.play()

    pg.display.flip()
    clock.tick(60)