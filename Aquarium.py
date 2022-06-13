
import pygame
import numpy as np
from pygame.locals import *
from math import *
from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys
# import math

global bubblepath
bubblepath = -0.5

points = [-0.1, -0.19, -0.28, -0.37, -0.46, -
          0.55, -0.64, -0.73, -0.82, -0.91, -1.0]
value = [-3.6, -3.4, -3.2, - 3.0, -2.8, -2.6, -2.4, -
         2.2, -2.0, -1.8, -1.6, -1.4, -1.2, -1.0, -0.8, -0.6, 2.8, 2.6, 2.4,
         2.2, 2.0, 1.8, 1.6, 1.4, 1.2, 1.0, 0.8, 0.6]


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)


def move_time(key):
    global bubblepath
    if(bubblepath > 2.0):
        bubblepath = -0.5
    bubblepath += 0.02

    glutPostRedisplay()
    glutTimerFunc(5, move_time, 0)


def circle_bubbles():
    glLoadIdentity()

    for l in points:
        glPushMatrix()
        glScalef(1.0, 1.0, 0.0)
        glTranslated(0.8, l, 0.0)
        posx, posy = 0, 0
        sides = 32
        radius = 0.03
        glTranslated(0.0, bubblepath, 0.0)
        glBegin(GL_LINE_LOOP)
        glColor3f(1.0, 1.0, 1.0)
        for i in range(200):
            cosine = radius * cos(i*2*pi/sides)
            sine = radius * sin(i*2*pi/sides)
            glVertex2f(cosine, sine)
        glEnd()
        glPopMatrix()

    for k in points:
        glPushMatrix()
        glScalef(1.0, 1.0, 0.0)
        glTranslated(-0.9, k, 0.0)
        posx, posy = 0, 0
        sides = 32
        radius = 0.03
        glTranslated(0.0, bubblepath, 0.0)
        glBegin(GL_LINE_LOOP)
        glColor3f(1.0, 1.0, 1.0)
        for i in range(100):
            cosine = radius * cos(i*2*pi/sides)
            sine = radius * sin(i*2*pi/sides)
            glVertex2f(cosine, sine)
        glEnd()
        glPopMatrix()
    glutSwapBuffers()

    # glFlush()


def fish1():
    glPushMatrix()
    glScalef(1.0, 1.0, 0.0)
    glTranslated(-0.4, 0.0, 0.0)
    # glColor3f(0.4, 0.0, 0.0)
    # first fish
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
    glPopMatrix()
    glFlush()


def fish2():
    glPushMatrix()
    glScalef(1.0, 1.0, 0.0)
    glTranslated(-0.4, 0.0, 0.0)
    glColor3f(0.4, 0.0, 0.0)
    glBegin(GL_POLYGON)
    glVertex2f(0.7, -0.1)
    glVertex2f(0.75, -0.07)
    glVertex2f(0.85, -0.07)
    glVertex2f(0.90, -0.1)
    glVertex2f(0.85, -0.14)
    glVertex2f(0.75, -0.14)
    glEnd()

    glColor3f(0.863, 0.863, 0.863)
    glTranslated(0.051, -0.05, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(0.83, -0.05)
    glColor3f(0.412, 0.412, 0.412)
    glVertex2f(0.9, -0.09)
    glVertex2f(0.9, -0.01)
    glEnd()
    glPointSize(4.0)
    glColor3f(1.0, 1.0, 0.0)
    glBegin(GL_POINTS)
    glVertex2f(0.7, -0.036)
    glEnd()

    glColor3f(1.0, 1.0, 1.0)
    glTranslated(-0.015, 0.03, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(0.79, -0.125)
    glVertex2f(0.77, -0.07)
    glVertex2f(0.75, -0.095)
    glEnd()

    glPopMatrix()
    glFlush()


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
    # alternative water color
    # glBegin(GL_POLYGON)
    # glColor3f(0.118, 0.565, 1.000)
    # glVertex2f(-1.0, 1.0)
    # glVertex2f(1.0, 1.0)
    # glVertex2f(1.0, -1.0)
    # glVertex2f(-1.0, -1.0)
    # glVertex2f(-1.0, 1.0)
    # glEnd()
    #full sky blue ###
    glPushMatrix()
    for k in value:

        glPushMatrix()
        glScalef(0.3, 0.3, 0.0)
        glTranslated(k, -3.5, 0.0)
        # glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

        glBegin(GL_POLYGON)
        glColor3f(0.0, 1.0, 0.0)
        # glVertex3f(0.4, -0.4, 0.0)

        # glVertex3f(0.35, 0.75, 0.0)
        # glVertex3f(0.2, 0.35, 0.0)
        glEnd()

        glBegin(GL_LINES)
        # glColor3f(1.0, 1.0, 1.0)
        # glVertex3f(0.35, 0.75, 0.0)
        # glVertex3f(0.4, -0.4, 0.0)
        glEnd()
        glBegin(GL_POLYGON)
        # glColor3f(0.0, 1.0, 0.0)
        # glVertex3f(0.4, -0.4, 0.0)
        # glVertex3f(0.5, 0.35, 0.0)
        # glVertex3f(0.35, 0.75, 0.0)
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

    # dimond
    glPushMatrix()
    glColor3f(0.7255, 0.949, 1.0)
    glTranslated(-1.5, -0.5, 0.0)
    glBegin(GL_POLYGON)
    glVertex2f(1.0, -0.125)
    glVertex2f(0.92, -0.125)
    glVertex2f(0.87, -0.17)
    glVertex2f(1.05, -0.17)
    glVertex2f(0.87, -0.17)
    glVertex2f(0.96, -0.3)
    glVertex2f(1.05, -0.17)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslated(-1.5, -0.5, 0.0)
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINE_STRIP)
    glVertex2f(1.05, -0.17)
    glVertex2f(1.0, -0.19)
    glVertex2f(0.92, -0.19)
    glVertex2f(0.87, -0.17)

    glEnd()
    glPopMatrix()


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glPushMatrix()
    draw()
    glPopMatrix()

    glPushMatrix()
    fish1()
    glPopMatrix()

    glPushMatrix()
    fish2()
    glPopMatrix()

    glPushMatrix()
    circle_bubbles()
    glPopMatrix()

    for i in range(100):
        i = i/5
        glColor3f(0.0, 1.0, 0.0)
        glLineWidth(2.0)
        glBegin(GL_LINES)
        glVertex2f(-0.9+i, -0.85)
        glVertex2f(-0.8+i, -0.95)
        glVertex2f(-0.8+i, -0.85)
        glVertex2f(-0.8+i, -0.95)
        glVertex2f(-0.7+i, -0.85)
        glVertex2f(-0.8+i, -0.95)
        glVertex2f(-0.75+i, -0.85)
        glVertex2f(-0.8+i, -0.95)
        glVertex2f(-0.85+i, -0.85)
        glVertex2f(-0.8+i, -0.95)
        glVertex2f(-0.725+i, -0.85)
        glVertex2f(-0.8+i, -0.95)
        glVertex2f(-0.775+i, -0.85)
        glVertex2f(-0.8+i, -0.95)
        glVertex2f(-0.825+i, -0.85)
        glVertex2f(-0.8+i, -0.95)
        glVertex2f(-0.875+i, -0.85)
        glVertex2f(-0.8+i, -0.95)
        glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(-1, -0.96)
    glVertex2f(-1, -1)
    glVertex2f(1, -1)
    glVertex2f(1, -0.96)
    glEnd()

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
    glFlush()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
    glutInitWindowSize(900, 600)
    glutInitWindowPosition(50, 50)
    glutCreateWindow("Aquarium Environment")
    init()
    glutDisplayFunc(display)
    glutTimerFunc(5, move_time, 0)

    glutMainLoop()


main()
