# pip install pygame PyOpenGL
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
pygame.display.set_caption("2 Textured Objects")
def add_texture(filename):
    image = pygame.image.load(filename)
    data = pygame.image.tostring(image, 'RGBA', 1)
    texID = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texID)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image.get_width(), image.get_height(), 0, GL_RGBA, GL_UNSIGNED_BYTE, data)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    return texID
texture_cube_id = add_texture('texture1.png')
texture_diamond_id = add_texture('texture2.png')
glEnable(GL_TEXTURE_2D)
glEnable(GL_DEPTH_TEST)
gluPerspective(45, (display[0]/display[1]), 0.1, 50)
glTranslate(0, 0, -10)
rotation_angle = 0

vertices = [
    [-1, -1, -1],
    [ 1, -1, -1],
    [ 1,  1, -1],
    [-1,  1, -1],
]

tex_coords = [
    [0, 0],
    [1, 0],
    [1, 1],
    [0, 1]
]

vertices1 = [
    [0, 1, 0],
    [1, 0, 0],
    [0, -1, 0],
    [-1, 0, 0],
    [0, 0, 1],
    [0, 0, -1]
]

squares =  [
    [0, 1, 4],
    [0, 4, 3],
    [0, 3, 5],
    [0, 5, 1],
    [2, 1, 4],
    [2, 4, 3],
    [2, 3, 5],
    [2, 5, 1]
]

tex_coords1 = [
    [0.5, 1],
    [1, 0.5],
    [0.5, 0],
    [0, 0.5],
    [0.5, 0.5],
    [0.5, 0.5],
]


def draw_diamond():
    glBegin(GL_TRIANGLES)
    for triangle in squares:
        for vertex in triangle:
            glTexCoord2fv(tex_coords1[vertex])
            glVertex3fv(vertices1[vertex])
    glEnd()


def draw_square():
    glBegin(GL_TRIANGLES)
    for triangle in [[0, 1, 2], [2, 3, 0]]:
        for vertex in triangle:
            glTexCoord2fv(tex_coords[vertex])
            glVertex3fv(vertices[vertex])
    glEnd()


def draw_cube():
    glPushMatrix()
    draw_square()
    glPopMatrix()
    glPushMatrix()
    glRotatef(90, 0, 1, 0)
    draw_square()
    glPopMatrix()
    glPushMatrix()
    glRotatef(-90, 1, 0, 0)
    draw_square()
    glPopMatrix()
    glPushMatrix()
    glRotatef(180, 0, 1, 0)
    draw_square()
    glPopMatrix()
    glPushMatrix()
    glRotatef(-90, 0, 1, 0)
    draw_square()
    glPopMatrix()
    glPushMatrix()
    glRotatef(90, 1, 0, 0)
    draw_square()
    glPopMatrix()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    rotation_angle += 1
    glPushMatrix()
    glTranslate(-2.5, 0, 0)
    glRotatef(rotation_angle, 1, 1, 1)
    glBindTexture(GL_TEXTURE_2D, texture_cube_id)
    draw_cube()
    glPopMatrix()
    glPushMatrix()
    glTranslate(2.5, 0, 0)
    glRotatef(rotation_angle, 0, 1, 0)
    glBindTexture(GL_TEXTURE_2D, texture_diamond_id)
    draw_diamond()
    glPopMatrix()
    pygame.display.flip()
    pygame.time.wait(15)