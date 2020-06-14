import pyglet
import pymunk
class Marker:
    def __init__(self, position : (float, float)):
        self.image = pyglet.image.load("rsc/marker.png")
        self.sprite = pyglet.sprite.Sprite(self.image, subpixel = True)
        self.position = pymunk.Vec2d(position)

    def update(self, delta : float):
        pass
    
    def check_win(self, container : pymunk.Body) -> bool:
        points = [container.local_to_world((-3,-12)), container.local_to_world((3,-12)), container.local_to_world((3,12)), container.local_to_world((-3,12))]
        won = True
        for point in points:
            if point.x > self.position.x + 10 or point.x < self.position.x or point.y > self.position.y + 26 or point.y < self.position.y:
                won = False
        return won;

    def draw(self):
        self.sprite.position = self.position
        pyglet.gl.glTexParameteri(pyglet.gl.GL_TEXTURE_2D, pyglet.gl.GL_TEXTURE_MAG_FILTER, pyglet.gl.GL_NEAREST) 
        pyglet.gl.glTexParameteri(pyglet.gl.GL_TEXTURE_2D, pyglet.gl.GL_TEXTURE_MIN_FILTER, pyglet.gl.GL_NEAREST)
        self.sprite.draw()