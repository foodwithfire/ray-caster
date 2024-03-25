import pygame, keyboard, math
from settings import *


class Player:
    def __init__(self, pos):
        self.pos = pygame.math.Vector2(pos)
        self.vel = pygame.math.Vector2(0, 0)
        self.dir = None
        self.speed = 0.02
        self.friction = 0.95
        self.size = 40

        self.wall_size = screensize[0] / 50
        self.angle = None
        self.fov = 5
        self.distances = []

    def render(self):
        self.distances = []
        for i in range(self.fov):
            distance = 0
            ray = pygame.math.Vector2(self.pos.x, self.pos.y)
            while True:
                ray += pygame.math.Vector2(math.cos(self.angle), math.sin(self.angle))
                if (ray.x < 0 or ray.y < 0) or (ray.x > screensize[0] or ray.y > screensize[1]):
                    break
                distance += 1
            pygame.draw.line(pygame.display.get_surface(), (0, 255, 0), self.pos, ray, 2)
            self.angle += math.radians(2)
            self.distances.append(distance)
        pygame.draw.circle(pygame.display.get_surface(), "black", self.pos, self.size/2)

    def collision(self):
        if self.pos.x < self.size/2:
            self.pos.x = self.size/2
        if self.pos.x > screensize[0] - self.size/2:
            self.pos.x = screensize[0] - self.size/2
        if self.pos.y < self.size/2:
            self.pos.y = self.size/2
        if self.pos.y > screensize[1] - self.size/2:
            self.pos.y = screensize[1] - self.size/2

    def update(self, dt):
        self.dir = pygame.math.Vector2(keyboard.is_pressed("d") - keyboard.is_pressed("q"),
                                       keyboard.is_pressed("s") - keyboard.is_pressed("z"))
        self.vel += self.dir * self.speed
        self.pos += self.vel * dt
        self.vel *= self.friction
        diff = pygame.math.Vector2(self.pos - pygame.mouse.get_pos())
        self.angle = math.radians(math.degrees(math.atan2(diff.y, diff.x)) + 180)
        print(self.distances)

        self.collision()
        self.render()
