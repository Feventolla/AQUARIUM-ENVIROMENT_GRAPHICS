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
fish3pathy = 0.8
fish2pathy = -0.2

fishX = 4.0
fishY = 3.0

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



value = [-3.6,  -3.2, -2.8, -2.4, -2.0,
          -1.6,  -1.2,  -0.8, -0.4, 0.0,
         0.4, 3.2, 3.6, 2.8,  2.4,
         2.0,  1.6,  1.2,  0.8
         ]
# value1 = [-3.2,  -2.8, -2.4, -
#           -2.0, -1.6,  -1.2,  -0.8,  2.8,  2.4,
#           2.0,  1.6,  1.2,  0.8, ]



def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)


def move_time(key):
    global bubblepathx, largebubblepathx, bubblepathy, largebubblepathy, fish1path, fish3pathy, fish2pathy
    if(bubblepathx > 2.0):
        bubblepathx = -0.6
    bubblepathx += 0.03

    if(largebubblepathx > 2.0):
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

    if(fish3pathy < -2):
        fish3pathy = 0.8
    fish3pathy -= 0.008

    if(fish2pathy > 2):
        fish2pathy = -0.2
    fish2pathy += 0.004

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
    glColor3f(0.0, 0.05, 0.1)
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
    glTranslated(-fish1path, fish2pathy, 0.0)
    glColor3f(0.7, 0.25, 0.20)
    glBegin(GL_POLYGON)
    glVertex2f(-0.2, -0.6)
    glVertex2f(0.2, -0.5)
    glVertex2f(0.2, -0.7)
    glColor4f(0.1, 0.25, 0.20, 0.5)
    glVertex2f(0.5, -0.6)
    glVertex2f(0.2, -0.5)

    glEnd()
    glBegin(GL_TRIANGLES)
    glColor3f(0.7, 0.25, 0.20)
    glVertex2f(0.2, -0.5)
    glVertex2f(0.17, -0.55)
    glColor4f(0.1, 0.25, 0.20, 0.5)
    glVertex2f(0.1, -0.45)
    glVertex2f(0.2, -0.7)
    glColor3f(0.7, 0.25, 0.20)
    glVertex2f(0.17, -0.65)
    glVertex2f(0.1, -0.75)

    glVertex2f(-0.18, -0.6)
    glVertex2f(-0.27, -0.6)
    glColor4f(0.1, 0.25, 0.20, 0.5)
    glVertex2f(-0.3, -0.67)
    glColor3f(0.7, 0.25, 0.20)
    glVertex2f(-0.18, -0.6)
    glVertex2f(-0.27, -0.6)
    glColor4f(0.1, 0.25, 0.20, 0.5)
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
   


    glBegin(GL_POINTS)
    glVertex2f(0.4, -0.6)
    glEnd()


    glPopMatrix()
    glFlush()


def fish3():
    glScalef(0.6, 0.6, 0.0)
    glTranslated(fish1path+0.01, fish3pathy, 0.0)
    glColor4f(0.7, 0.4, 0.0, 0.0)
    glBegin(GL_TRIANGLES)

    glVertex2f(0.428, 0.227)
    glVertex2f(0.51, 0.1)
    glVertex2f(0.428, 0.335)

    glVertex2f(0.429, 0.343)
    glVertex2f(0.51, 0.512)
    glVertex2f(0.429, 0.20)

    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(0.429, 0.343, 0.0)
    glVertex3f(0.306, 0.376, 0.0)
    glVertex3f(0.292, 0.401, 0.0)
    glColor4f(1.0, 0.5, 0.0, 0.0)
    glVertex3f(0.226, 0.416, 0.0)
    glVertex3f(0.200, 0.419, 0.0)
    glColor4f(1, 1, 1, 0)
    glVertex3f(0.164, 0.409, 0.0)
    glVertex3f(0.117, 0.388, 0.0)
    glColor4f(1.0, 0.5, 0.0, 0.0)
    glVertex3f(0.077, 0.356, 0.0)
    glVertex3f(0.052, 0.322, 0.0)
    glColor4f(1, 1, 1, 0)
    glVertex3f(0.038, 0.287, 0.0)
    glVertex3f(0.041, 0.244, 0.0)
    glColor4f(1.0, 0.5, 0.0, 0.0)
    glVertex3f(0.061, 0.219, 0.0)
    glVertex3f(0.108, 0.183, 0.0)
    glColor4f(1, 1, 1, 0)
    glVertex3f(0.168, 0.160, 0.0)
    glVertex3f(0.204, 0.153, 0.0)
    glColor4f(1.0, 0.5, 0.0, 0.0)
    glVertex3f(0.231, 0.154, 0.0)
    glVertex3f(0.288, 0.167, 0.0)
    glColor4f(1, 1, 1, 0)
    glVertex3f(0.340, 0.187, 0.0)
    glVertex3f(0.403, 0.215, 0.0)
    glColor4f(1.0, 0.5, 0.0, 0.0)
    glVertex3f(0.428, 0.227, 0.0)
    glEnd()

    glPointSize(3)
    glBegin(GL_POINTS)

    glColor3f(0.1, 0.1, 0.3)

    glVertex2f(0.09, 0.3)
    glEnd()
    glColor4f(0.7, 0.4, 0.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(0.12, 0.340)
    glVertex2f(0.20, 0.340)
    glVertex2f(0.22, 0.27)
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
    for k in value:
        glPushMatrix()
        glScalef(0.3, 0.3, 0.0)
        glTranslated(k, -3.2, 0.0)
        posx, posy = 0, 0
        sides = 32
        radius = 0.06
        glBegin(GL_POLYGON)
        glColor3f(1.0, 0.36, 0.25)
        for i in range(100):
            cosine = radius * cos(i*2*pi/sides)
            sine = radius * sin(i*2*pi/sides)

            glVertex2f(sine, cosine)
        glEnd()
        glPopMatrix()


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

    # for k in value:
    #     glPushMatrix()
    #     glScalef(0.3, 0.3, 0.0)
    #     glTranslated(k, -4.5, 0.0)
    #     posx, posy = 0, 0
    #     sides = 32
    #     radius = 1.5
    #     glBegin(GL_POLYGON)

    #     glColor3f(0.0, 0.54, 0.0)
        # for i in range(30):
        #     cosine = radius * cos(i/sides)
        #     sine = radius * sin(i/sides)

        #     glVertex2f(sine, cosine)
        # glEnd()
        # glPopMatrix()
    
    # for k in value:
    #     glPushMatrix()
    #     glScalef(0.3, 0.3, 0.0)
    #     glTranslated(k+0.05, -4.7, 0.0)
    #     posx, posy = 0, 0
    #     sides = 32
    #     radius = 1.5
    #     glBegin(GL_POLYGON)
    #     glColor3f(0.0, 0.54, 0.0)
    #     for i in range(30):
    #         cosine = radius * cos(i/sides)
    #         sine = radius * sin(i/sides)

    #         glVertex2f(-sine, cosine)
    #     glEnd()
    #     glPopMatrix()
    # for k in value:
    #     glPushMatrix()
    #     glScalef(0.3, 0.3, 0.0)
    #     glTranslated(k, -3.25, 0.0)
    #     posx, posy = 0, 0
    #     sides = 32
    #     radius = 0.05
    #     glBegin(GL_POLYGON)
    #     glColor3f(0.95, 0.36, 0.25)
    #     for i in range(100):
    #         cosine = radius * cos(i*2*pi/sides)
    #         sine = radius * sin(i*2*pi/sides)

    #         glVertex2f(sine, cosine)
    #     glEnd()
    #     glPopMatrix()

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


    for i in range(36):
        glPushMatrix()
        if (i%3 == 0):
            i = i/6
            glTranslated(i,i*10,0)
        elif (i%2 == 0):
            i = i/15
            glTranslated(i*10,i/10,0)
        else:
            i = i/10
            glTranslated(i,i/10,0)
        
        glBegin(GL_LINES)    
        glColor3f(0.5,0.35,0.05)
        glVertex2f(-0.9,-0.85)
        glVertex2f(-0.89,-0.83)
        glEnd()
        glPopMatrix()

    for i in range(36):
        glPushMatrix()
        if (i%3 == 0):
            i = i/6
            glTranslated(-i,-i*10,0)
        elif (i%2 == 0):
            i = i/15
            glTranslated(-i*10,-i/10,0)
        else:
            i = i/10
            glTranslated(-i,-i/10,0)
        
        glBegin(GL_LINES)    
        glColor3f(0.5,0.35,0.05)
        glVertex2f(0.98,-0.85)
        glVertex2f(0.99,-0.83)
        glEnd()
        glPopMatrix()



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
    glTranslated(-0.85, -0.5, 0.0)
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
    glTranslated(-0.85, -0.5, 0.0)
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINE_STRIP)
    glVertex2f(1.05, -0.17)
    glVertex2f(1.0, -0.19)
    glVertex2f(0.92, -0.19)
    glVertex2f(0.87, -0.17)

    glEnd()

    glPopMatrix()

    
    glPushMatrix()
    glTranslated(-0.2,-0.35,0)
    glColor3f(0.0,0.5,0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.6,-0.6)
    glVertex2f(-0.56,-0.46)
    glColor3f(0.5,0.5,0.0)
    glVertex2f(-0.62,-0.6)
    glColor3f(0.0,0.5,0.0)
    glVertex2f(-0.62,-0.6)
    glVertex2f(-0.612,-0.58)
    glVertex2f(-0.63,-0.5)
    glEnd()
    glPopMatrix() 

    glPushMatrix()
    glTranslated(-0.37,-0.33,0)
    glColor3f(0.0,0.5,0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.6,-0.6)
    glVertex2f(-0.56,-0.46)
    glColor3f(0.5,0.5,0.0)
    glVertex2f(-0.62,-0.6)
    glColor3f(0.0,0.5,0.0)
    glVertex2f(-0.62,-0.6)
    glVertex2f(-0.612,-0.58)
    glVertex2f(-0.63,-0.5)
    glEnd()
    glPopMatrix() 


    glPushMatrix()
    glTranslated(-0.1,-0.4,0)
    glColor3f(0.0,0.5,0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.6,-0.6)
    glVertex2f(-0.56,-0.46)
    glColor3f(0.5,0.5,0.0)
    glVertex2f(-0.62,-0.6)
    glColor3f(0.0,0.5,0.0)
    glVertex2f(-0.62,-0.6)
    glVertex2f(-0.612,-0.58)
    glVertex2f(-0.63,-0.5)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslated(0.09,-0.4,0)
    glColor3f(0.0,0.5,0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.6,-0.6)
    glVertex2f(-0.56,-0.46)
    glColor3f(0.5,0.5,0.0)
    glVertex2f(-0.62,-0.6)
    glColor3f(0.0,0.5,0.0)
    glVertex2f(-0.62,-0.6)
    glVertex2f(-0.612,-0.58)
    glVertex2f(-0.63,-0.5)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslated(0.1,-0.3,0)
    glColor3f(0.0,0.5,0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.6,-0.6)
    glVertex2f(-0.56,-0.46)
    glColor3f(0.5,0.5,0.0)
    glVertex2f(-0.62,-0.6)
    glColor3f(0.0,0.5,0.0)
    glVertex2f(-0.62,-0.6)
    glVertex2f(-0.612,-0.58)
    glVertex2f(-0.63,-0.5)
    glEnd()
    glPopMatrix() 

    glPushMatrix()
    glTranslated(0.2,-0.35,0)
    glColor3f(0.0,0.5,0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.6,-0.6)
    glVertex2f(-0.56,-0.46)
    glColor3f(0.5,0.5,0.0)
    glVertex2f(-0.62,-0.6)
    glColor3f(0.0,0.5,0.0)
    glVertex2f(-0.62,-0.6)
    glVertex2f(-0.612,-0.58)
    glVertex2f(-0.63,-0.5)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslated(0.3,-0.35,0)
    glColor3f(0.0,0.5,0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.6,-0.6)
    glVertex2f(-0.56,-0.46)
    glColor3f(0.5,0.5,0.0)
    glVertex2f(-0.62,-0.6)
    glColor3f(0.0,0.5,0.0)
    glVertex2f(-0.62,-0.6)
    glVertex2f(-0.612,-0.58)
    glVertex2f(-0.63,-0.5)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslated(0.42,-0.4,0)
    glColor3f(0.0,0.5,0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.6,-0.6)
    glVertex2f(-0.56,-0.46)
    glColor3f(0.5,0.5,0.0)
    glVertex2f(-0.62,-0.6)
    glColor3f(0.0,0.5,0.0)
    glVertex2f(-0.62,-0.6)
    glVertex2f(-0.612,-0.58)
    glVertex2f(-0.63,-0.5)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslated(0.5,-0.3,0)
    glColor3f(0.0,0.5,0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.6,-0.6)
    glVertex2f(-0.56,-0.46)
    glColor3f(0.5,0.5,0.0)
    glVertex2f(-0.62,-0.6)
    glColor3f(0.0,0.5,0.0)
    glVertex2f(-0.62,-0.6)
    glVertex2f(-0.612,-0.58)
    glVertex2f(-0.63,-0.5)
    glEnd()
    glPopMatrix() 
    

    glPushMatrix()
    glTranslated(0.9,-0.3,0)
    glColor3f(0.0,0.5,0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.6,-0.6)
    glVertex2f(-0.56,-0.46)
    glColor3f(0.5,0.5,0.0)
    glVertex2f(-0.62,-0.6)
    glColor3f(0.0,0.5,0.0)
    glVertex2f(-0.62,-0.6)
    glVertex2f(-0.612,-0.58)
    glVertex2f(-0.63,-0.5)
    glEnd()
    glPopMatrix() 

    glPushMatrix()
    glTranslated(1.0,-0.35,0)
    glColor3f(0.0,0.5,0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.6,-0.6)
    glVertex2f(-0.56,-0.46)
    glColor3f(0.5,0.5,0.0)
    glVertex2f(-0.62,-0.6)
    glColor3f(0.0,0.5,0.0)
    glVertex2f(-0.62,-0.6)
    glVertex2f(-0.612,-0.58)
    glVertex2f(-0.63,-0.5)
    glEnd()
    glPopMatrix() 

    glPushMatrix()
    glTranslated(1.1,-0.43,0)
    glColor3f(0.0,0.5,0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.6,-0.6)
    glVertex2f(-0.56,-0.46)
    glColor3f(0.5,0.5,0.0)
    glVertex2f(-0.62,-0.6)
    glColor3f(0.0,0.5,0.0)
    glVertex2f(-0.62,-0.6)
    glVertex2f(-0.612,-0.58)
    glVertex2f(-0.63,-0.5)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslated(1.2,-0.3,0)
    glColor3f(0.0,0.5,0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.6,-0.6)
    glVertex2f(-0.56,-0.46)
    glColor3f(0.5,0.5,0.0)
    glVertex2f(-0.62,-0.6)
    glColor3f(0.0,0.5,0.0)
    glVertex2f(-0.62,-0.6)
    glVertex2f(-0.612,-0.58)
    glVertex2f(-0.63,-0.5)
    glEnd()
    glPopMatrix() 

    glPushMatrix()
    glTranslated(1.32,-0.36,0)
    glColor3f(0.0,0.5,0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.6,-0.6)
    glVertex2f(-0.56,-0.46)
    glColor3f(0.5,0.5,0.0)
    glVertex2f(-0.62,-0.6)
    glColor3f(0.0,0.5,0.0)
    glVertex2f(-0.62,-0.6)
    glVertex2f(-0.612,-0.58)
    glVertex2f(-0.63,-0.5)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslated(1.5,-0.36,0)
    glColor3f(0.0,0.5,0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.6,-0.6)
    glVertex2f(-0.56,-0.46)
    glColor3f(0.5,0.5,0.0)
    glVertex2f(-0.62,-0.6)
    glColor3f(0.0,0.5,0.0)
    glVertex2f(-0.62,-0.6)
    glVertex2f(-0.612,-0.58)
    glVertex2f(-0.63,-0.5)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslated(1.6,-0.1,0)
    glColor3f(0.0,0.5,0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.6,-0.6)
    glVertex2f(-0.56,-0.46)
    glColor3f(0.5,0.5,0.0)
    glVertex2f(-0.62,-0.6)
    glColor3f(0.0,0.5,0.0)
    glVertex2f(-0.62,-0.6)
    glVertex2f(-0.612,-0.58)
    glVertex2f(-0.63,-0.5)
    glEnd()
    glPopMatrix() 

    glPushMatrix()
    glTranslated(1.45,-0.2,0)
    glColor3f(0.0,0.5,0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.6,-0.6)
    glVertex2f(-0.56,-0.46)
    glColor3f(0.5,0.5,0.0)
    glVertex2f(-0.62,-0.6)
    glColor3f(0.0,0.5,0.0)
    glVertex2f(-0.62,-0.6)
    glVertex2f(-0.612,-0.58)
    glVertex2f(-0.63,-0.5)
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
    fish3()
    glPopMatrix()

    glPushMatrix()
    circle_bubbles()
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
