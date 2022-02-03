import pyglet
from pyglet import gl

#OKNO
SIRKA = 925
VYSKA = 500

RYCHLOST = 100

#PREKAZKA
VYSKA_PODSTAVY = 15
SIRKA_PODSTAVY = 50
SIRKA_PREKAZKY = 30
MEDZERA = 80 #medzera medzi hornou a dolnou castou prekazky

#HRAC
VYSKA_HRACA = 30
SIRKA_HRACA = 30

pozicia_hraca = [100,200]
pozicia_prekazky1 = [300,250]
pozicia_prekazky2 = [600,200]
pozicia_prekazky3 = [900,300]
body = [0]

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



def vykresli():
    vykresli_pozadie()
    vykresli_prekazku1()
    vykresli_prekazku2()
    vykresli_prekazku3()
    vykresli_podlahu()
    
def obnov_stav(dt):
    #pohyb prekazok
    pozicia_prekazky1[0] -= RYCHLOST * dt
    pozicia_prekazky2[0] -= RYCHLOST * dt
    pozicia_prekazky3[0] -= RYCHLOST * dt

window = pyglet.window.Window(width=SIRKA,height=VYSKA)
window.push_handlers(
    on_draw=vykresli,
    
)
#nastavenie FPS na 60 kvôli výpočtom
pyglet.clock.schedule_interval(obnov_stav, 1/60)

pyglet.app.run() 