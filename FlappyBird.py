import pyglet
from pyglet import gl

#OKNO
SIRKA = 925
VYSKA = 500

#PREKAZKA
VYSKA_PODSTAVY = 15
SIRKA_PODSTAVY = 50
SIRKA_PREKAZKY = 30
MEDZERA = 80

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

def vykresli():
    vykresli_pozadie()
    vykresli_podlahu()

window = pyglet.window.Window(width=SIRKA,height=VYSKA)
window.push_handlers(
    on_draw=vykresli,

)


pyglet.app.run() 