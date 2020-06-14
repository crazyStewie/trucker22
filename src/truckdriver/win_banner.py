import pymunk
import pyglet

class WinBanner:
    def __init__(self):
        self.image = pyglet.image.load("rsc/win_banner.png")
        self.sprite = pyglet.sprite.Sprite(self.image, subpixel = True)
        self.position = pymunk.Vec2d(-160,116)
        self.win_timer = 0
        self.win_time = 1
        self.banner_time = 0.5
        self.won = False

    def update(self, delta : float, is_winning : bool):
        if is_winning and not self.won:
            self.win_timer += delta
            if self.win_timer > self.win_time:
                self.win_timer = 0
                self.won = True
            self.position.x = -160*(1 - self.win_timer/self.win_time)
            self.position.y = 116
        if not is_winning and not self.won:
            self.position.x = -160
            self.win_timer = 0
        if self.won:
            self.position.x = 0
            if self.win_timer > self.banner_time:
                self.win_timer = self.banner_time
            self.position.y = 116*(1-self.win_timer/self.banner_time)
            self.win_timer += delta

    def draw(self):
        self.sprite.position = self.position
        pyglet.gl.glTexParameteri(pyglet.gl.GL_TEXTURE_2D, pyglet.gl.GL_TEXTURE_MAG_FILTER, pyglet.gl.GL_NEAREST) 
        pyglet.gl.glTexParameteri(pyglet.gl.GL_TEXTURE_2D, pyglet.gl.GL_TEXTURE_MIN_FILTER, pyglet.gl.GL_NEAREST)
        self.sprite.draw()