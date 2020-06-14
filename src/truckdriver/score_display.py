import pyglet
import pymunk
from pyglet.window import key

class ScoreDisplay:
    def __init__(self, time : int):
        self.digits = pyglet.image.load("rsc/digits.png")
        self.background_img = pyglet.image.load("rsc/end_screen.png")
        self.background = pyglet.sprite.Sprite(self.background_img, subpixel = True)
        self.digit_array = [
            self.digits.get_region(0,0,10,16),
            self.digits.get_region(10,0,10,16),
            self.digits.get_region(20,0,10,16),
            self.digits.get_region(30,0,10,16),
            self.digits.get_region(40,0,10,16),
            self.digits.get_region(50,0,10,16),
            self.digits.get_region(60,0,10,16),
            self.digits.get_region(70,0,10,16),
            self.digits.get_region(80,0,10,16),
            self.digits.get_region(90,0,10,16),
            self.digits.get_region(100,0,10,16)]
        for digit in self.digit_array:
            digit.anchor_x = 5
            digit.anchor_y = 8
        seconds : int = time%60
        minutes : int = time/60
        
        self.display = [
            pyglet.sprite.Sprite(self.digit_array[int(minutes//10)],x = 80 - 11*2, y = 26,subpixel = True),
            pyglet.sprite.Sprite(self.digit_array[int(minutes%10)],x = 80 - 11*1, y = 26,subpixel = True),
            pyglet.sprite.Sprite(self.digit_array[int(10)],x = 80, y = 26,subpixel = True),
            pyglet.sprite.Sprite(self.digit_array[int(seconds//10)],x = 80 + 11*1, y = 26,subpixel = True),
            pyglet.sprite.Sprite(self.digit_array[int(seconds%10)],x = 80 + 11*2, y = 26,subpixel = True)
        ]
        self.should_restart = False
        self.keys = key.KeyStateHandler()

    def update(self, delta: float):
        if self.keys[key.ENTER]:
            self.should_restart = True
        pass

    def draw(self):
        pyglet.gl.glTexParameteri(pyglet.gl.GL_TEXTURE_2D, pyglet.gl.GL_TEXTURE_MAG_FILTER, pyglet.gl.GL_NEAREST) 
        pyglet.gl.glTexParameteri(pyglet.gl.GL_TEXTURE_2D, pyglet.gl.GL_TEXTURE_MIN_FILTER, pyglet.gl.GL_NEAREST)
        self.background.draw()
        for digit in self.display:
            pyglet.gl.glTexParameteri(pyglet.gl.GL_TEXTURE_2D, pyglet.gl.GL_TEXTURE_MAG_FILTER, pyglet.gl.GL_NEAREST) 
            pyglet.gl.glTexParameteri(pyglet.gl.GL_TEXTURE_2D, pyglet.gl.GL_TEXTURE_MIN_FILTER, pyglet.gl.GL_NEAREST)
            digit.draw()
        pass