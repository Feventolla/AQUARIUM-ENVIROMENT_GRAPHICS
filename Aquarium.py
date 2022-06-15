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

fishX = 4.0
fishY= 3.0

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

def fish3():
    glScalef(0.6, 0.6, 0.0)
    glTranslatef(0,0, 0.0) 
    
    glColor3f(0.000, 0.749, 1.000)
    glBegin(GL_POLYGON)
    glVertex3f(0.428, 0.127, 0.0)
    glVertex3f(0.517, 0.057, 0.0)
    glVertex3f(0.499, 0.108, 0.0)
    glVertex3f(0.488, 0.162, 0.0)
    glVertex3f(0.486, 0.148, 0.0)
    glVertex3f(0.497, 0.233, 0.0)
    glVertex3f(0.514, 0.282, 0.0)
    glVertex3f(0.528, 0.318, 0.0)
    glVertex3f(0.429, 0.245, 0.0)
    glEnd()
    glColor3f(0.000, 0.749, 1.000)
    glBegin(GL_POLYGON)
    glVertex3f(0.160, 0.304, 0.0)
    glVertex3f(0.177, 0.326, 0.0)
    glVertex3f(0.193, 0.334, 0.0)
    glVertex3f(0.221, 0.346, 0.0)
    glVertex3f(0.224, 0.348, 0.0)
    glVertex3f(0.244, 0.348, 0.0)
    glVertex3f(0.265, 0.345, 0.0)
    glVertex3f(0.303, 0.333, 0.0)
    glVertex3f(0.276, 0.304, 0.0)
    glEnd()
    glColor3f(0.3,0.3,1)
    glBegin(GL_POLYGON)
    glVertex3f(0.429, 0.243, 0.0)
    glVertex3f(0.306, 0.276, 0.0)
    glVertex3f(0.292, 0.301, 0.0)
    glVertex3f(0.226, 0.316, 0.0)
    glVertex3f(0.200, 0.319, 0.0)
    glVertex3f(0.164, 0.309, 0.0)
    glVertex3f(0.117, 0.288, 0.0)
    glVertex3f(0.077, 0.256, 0.0)
    glVertex3f(0.052, 0.222, 0.0)
    glVertex3f(0.038, 0.187, 0.0)
    glVertex3f(0.041, 0.144, 0.0)
    glVertex3f(0.061, 0.119, 0.0)
    glVertex3f(0.108, 0.083, 0.0)
    glVertex3f(0.168, 0.060, 0.0)
    glVertex3f(0.204, 0.053, 0.0)
    glVertex3f(0.231, 0.054, 0.0)
    glVertex3f(0.288, 0.067, 0.0)
    glVertex3f(0.340, 0.087, 0.0)
    glVertex3f(0.403, 0.115, 0.0)
    glVertex3f(0.428, 0.127, 0.0)
    glEnd()

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


def grass():
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
    fish3()
    glPopMatrix()

    glPushMatrix()
    circle_bubbles()
    glPopMatrix()

    glPushMatrix()
    grass()
    glPopMatrix()

    # glutSwapBuffers()

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
