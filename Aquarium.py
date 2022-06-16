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
bubblepathx = -0.5
bubblepathy = -0.5
largebubblepathx = -0.5
largebubblepathy = -0.5
fish1path = 0.8


fishX = 4.0
fishY= 3.0

points = [-0.1, -0.19, -0.28, -0.37, -0.46, -
          0.55, -0.64, -0.73, -0.82, -0.91, -1.0]

onlyPoints = [-0.1, -0.24, -0.41, -0.56]

#   -0.55, -0.64, -0.73, -0.82, -0.91, -1.0]

points = [-0.1, -0.22, -0.34, -0.45, -0.56, -
          0.65, -0.74, -0.83, -0.92, -1.0]

value = [-3.6, -3.6,  -2.4, -1.2
         #  -1.8, -1.2, -0.8, 0.0, 0.4,
         #          0.8,  1.2,  1.6, 2.0, 2.4, 2.8, 3.2, 3.6
         ]
value1 = [-3.6,   -2.4, -1.2, 0.3
          # -0.6, -0.2, 0.4,
          #           0.8,  1.2,  1.6, 2.0, 2.4, 2.8, 3.2, 3.6
          ]


value = [-3.6, -3.4, -3.2, - 3.0, -2.8, -2.6, -2.4, -
         2.2, -2.0, -1.8, -1.6, -1.4, -1.2, -1.0, -0.8, -0.6, 2.8, 2.6, 2.4,
         2.2, 2.0, 1.8, 1.6, 1.4, 1.2, 1.0, 0.8, 0.6]



def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)


def move_time(key):
    global bubblepathx, largebubblepathx, bubblepathy, largebubblepathy, fish1path
    if(bubblepathx > 2.0):
        bubblepathx = -0.6
    bubblepathx += 0.03

    if(largebubblepathx > 2):
        largebubblepathx = -.5
    largebubblepathx += 0.03

    if(bubblepathy > 2):
        bubblepathy = -.5
    bubblepathy += 0.02

    if(largebubblepathy > 2):
        largebubblepathy = -.5
    largebubblepathy += 0.02

    if(fish1path < -2):
        fish1path = 0.8
    fish1path -= 0.008

    glutPostRedisplay()
    glutTimerFunc(10, move_time, 0)


def circle_bubbles():
    glLoadIdentity()

    for l in points:
        glPushMatrix()
        glScalef(1.0, 1.0, 0.0)
        glTranslated(0.9, l, 0.0)
        posx, posy = 0, 0
        sides = 32
        radius = 0.02
        glTranslated(0.0, bubblepathx, 0.0)
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
        radius = 0.02
        glTranslated(0.0, bubblepathy, 0.0)
        glBegin(GL_LINE_LOOP)
        glColor3f(1.0, 1.0, 1.0)
        for i in range(100):
            cosine = radius * cos(i*2*pi/sides)
            sine = radius * sin(i*2*pi/sides)
            glVertex2f(cosine, sine)
        glEnd()
        glPopMatrix()

    for d in onlyPoints:
        glPushMatrix()
        glScalef(1.0, 1.0, 0.0)
        glTranslated(-0.9, d, 0.0)
        posx, posy = 0, 0
        sides = 32
        radius = 0.04
        glTranslated(0.0, largebubblepathx, 0.0)
        glBegin(GL_LINE_LOOP)
        glColor3f(1.0, 1.0, 1.0)
        for i in range(100):
            cosine = radius * cos(i*2*pi/sides)
            sine = radius * sin(i*2*pi/sides)
            glVertex2f(cosine, sine)
        glEnd()
        glPopMatrix()
    for j in onlyPoints:
        glPushMatrix()
        glScalef(1.0, 1.0, 0.0)
        glTranslated(0.9, j, 0.0)
        posx, posy = 0, 0
        sides = 32
        radius = 0.04
        glTranslated(0.0, largebubblepathy, 0.0)
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
    glTranslated(fish1path, 0.0, 0.0)
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
    glColor3f(0.7, 0.25, 0.20) 
    glBegin(GL_POLYGON)
    glVertex2f(-0.2, -0.6)
    glVertex2f(0.2, -0.5)
    glVertex2f(0.2, -0.7)
    glColor4f(0.1, 0.25, 0.20,0.5)
    glVertex2f(0.5, -0.6)
    glVertex2f(0.2, -0.5)

    glEnd()
    glBegin(GL_TRIANGLES)
    glColor3f(0.7, 0.25, 0.20) 
    glVertex2f(0.2, -0.5)
    glVertex2f(0.17, -0.55)
    glColor4f(0.1, 0.25, 0.20,0.5)
    glVertex2f(0.1, -0.45)
    glVertex2f(0.2, -0.7)
    glColor3f(0.7, 0.25, 0.20) 
    glVertex2f(0.17, -0.65)
    glVertex2f(0.1, -0.75)


    glVertex2f(-0.18, -0.6)
    glVertex2f(-0.27, -0.6)
    glColor4f(0.1, 0.25, 0.20,0.5)
    glVertex2f(-0.3, -0.67)
    glColor3f(0.7, 0.25, 0.20)
    glVertex2f(-0.18, -0.6)
    glVertex2f(-0.27, -0.6)
    glColor4f(0.1, 0.25, 0.20,0.5)
    glVertex2f(-0.3, -0.53)
    glEnd()

    glColor3f(1, 1, 1)
    glPointSize(3)
    glBegin(GL_POINTS)
    glVertex2f(0.4, -0.6)
    glEnd()

    # glColor3f(0.7, 0.25, 0.20)
    # glBegin(GL_LINES)
    # glVertex2f(0.495, -0.6)
    # glVertex2f(0.46, -0.6)
    # glEnd()
   

    glPopMatrix()
    glFlush()

def fish3():
    glScalef(0.6, 0.6, 0.0)
    # glTranslatef(0,0, 0.0) 
    
    glColor4f(0.7, 0.4, 0.0,0.0)
    glBegin(GL_TRIANGLES)
    
    glVertex2f(0.428, 0.227)
    glVertex2f(0.51, 0.1) 
    glVertex2f(0.428,0.335)

    
    glVertex2f(0.429, 0.343)
    glVertex2f(0.51, 0.512)
    glVertex2f(0.429, 0.20)
   
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(0.429, 0.343, 0.0)
    glVertex3f(0.306, 0.376, 0.0)
    glVertex3f(0.292, 0.401, 0.0)
    glColor4f(1.0, 0.5, 0.0,0.0)
    glVertex3f(0.226, 0.416, 0.0)
    glVertex3f(0.200, 0.419, 0.0)
    glColor4f(1,1,1,0)
    glVertex3f(0.164, 0.409, 0.0)
    glVertex3f(0.117, 0.388, 0.0)
    glColor4f(1.0, 0.5, 0.0,0.0)
    glVertex3f(0.077, 0.356, 0.0)
    glVertex3f(0.052, 0.322, 0.0)
    glColor4f(1,1,1,0)
    glVertex3f(0.038, 0.287, 0.0)
    glVertex3f(0.041, 0.244, 0.0)
    glColor4f(1.0, 0.5, 0.0,0.0)
    glVertex3f(0.061, 0.219, 0.0)
    glVertex3f(0.108, 0.183, 0.0)
    glColor4f(1,1,1,0)
    glVertex3f(0.168, 0.160, 0.0)
    glVertex3f(0.204, 0.153, 0.0)
    glColor4f(1.0, 0.5, 0.0,0.0)
    glVertex3f(0.231, 0.154, 0.0)
    glVertex3f(0.288, 0.167, 0.0)
    glColor4f(1,1,1,0)
    glVertex3f(0.340, 0.187, 0.0)
    glVertex3f(0.403, 0.215, 0.0)
    glColor4f(1.0, 0.5, 0.0,0.0)
    glVertex3f(0.428, 0.227, 0.0)
    glEnd()

    glPointSize(3)
    glBegin(GL_POINTS)
  
    glColor3f(0.1,0.1,0.3)
    
    glVertex2f(0.09,0.3)
    glEnd()
    glColor4f(0.7, 0.4, 0.0,0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(0.12,0.340)
    glVertex2f(0.20,0.340)
    glVertex2f(0.22,0.27)
    glEnd()
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_LINES)
    glVertex2f(0.041, 0.253)
    glVertex2f(0.075, 0.253)
    glEnd()

def sand_env() :
    glScalef(0.6, 0.6, 0.0)
    # glTranslatef(0,0, 0.0) 
    
    glColor4f(0.7, 0.4, 0.0,0.0)
    glColor3f(1,1,0)
    glBegin(GL_POLYGON)
    glVertex2f(-0.1,-1)
    glVertex2f(-1,-0.6)
    glVertex2f(1,-0.6)
    glVertex2f(1,1)
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

    # for k in value:
    #     glPushMatrix()
    #     glScalef(0.3, 0.3, 0.0)
    #     glTranslated(k, -4.5, 0.0)
    #     posx, posy = 0, 0
    #     sides = 65
    #     radius = 1.5
    #     glBegin(GL_POLYGON)

    #     glColor3f(0.0, 1.0, 0.0)
    #     for i in range(30):
    #         cosine = radius * cos(i/sides)
    #         sine = radius * sin(i/sides)

    #         glVertex2f(sine, cosine)
    #     glEnd()
    #     glPopMatrix()
    # for k in value:
        # glPushMatrix()
        # glScalef(0.3, 0.3, 0.0)
        # glTranslated(k, -4.5, 0.0)
        # posx, posy = 0, 0
        # sides = 1000
        # radius = 4
        # glBegin(GL_POLYGON)
        # glColor3f(0.0, 1.0, 0.0)
        # for i in range(30):
        #     cosine = radius * cos(i/sides)
        #     sine = radius * sin(i/sides)

        #     glVertex2f(-sine, cosine)
        # glEnd()
        # glPopMatrix()
    # glPushMatrix()

        # glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        # glPushMatrix()
        # glScalef(0.3, 0.3, 0.0)
        # glTranslated(k, -3.8, 0.0)
        # glBegin(GL_POLYGON)
        # glColor3f(0.0, 1.0, 0.0)
        # glVertex3f(0.4, -0.4, 0.0)

        # glVertex3f(0.35, 0.75, 0.0)
        # glVertex3f(0.2, 0.35, 0.0)
        # glEnd()

        # glBegin(GL_LINES)
        # glColor3f(1.0, 1.0, 1.0)
        # glVertex3f(0.35, 0.75, 0.0)
        # glVertex3f(0.4, -0.4, 0.0)
        # glEnd()
        # glBegin(GL_POLYGON)
        # glColor3f(0.0, 1.0, 0.0)
        # glVertex3f(0.4, -0.4, 0.0)
        # glVertex3f(0.5, 0.35, 0.0)
        # glVertex3f(0.35, 0.75, 0.0)
        # glEnd()
        # glPopMatrix()
    # glPopMatrix()

    # big rock
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

    # small rock
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
    glColor3f(1,1,1)
    glBegin(GL_POLYGON)
    glVertex3f(-0.984620, -0.030759, 0.000157)
    glVertex3f(-0.881724, -0.136549, 0.000697)
    glVertex3f(-0.816608, -0.207216, 0.001057)
    glVertex3f(-0.779634, -0.247701, 0.001264)
    glVertex3f(-0.761162, -0.262946, 0.001342)
    glVertex3f(-0.751551, -0.257892, 0.001316)
    glVertex3f(-0.741164, -0.237480, 0.001212)
    glVertex3f(-0.720360, -0.206652, 0.001054)
    glVertex3f(-0.679500, -0.170349, 0.000869)
    glVertex3f(-0.608944, -0.133511, 0.000681)
    glVertex3f(-0.499053, -0.101081, 0.000516)
    glVertex3f(-0.340188, -0.077999, 0.000398)
    glVertex3f(-0.122708, -0.069207, 0.000353)
    glVertex3f(0.085513 ,-0.072687 ,0.000371)
    glVertex3f(0.220006 ,-0.082308 ,0.000420)
    glVertex3f(0.295516 ,-0.096842 ,0.000494)
    glVertex3f(0.326790 ,-0.115060 ,0.000587)
    glVertex3f(0.328573 ,-0.135735 ,0.000693)
    glVertex3f(0.315610 ,-0.157639 ,0.000804)
    glVertex3f(0.302647 ,-0.179542 ,0.000916)
    glVertex3f(0.304429 ,-0.200217 ,0.001022)
    glVertex3f(0.335703 ,-0.218435 ,0.001114)
    glVertex3f(0.411214 ,-0.232969 ,0.001189)
    glVertex3f(0.545706 ,-0.242590 ,0.001238)
    glVertex3f(0.753927 ,-0.246070 ,0.001255)
    glVertex3f(0.954431 ,-0.240926 ,0.001229)
    glVertex3f(1.067590 ,-0.226703 ,0.001157)
    glVertex3f(1.110873 ,-0.205218 ,0.001047)
    glVertex3f(1.101749 ,-0.178287 ,0.000910)
    glVertex3f(1.057686 ,-0.147724 ,0.000754)
    glVertex3f(0.996155 ,-0.115345 ,0.000589)
    glVertex3f(0.934623 ,-0.082967 ,0.000423)
    glVertex3f(0.890561 ,-0.052404 ,0.000267)
    glVertex3f(0.881437 ,-0.025472 ,0.000130)
    glVertex3f(0.924720 ,-0.003987 ,0.000020)
    glVertex3f(1.037879 ,0.010235 ,-0.000052)
    glVertex3f(1.238383 ,0.015379 ,-0.000078)
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
    glutTimerFunc(35, move_time, 0)

    glutMainLoop()


main()
