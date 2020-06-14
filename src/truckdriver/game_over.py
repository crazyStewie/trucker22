import pymunk
import pyglet

class GameOver:
    def __init__(self):
        self.image = pyglet.image.load("rsc/game_over.png")
        self.sprite = pyglet.sprite.Sprite(self.image, subpixel = True)
        self.position = pymunk.Vec2d(-160,-116)
        self.lost = False
        self.lost_timer = 0
        self.banner_time = 0.5

    def update(self, delta : float, progress : float):
        if not self.lost:
            self.position.x = -160*(1-progress)
            if progress >= 1:
                self.lost = True
        if self.lost:
            self.position.x = 0
            if self.lost_timer > self.banner_time:
                self.lost_timer = self.banner_time
            self.position.y = -116*(1-self.lost_timer/self.banner_time)
            self.lost_timer += delta

    def draw(self):
        self.sprite.position = self.position
        pyglet.gl.glTexParameteri(pyglet.gl.GL_TEXTURE_2D, pyglet.gl.GL_TEXTURE_MAG_FILTER, pyglet.gl.GL_NEAREST) 
        pyglet.gl.glTexParameteri(pyglet.gl.GL_TEXTURE_2D, pyglet.gl.GL_TEXTURE_MIN_FILTER, pyglet.gl.GL_NEAREST)
        self.sprite.draw()