import pyglet
import pymunk
class Marker:
    def __init__(self, position : (float, float), vertical : bool = False):
        self.image = pyglet.image.load("rsc/marker.png")
        self.sprite = pyglet.sprite.Sprite(self.image, subpixel = True)
        self.position = pymunk.Vec2d(position)
        self.vertical = vertical
        if not vertical:
            self.sprite.update(rotation=90.0)

    def update(self, delta : float):
        pass
    
    def check_win(self, container : pymunk.Body) -> bool:
        points = [container.local_to_world((-3,-12)), container.local_to_world((3,-12)), container.local_to_world((3,12)), container.local_to_world((-3,12))]
        won = True
        (dx, dy) = (10, 26) if self.vertical else (26,-10)
        limits = {'x': (min(self.position.x, self.position.x + dx), 
                        max(self.position.x, self.position.x + dx)), 
                  'y': (min(self.position.y, self.position.y + dy), 
                        max(self.position.y, self.position.y + dy))}
        for point in points:
            if (point.x < limits['x'][0] or point.x > limits['x'][1]) or (point.y < limits['y'][0] or point.y > limits['y'][1]):
                won = False
        return won;

    def draw(self):
        self.sprite.position = self.position
        pyglet.gl.glTexParameteri(pyglet.gl.GL_TEXTURE_2D, pyglet.gl.GL_TEXTURE_MAG_FILTER, pyglet.gl.GL_NEAREST) 
        pyglet.gl.glTexParameteri(pyglet.gl.GL_TEXTURE_2D, pyglet.gl.GL_TEXTURE_MIN_FILTER, pyglet.gl.GL_NEAREST)
        self.sprite.draw()