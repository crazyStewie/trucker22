import pymunk
import pyglet
from ..engine.base.physics_server import PhysicsServer
class Scenario:
    def __init__(self):
        physics_server = PhysicsServer.instance()
        self.static = pymunk.Body(body_type = pymunk.Body.STATIC)
        physics_server._space.add(self.static)
        physics_server._space.add(pymunk.Segment(self.static, (8, -24), (8, 112), 0))
        physics_server._space.add(pymunk.Segment(self.static, (8, 112), (152, 112), 0))
        physics_server._space.add(pymunk.Segment(self.static, (152, 112), (152, 8), 0))
        physics_server._space.add(pymunk.Segment(self.static, (152, 8), (24, 8), 0))
        physics_server._space.add(pymunk.Segment(self.static, (24, 8), (24, -24), 0))
        physics_server._space.add(pymunk.Segment(self.static, (24, -24), (8, -24), 0))
        self.image = pyglet.image.load("rsc/arena.png")
        self.image.anchor_x = 0
        self.image.anchor_y = 0
        self.sprite = pyglet.sprite.Sprite(self.image, subpixel = True)
        points = [pymunk.Vec2d(29, 8), (38, 8), (47, 8), (56, 8)]
        self.sprites = []
        self.containers = []
        self.container_image = pyglet.image.load("rsc/container.png")
        self.container_image.anchor_x = 3
        self.container_image.anchor_y = 12
        for point in points:
            body = pymunk.Body()
            shape = pymunk.Poly(body, [(-3,-12), (3,-12), (3,12),(-3,12)])
            shape.density = 1
            sprite = pyglet.sprite.Sprite(self.container_image, subpixel = True)
            body.position = point + pymunk.Vec2d(3, 12)
            physics_server._space.add(body, shape)
            self.sprites.append(sprite)
            self.containers.append(body)
    
    def update(self, delta : float):
        points = [(-3,-12), (3,-12), (3,12),(-3,12)]
        friction = 500
        for container in self.containers:
            for point in points:
                container.apply_force_at_local_point(-friction*container.velocity_at_local_point(point), point)


        pass

    def draw(self):
        pyglet.gl.glTexParameteri(pyglet.gl.GL_TEXTURE_2D, pyglet.gl.GL_TEXTURE_MAG_FILTER, pyglet.gl.GL_NEAREST) 
        pyglet.gl.glTexParameteri(pyglet.gl.GL_TEXTURE_2D, pyglet.gl.GL_TEXTURE_MIN_FILTER, pyglet.gl.GL_NEAREST)
        self.sprite.draw()
        for i in range(len(self.sprites)):
            self.sprites[i].update(x = self.containers[i].position.x, y =self.containers[i].position.y, rotation = -self.containers[i].rotation_vector.get_angle_degrees())
            pyglet.gl.glTexParameteri(pyglet.gl.GL_TEXTURE_2D, pyglet.gl.GL_TEXTURE_MAG_FILTER, pyglet.gl.GL_NEAREST) 
            pyglet.gl.glTexParameteri(pyglet.gl.GL_TEXTURE_2D, pyglet.gl.GL_TEXTURE_MIN_FILTER, pyglet.gl.GL_NEAREST)
            self.sprites[i].draw()
        pass