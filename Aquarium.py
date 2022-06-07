import pygame
import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from pygame.locals import *
from math import *

bubbleYaxis = -4.0

points = [-0.1, -0.19, -0.28, -0.37, -0.46, -
          0.55, -0.64, -0.73, -0.82, -0.91, -1.0]
value = [-3.6, -3.4, -3.2, - 3.0, -2.8, -2.6, -2.4, -
         2.2, -2.0, -1.8, -1.6, -1.4, -1.2, -1.0, -0.8, -0.6, 2.8, 2.6, 2.4,
         2.2, 2.0, 1.8, 1.6, 1.4, 1.2, 1.0, 0.8, 0.6]


def init():
    pygame.init()
    display = (900, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)


def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(6.0)

    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    glBegin(GL_POLYGON)
    glColor3f(0.118, 0.565, 1.000)
    glVertex2f(-1.0, 1.0)
    glVertex2f(1.0, 1.0)
    glColor3ub(230, 126, 34)
    glVertex2f(1.0, -1.0)
    glVertex2f(-1.0, -1.0)
    glVertex2f(-1.0, 1.0)
    # glColor3f(66/255., 161/255., 198/255.)
    # glVertex2f(0, 0.)
    glEnd()
    glBegin(GL_POLYGON)
    glColor3f(0.118, 0.565, 1.000)
    glVertex2f(-1.0, 1.0)
    glVertex2f(1.0, 1.0)
    glVertex2f(1.0, -1.0)
    glVertex2f(-1.0, -1.0)
    glVertex2f(-1.0, 1.0)
    glEnd()

    glLoadIdentity()
    # glTranslated(0.0, bubbleYaxis, 0.0)
    for i in points:
        glPushMatrix()
        glScalef(1.0, 1.0, 0.0)
        glTranslated(0.8, i, 0.0)
        posx, posy = 0, 0
        sides = 32
        radius = 0.03
        glBegin(GL_LINE_LOOP)
        glColor3f(1.0, 1.0, 1.0)
        for i in range(100):
            cosine = radius * cos(i*2*pi/sides)+posx
            sine = radius * sin(i*2*pi/sides)+posy
            glVertex2f(cosine, sine)
        glEnd()
        glPopMatrix()

    for i in points:
        glPushMatrix()
        glScalef(1.0, 1.0, 0.0)
        glTranslated(-0.9, i, 0.0)
        posx, posy = 0, 0
        sides = 32
        radius = 0.03
        glBegin(GL_LINE_LOOP)
        glColor3f(1.0, 1.0, 1.0)
        for i in range(100):
            cosine = radius * cos(i*2*pi/sides)+posx
            sine = radius * sin(i*2*pi/sides)+posy
            glVertex2f(cosine, sine)
        glEnd()
        glPopMatrix()

    glPushMatrix()
    for k in value:

        glPushMatrix()
        glScalef(0.3, 0.3, 0.0)
        glTranslated(k, -3.5, 0.0)
        # glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

        glBegin(GL_POLYGON)
        glColor3f(0.0, 1.0, 0.0)
        glVertex3f(0.4, -0.4, 0.0)

        glVertex3f(0.35, 0.75, 0.0)
        glVertex3f(0.2, 0.35, 0.0)
        glEnd()

        glBegin(GL_LINES)
        glColor3f(1.0, 1.0, 1.0)
        glVertex3f(0.35, 0.75, 0.0)
        glVertex3f(0.4, -0.4, 0.0)
        glEnd()
        glBegin(GL_POLYGON)
        glColor3f(0.0, 1.0, 0.0)
        glVertex3f(0.4, -0.4, 0.0)
        glVertex3f(0.5, 0.35, 0.0)
        glVertex3f(0.35, 0.75, 0.0)
        glEnd()
        glPopMatrix()
    glPopMatrix()

    glPushMatrix()
    glScalef(1.0, 1.0, 0.0)
    glTranslated(0.1, -1.0, 0.0)
    posx, posy = 0, 0
    sides = 32
    radius = 0.2
    glBegin(GL_POLYGON)
    glColor3f(0.36, 0.25, 0.20)
    for i in range(100):
        cosine = radius * cos(i*2*pi/sides)+posx
        sine = radius * sin(i*2*pi/sides)+posy
        glVertex2f(cosine, sine)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glScalef(1.0, 1.0, 0.0)
    glTranslated(-0.9, -1.0, 0.0)
    posx, posy = 0, 0
    sides = 32
    radius = 0.1
    glBegin(GL_POLYGON)
    glColor3f(0.36, 0.25, 0.20)
    for i in range(100):
        cosine = radius * cos(i*2*pi/sides)+posx
        sine = radius * sin(i*2*pi/sides)+posy
        glVertex2f(cosine, sine)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glScalef(1.0, 1.0, 0.0)
    glTranslated(-0.4, 0.0, 0.0)
    # glColor3f(0.4, 0.0, 0.0)
    glColor3f(0.0, 0.0, 0.1)
    glBegin(GL_POLYGON)
    glVertex2f(0.0, -0.0)
    glVertex2f(0.2, 0.1)
    glVertex2f(0.2, -0.1)
    glColor3f(0.412, 0.412, 0.412)
    glVertex2f(0.5, -0.0)
    glVertex2f(0.2, 0.1)
    glEnd()
    glColor3f(0.863, 0.863, 0.863)
    glTranslated(0.051, -0.05, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(0.3, 0.05)
    glColor3f(0.412, 0.412, 0.412)
    glVertex2f(0.5, 0.15)
    glVertex2f(0.5, -0.05)
    
    glEnd()
    glPointSize(4.0)
    glColor3f(1.0, 1.0, 0.0)
    glBegin(GL_POINTS)
    glVertex2f(0.02, 0.05)
    glEnd()

    glColor3f(1.0, 1.0, 1.0)
    glTranslated(-0.015, 0.03, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(0.1, -0.04)
    glColor3f(0.412, 0.412, 0.412)
    glVertex2f(0.19, -0.03)
    glVertex2f(0.25, -0.13)
    glColor3f(0.863, 0.863, 0.863)
    glVertex2f(0.1, 0.08)
    glColor3f(0.412, 0.412, 0.412)
    glVertex2f(0.19, 0.07)
    glVertex2f(0.25, 0.17)

    glEnd()

    # glColor3f(0.8, 0.0, 0.0)
    # glBegin(GL_TRIANGLES)
    # glVertex2f(0.795, 0.035)
    # glVertex2f(0.77, -0.02)
    # glVertex2f(0.75, -0.007)
    # glEnd()

    glPopMatrix()

    glFlush()
    # glutSwapBuffers()


# def move_time():
#     if(bubbleYaxis > 3.0):
#         _bubbleYaxis = (-4.0)
#     bubbleYaxis += 0.02
#     glutPostRedisplay()
    # glutTimerFunc(35, move_time, 0)
    # for i in points:
    #     i += 1
    # glBegin(GL_LINE_LOOP)
    # glTranslatef(0.0, 0.5, 0.0)
    # glColor3f(1.0, 1.0, 1.0)
    # for i in range(100):
    #     cosine = radius * cos(i*2*pi/sides)+posx
    #     sine = radius * sin(i*2*pi/sides)+posy
    #     glVertex2f(cosine, sine)
    # glEnd()
    # glMatrixMode(GL_PROJECTION)
    # glLoadIdentity()
    # glOrtho(0.0, 500, 0.0, 500, -100, 100)

    # glMatrixMode(GL_MODELVIEW)
    # glLoadIdentity()

    # yellow STAR
    # glColor3f(1.0, 1.0, 0.0)
    # glBegin(GL_TRIANGLES)
    # glVertex3f(0.0, 0.2, 0.0)
    # glVertex3f(0.04, 0.08, 0.0)
    # glVertex3f(-0.04, 0.08, 0.0)
    # glVertex3f(0.04, 0.08, 0.0)
    # glVertex3f(0.17, 0.08, 0.0)
    # glVertex3f(0.07, 0.0, 0.0)
    # glVertex3f(0.07, 0.0, 0.0)
    # glVertex3f(0.12, -.14, 0.0)
    # glVertex3f(0, -.04, 0.0)
    # glVertex3f(0, -.04, 0.0)
    # glVertex3f(-0.12, -.14, 0.0)
    # glVertex3f(-0.06, 0, 0.0)
    # glVertex3f(-0.06, 0, 0.0)
    # glVertex3f(-0.16, 0.08, 0.0)
    # glVertex3f(-0.04, 0.08, 0.0)
    # glEnd()
    # glBegin(GL_POLYGON)
    # glVertex3f(0.04, 0.08, 0.0)
    # glVertex3f(0.07, 0.0, 0.0)
    # glVertex3f(0, -.04, 0.0)
    # glVertex3f(-0.07, 0.0, 0.0)
    # glVertex3f(-0.04, 0.08, 0.0)
    # glEnd()


def main():
    init()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        draw()
        # glutTimerFunc(35, move_time, 0)
        # glutMainLoop()
        pygame.display.flip()
        pygame.time.wait(10)


main()
