import pyglet
from pyglet import gl
from random import randint
from pyglet.window import key
import time

#OKNO
SIRKA = 1000
VYSKA = 500

VELKOST_FONTU = 42

RYCHLOST = 100

#PREKAZKA
VYSKA_PODSTAVY = 15
SIRKA_PODSTAVY = 50
SIRKA_PREKAZKY = 30
MEDZERA = 120 #medzera medzi hornou a dolnou castou prekazky

#HRAC
VYSKA_HRACA = 20
SIRKA_HRACA = 26

pozicia_hraca = [100,250]
pozicia_prekazky1 = [800,250]
pozicia_prekazky2 = [1100,200]
pozicia_prekazky3 = [1400,300]
pozicia_prekazky4 = [1700, 100]
body = 0
stisknuta_klavesnica = [0]
rychlost_hraca_y = [1]
moznost_skakat = [1]
moznost_hrat = [0]
zaciatok = [0]
najvyssie_skore = 0
moznost_ziskat_bod = 1

#pridanie obrázku
flappy = pyglet.image.load('flappy3.png')
flappy_down = pyglet.image.load('flappy_down.png')
hrac = pyglet.sprite.Sprite(flappy)
hrac.x = pozicia_hraca[0]
hrac.y = pozicia_hraca[1]

#zmena flappy_bird obrazku(veľmi náročné na hradwere)
# def zmen(t):
#     hrac.image = flappy_down
#     pyglet.clock.schedule_once(zmen_nazad, 1)

# def zmen_nazad(t):
#     hrac.image = flappy
#     pyglet.clock.schedule_interval(zmen, 1)

# pyglet.clock.schedule_interval(zmen, 1)


def vykresli_obdlznik(x1,y1,x2,y2):
    gl.glBegin(gl.GL_TRIANGLE_FAN)  
    gl.glVertex2f(int(x1), int(y1))  
    gl.glVertex2f(int(x1), int(y2))  
    gl.glVertex2f(int(x2), int(y2))  
    gl.glVertex2f(int(x2), int(y1))  
    gl.glEnd()

def vykresli_pozadie():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    gl.glColor3f(0, 0.75, 1)

    vykresli_obdlznik(
        0,
        0,
        SIRKA,
        VYSKA
    )

def vykresli_podlahu():
    gl.glColor3f(0.2,0.6,0.2)
    vykresli_obdlznik(
        0,
        0,
        SIRKA,
        50
    )
def nakresli_text(text, x ,y, pozice_x):
    napis = pyglet.text.Label(text, font_size=VELKOST_FONTU, x=x, y=y, anchor_x=pozice_x)
    napis.draw()

def vykresli_prekazku1():
    #dolna cast
    #__________
    #vykresli podstavu
    gl.glColor3f(0.11, 0.59 , 0.11 )
    vykresli_obdlznik(
        pozicia_prekazky1[0] - SIRKA_PODSTAVY//2,
        pozicia_prekazky1[1] - MEDZERA//2 - VYSKA_PODSTAVY,
        pozicia_prekazky1[0] + SIRKA_PODSTAVY//2,
        pozicia_prekazky1[1] - MEDZERA//2
    )
    #vykresli cast pod podstavou
    gl.glColor3f(0.1, 0.8, 0.1)
    vykresli_obdlznik(
        pozicia_prekazky1[0] - SIRKA_PREKAZKY//2,
        0,
        pozicia_prekazky1[0] + SIRKA_PREKAZKY//2,
        pozicia_prekazky1[1]-MEDZERA//2-VYSKA_PODSTAVY
    )
    #horna cast
    gl.glColor3f(0.11,0.59,0.11)
    vykresli_obdlznik(
        pozicia_prekazky1[0] - SIRKA_PODSTAVY//2,
        pozicia_prekazky1[1] + MEDZERA//2,
        pozicia_prekazky1[0] + SIRKA_PODSTAVY//2,
        pozicia_prekazky1[1] + MEDZERA//2 + VYSKA_PODSTAVY
    )
    #vykresli cast nad hornou podstavou
    gl.glColor3f(0.1, 0.8, 0.1)
    vykresli_obdlznik(
        pozicia_prekazky1[0] - SIRKA_PREKAZKY//2,
        pozicia_prekazky1[1] + MEDZERA//2 + VYSKA_PODSTAVY,
        pozicia_prekazky1[0] + SIRKA_PREKAZKY//2,
        VYSKA
    )
def vykresli_prekazku2():
    #dolna cast
    #__________
    #vykresli podstavu
    gl.glColor3f(0.11, 0.59 , 0.11 )
    vykresli_obdlznik(
        pozicia_prekazky2[0] - SIRKA_PODSTAVY//2,
        pozicia_prekazky2[1] - MEDZERA//2 - VYSKA_PODSTAVY,
        pozicia_prekazky2[0] + SIRKA_PODSTAVY//2,
        pozicia_prekazky2[1] - MEDZERA//2
    )
    #vykresli cast pod podstavou
    gl.glColor3f(0.1, 0.8, 0.1)
    vykresli_obdlznik(
        pozicia_prekazky2[0] - SIRKA_PREKAZKY//2,
        0,
        pozicia_prekazky2[0] + SIRKA_PREKAZKY//2,
        pozicia_prekazky2[1]-MEDZERA//2-VYSKA_PODSTAVY
    )
    #horna cast
    gl.glColor3f(0.11,0.59,0.11)
    vykresli_obdlznik(
        pozicia_prekazky2[0] - SIRKA_PODSTAVY//2,
        pozicia_prekazky2[1] + MEDZERA//2,
        pozicia_prekazky2[0] + SIRKA_PODSTAVY//2,
        pozicia_prekazky2[1] + MEDZERA//2 + VYSKA_PODSTAVY
    )
    #vykresli cast nad hornou podstavou
    gl.glColor3f(0.1, 0.8, 0.1)
    vykresli_obdlznik(
        pozicia_prekazky2[0] - SIRKA_PREKAZKY//2,
        pozicia_prekazky2[1] + MEDZERA//2 + VYSKA_PODSTAVY,
        pozicia_prekazky2[0] + SIRKA_PREKAZKY//2,
        VYSKA
    )
def vykresli_prekazku3():
    #dolna cast
    #__________
    #vykresli podstavu
    gl.glColor3f(0.11, 0.59 , 0.11 )
    vykresli_obdlznik(
        pozicia_prekazky3[0] - SIRKA_PODSTAVY//2,
        pozicia_prekazky3[1] - MEDZERA//2 - VYSKA_PODSTAVY,
        pozicia_prekazky3[0] + SIRKA_PODSTAVY//2,
        pozicia_prekazky3[1] - MEDZERA//2
    )
    #vykresli cast pod podstavou
    gl.glColor3f(0.1, 0.8, 0.1)
    vykresli_obdlznik(
        pozicia_prekazky3[0] - SIRKA_PREKAZKY//2,
        0,
        pozicia_prekazky3[0] + SIRKA_PREKAZKY//2,
        pozicia_prekazky3[1]-MEDZERA//2-VYSKA_PODSTAVY
    )
    #horna cast
    gl.glColor3f(0.11,0.59,0.11)
    vykresli_obdlznik(
        pozicia_prekazky3[0] - SIRKA_PODSTAVY//2,
        pozicia_prekazky3[1] + MEDZERA//2,
        pozicia_prekazky3[0] + SIRKA_PODSTAVY//2,
        pozicia_prekazky3[1] + MEDZERA//2 + VYSKA_PODSTAVY
    )
    #vykresli cast nad hornou podstavou
    gl.glColor3f(0.1, 0.8, 0.1)
    vykresli_obdlznik(
        pozicia_prekazky3[0] - SIRKA_PREKAZKY//2,
        pozicia_prekazky3[1] + MEDZERA//2 + VYSKA_PODSTAVY,
        pozicia_prekazky3[0] + SIRKA_PREKAZKY//2,
        VYSKA
    )
def vykresli_prekazku4():
    #dolna cast
    #__________
    #vykresli podstavu
    gl.glColor3f(0.11, 0.59 , 0.11 )
    vykresli_obdlznik(
        pozicia_prekazky4[0] - SIRKA_PODSTAVY//2,
        pozicia_prekazky4[1] - MEDZERA//2 - VYSKA_PODSTAVY,
        pozicia_prekazky4[0] + SIRKA_PODSTAVY//2,
        pozicia_prekazky4[1] - MEDZERA//2
    )
    #vykresli cast pod podstavou
    gl.glColor3f(0.1, 0.8, 0.1)
    vykresli_obdlznik(
        pozicia_prekazky4[0] - SIRKA_PREKAZKY//2,
        0,
        pozicia_prekazky4[0] + SIRKA_PREKAZKY//2,
        pozicia_prekazky4[1]-MEDZERA//2-VYSKA_PODSTAVY
    )
    #horna cast
    gl.glColor3f(0.11,0.59,0.11)
    vykresli_obdlznik(
        pozicia_prekazky4[0] - SIRKA_PODSTAVY//2,
        pozicia_prekazky4[1] + MEDZERA//2,
        pozicia_prekazky4[0] + SIRKA_PODSTAVY//2,
        pozicia_prekazky4[1] + MEDZERA//2 + VYSKA_PODSTAVY
    )
    #vykresli cast nad hornou podstavou
    gl.glColor3f(0.1, 0.8, 0.1)
    vykresli_obdlznik(
        pozicia_prekazky4[0] - SIRKA_PREKAZKY//2,
        pozicia_prekazky4[1] + MEDZERA//2 + VYSKA_PODSTAVY,
        pozicia_prekazky4[0] + SIRKA_PREKAZKY//2,
        VYSKA
    )


def vykresli():
    vykresli_pozadie()
    vykresli_prekazku1()
    vykresli_prekazku2()
    vykresli_prekazku3()
    vykresli_prekazku4()
    vykresli_podlahu()
    hrac.draw()
    nakresli_text(str(body), SIRKA - 5, VYSKA - 50, 'right')
    if moznost_hrat[0] == 0:
        nakresli_text("To START press SPACE", SIRKA//2, VYSKA//2 + 45, 'center')
        nakresli_text("HIGH SCORE: "+ str(najvyssie_skore),SIRKA//2, VYSKA//2 - 45, 'center')
    elif moznost_hrat[0] == 2:
        nakresli_text("GAME OVER", SIRKA//2, VYSKA//2 + 45, 'center')
        nakresli_text("Press SPACE to RESTART", SIRKA//2, VYSKA//2 - 45, 'center')
    
def obnov_stav(dt):
    global pozicia_hraca
    global pozicia_prekazky1
    global pozicia_prekazky2
    global pozicia_prekazky3
    global pozicia_prekazky4
    global body
    global stisknuta_klavesnica
    global rychlost_hraca_y
    global moznost_skakat 
    global moznost_hrat
    global zaciatok
    global najvyssie_skore
    global moznost_ziskat_bod


    if zaciatok[0] == 1:
        if moznost_hrat[0] == 1:
        #premiestnenie prekazok, keď prídu na koniec tak sa premiestnia na začiatok s náhodonou y-ovou súradnicou
            if pozicia_prekazky1[0] < -175:
                nova_pozicia = randint(50+MEDZERA//2, VYSKA-MEDZERA//2)
                pozicia_prekazky1[0] = SIRKA + SIRKA_PODSTAVY//2
                pozicia_prekazky1[1] = nova_pozicia
            if pozicia_prekazky2[0] < -175:
                nova_pozicia = randint(50+MEDZERA//2, VYSKA-MEDZERA//2)
                pozicia_prekazky2[0] = SIRKA + SIRKA_PODSTAVY//2
                pozicia_prekazky2[1] = nova_pozicia
            if pozicia_prekazky3[0] < -175:
                nova_pozicia = randint(50+MEDZERA//2, VYSKA-MEDZERA//2)
                pozicia_prekazky3[0] = SIRKA + SIRKA_PODSTAVY//2
                pozicia_prekazky3[1] = nova_pozicia
            if pozicia_prekazky4[0] < -175:
                nova_pozicia = randint(50+MEDZERA//2, VYSKA-MEDZERA//2)
                pozicia_prekazky4[0] = SIRKA + SIRKA_PODSTAVY//2
                pozicia_prekazky4[1] = nova_pozicia
            #pohyb prekazok
            print(pozicia_prekazky1[0])
            pozicia_prekazky1[0] -= RYCHLOST * dt
            pozicia_prekazky2[0] -= RYCHLOST * dt
            pozicia_prekazky3[0] -= RYCHLOST * dt
            pozicia_prekazky4[0] -= RYCHLOST * dt
            #kontrola kolízie
            if int(pozicia_hraca[0]) + SIRKA_HRACA + SIRKA_PODSTAVY//2 > int(pozicia_prekazky1[0]) >int(pozicia_hraca[0]) - SIRKA_PODSTAVY//2:
                if pozicia_prekazky1[1] - MEDZERA//2 + VYSKA_HRACA//2 > pozicia_hraca[1]:
                    moznost_hrat[0] = 2
                    najvyssie_skore = body
                elif pozicia_hraca[1] > pozicia_prekazky1[1] + MEDZERA//2 - VYSKA_HRACA//2:
                    moznost_hrat[0] = 2
                    najvyssie_skore = body
            if int(pozicia_hraca[0]) + SIRKA_HRACA + SIRKA_PODSTAVY//2 > int(pozicia_prekazky2[0]) >int(pozicia_hraca[0]) - SIRKA_PODSTAVY//2:
                if pozicia_prekazky2[1] - MEDZERA//2 + VYSKA_HRACA//2 > pozicia_hraca[1]:
                    moznost_hrat[0] = 2
                    najvyssie_skore = body
                elif pozicia_hraca[1] > pozicia_prekazky2[1] + MEDZERA//2 - VYSKA_HRACA//2:
                    moznost_hrat[0] = 2
                    najvyssie_skore = body
            if int(pozicia_hraca[0]) + SIRKA_HRACA + SIRKA_PODSTAVY//2 > int(pozicia_prekazky3[0]) >int(pozicia_hraca[0]) - SIRKA_PODSTAVY//2:
                if pozicia_prekazky3[1] - MEDZERA//2 + VYSKA_HRACA//2 > pozicia_hraca[1]:
                    moznost_hrat[0] = 2
                    najvyssie_skore = body
                elif pozicia_hraca[1] > pozicia_prekazky3[1] + MEDZERA//2 - VYSKA_HRACA//2:
                    moznost_hrat[0] = 2
                    najvyssie_skore = body
            if int(pozicia_hraca[0]) + SIRKA_HRACA + SIRKA_PODSTAVY//2 > int(pozicia_prekazky4[0]) >int(pozicia_hraca[0]) - SIRKA_PODSTAVY//2:
                if pozicia_prekazky4[1] - MEDZERA//2 + VYSKA_HRACA//2 > pozicia_hraca[1]:
                    moznost_hrat[0] = 2
                    najvyssie_skore = body
                elif pozicia_hraca[1] > pozicia_prekazky4[1] + MEDZERA//2 - VYSKA_HRACA//2:
                    moznost_hrat[0] = 2
                    najvyssie_skore = body 
            #kontrola bodov
            if int(pozicia_hraca[0]) + SIRKA_PODSTAVY >  pozicia_prekazky1[0] > int(pozicia_hraca[0]) - SIRKA_PODSTAVY//2:
                if moznost_ziskat_bod == 1: 
                    body += 1
                    moznost_ziskat_bod = 0
            if pozicia_hraca[0] - SIRKA_HRACA*2 > pozicia_prekazky1[0] > pozicia_hraca[0] - SIRKA_HRACA*3:
                moznost_ziskat_bod = 1
            if int(pozicia_hraca[0]) + SIRKA_PODSTAVY >  pozicia_prekazky2[0] > int(pozicia_hraca[0]) - SIRKA_PODSTAVY//2:
                if moznost_ziskat_bod == 1: 
                    body += 1
                    moznost_ziskat_bod = 0
            if pozicia_hraca[0] - SIRKA_HRACA*2 > pozicia_prekazky2[0] > pozicia_hraca[0] - SIRKA_HRACA*3:
                moznost_ziskat_bod = 1
            if int(pozicia_hraca[0]) + SIRKA_PODSTAVY >  pozicia_prekazky3[0] > int(pozicia_hraca[0]) - SIRKA_PODSTAVY//2:
                if moznost_ziskat_bod == 1: 
                    body += 1
                    moznost_ziskat_bod = 0
            if pozicia_hraca[0] - SIRKA_HRACA*2 > pozicia_prekazky3[0] > pozicia_hraca[0] - SIRKA_HRACA*3:
                moznost_ziskat_bod = 1
            if int(pozicia_hraca[0]) + SIRKA_PODSTAVY >  pozicia_prekazky4[0] > int(pozicia_hraca[0]) - SIRKA_PODSTAVY//2:
                if moznost_ziskat_bod == 1: 
                    body += 1
                    moznost_ziskat_bod = 0
            if pozicia_hraca[0] - SIRKA_HRACA*2 > pozicia_prekazky4[0] > pozicia_hraca[0] - SIRKA_HRACA*3:
                moznost_ziskat_bod = 1
        else:
            if stisknuta_klavesnica[0] == 1:
                pozicia_hraca[0] = 100
                pozicia_hraca[1] = 250
                pozicia_prekazky1[0] = 800
                pozicia_prekazky1[1] = 250
                pozicia_prekazky2[0] = 1100
                pozicia_prekazky2[1] = 200
                pozicia_prekazky3[0] = 1400
                pozicia_prekazky3[1] = 300
                pozicia_prekazky4[0] = 1700
                pozicia_prekazky4[1] = 100
                body = 0
                stisknuta_klavesnica[0] = 0
                rychlost_hraca_y[0] = 1
                moznost_skakat[0] = 1
                moznost_hrat[0] = 0
                zaciatok[0] = 0
                moznost_ziskat_bod = 1
            
        #pohyb hraca*************************
        hrac.y = pozicia_hraca[1]
        pozicia_hraca[1] = pozicia_hraca[1] + rychlost_hraca_y[0]
        hrac.y = pozicia_hraca[1]
        if pozicia_hraca[1] > 50:
            rychlost_hraca_y[0] -= 0.5
        hrac.x = pozicia_hraca[0]
        if moznost_hrat[0] == 1:
            if stisknuta_klavesnica[0] == 1:
                if moznost_skakat[0] == 1:
                    rychlost_hraca_y[0] = 6
                    moznost_skakat[0] = 0
        if pozicia_hraca[1] < 50:
            pozicia_hraca[1] = 50
            rychlost_hraca_y[0] = 0

    
def stisk_klavesnice(symbol, modifikatory):
    if symbol == key.SPACE:
        stisknuta_klavesnica[0] = 1
        moznost_hrat[0] = 1
        zaciatok[0] = 1
    if symbol == key.UP:
        stisknuta_klavesnica[0] = 1
        moznost_hrat[0] = 1
        zaciatok[0] = 1
def pusti_klavesnice(symbol, modifikatory):
    if symbol == key.SPACE:
        stisknuta_klavesnica[0] = 0
        moznost_skakat[0] = 1
    if symbol == key.UP:
        stisknuta_klavesnica[0] = 0
        moznost_skakat[0] = 1


window = pyglet.window.Window(width=SIRKA,height=VYSKA)
window.push_handlers(
    on_draw=vykresli,
    on_key_press=stisk_klavesnice,
    on_key_release=pusti_klavesnice
)
#nastavenie FPS na 60 kvôli výpočtom
pyglet.clock.schedule_interval(obnov_stav, 1/60)

pyglet.app.run()