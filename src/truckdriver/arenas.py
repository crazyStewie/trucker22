import pymunk
import pyglet
from ..engine.base.physics_server import PhysicsServer
import math

class Arena:
    def update(self, delta : float):
        points = [(-3,-12), (3,-12), (3,12),(-3,12)]
        friction = self.friction
        for container in self.containers:
            for point in points:
                container.apply_force_at_world_point(-friction*container.velocity_at_local_point(point), container.local_to_world(point))

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

class Arena1(Arena):
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
        self.image = pyglet.image.load("rsc/arena1.png")
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
        
        self.friction = 500
    

class Arena2(Arena):
    def __init__(self):
        physics_server = PhysicsServer.instance()
        self.static = pymunk.Body(body_type = pymunk.Body.STATIC)
        physics_server._space.add(self.static)
        physics_server._space.add(pymunk.Segment(self.static, (8, -24), (8, 112), 0))
        physics_server._space.add(pymunk.Segment(self.static, (8, 112), (128, 112), 0))
        physics_server._space.add(pymunk.Segment(self.static, (128, 112), (128, 8), 0))
        physics_server._space.add(pymunk.Segment(self.static, (128, 8), (24, 8), 0))
        physics_server._space.add(pymunk.Segment(self.static, (24, 8), (24, -24), 0))
        physics_server._space.add(pymunk.Segment(self.static, (24, -24), (8, -24), 0))
        physics_server._space.add(pymunk.Poly(self.static, [(7*8, 6*8),(10*8, 6*8),(10*8, 9*8),(7*8, 9*8)]))
        self.image = pyglet.image.load("rsc/arena2.png")
        self.image.anchor_x = 0
        self.image.anchor_y = 0
        self.sprite = pyglet.sprite.Sprite(self.image, subpixel = True)
        points = [pymunk.Vec2d(102, 20), (10, 31), (102, 65), (10, 40)]
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
            physics_server._space.add(body, shape)
            body.position = point + pymunk.Vec2d(12, 3)
            body.angle = math.pi/2
            self.sprites.append(sprite)
            self.containers.append(body)
    
        self.friction = 100


class Arena3(Arena):
    def __init__(self):
        physics_server = PhysicsServer.instance()
        self.static = pymunk.Body(body_type = pymunk.Body.STATIC)
        physics_server._space.add(self.static)
        physics_server._space.add(pymunk.Segment(self.static, (8, -24), (8, 52), 0))
        physics_server._space.add(pymunk.Segment(self.static, (8, 52), (60, 52), 0))
        physics_server._space.add(pymunk.Segment(self.static, (60, 52), (60, 38), 0))
        physics_server._space.add(pymunk.Segment(self.static, (60, 38), (100, 38), 0))
        physics_server._space.add(pymunk.Segment(self.static, (100, 38), (100, 82), 0))
        physics_server._space.add(pymunk.Segment(self.static, (100, 82), (60, 82), 0))
        physics_server._space.add(pymunk.Segment(self.static, (60, 82), (60, 68), 0))
        physics_server._space.add(pymunk.Segment(self.static, (60, 68), (8, 68), 0))
        physics_server._space.add(pymunk.Segment(self.static, (8, 68), (8, 112), 0))
        physics_server._space.add(pymunk.Segment(self.static, (8, 112), (60, 112), 0))
        physics_server._space.add(pymunk.Segment(self.static, (60, 112), (60, 94), 0))
        physics_server._space.add(pymunk.Segment(self.static, (60, 94), (100, 94), 0))
        physics_server._space.add(pymunk.Segment(self.static, (100, 94), (100, 112), 0))
        physics_server._space.add(pymunk.Segment(self.static, (100, 112), (152, 112), 0))
        physics_server._space.add(pymunk.Segment(self.static, (152, 112), (152, 8), 0))
        physics_server._space.add(pymunk.Segment(self.static, (152, 8), (100, 8), 0))
        physics_server._space.add(pymunk.Segment(self.static, (100, 8), (100, 26), 0))
        physics_server._space.add(pymunk.Segment(self.static, (100, 26), (60, 26), 0))
        physics_server._space.add(pymunk.Segment(self.static, (60, 26), (60, 8), 0))
        physics_server._space.add(pymunk.Segment(self.static, (60, 8), (24, 8), 0))

        physics_server._space.add(pymunk.Segment(self.static, (24, 8), (24, -24), 0))
        physics_server._space.add(pymunk.Segment(self.static, (24, -24), (8, -24), 0))
        physics_server._space.add(pymunk.Poly(self.static, [(7*8, 6*8),(10*8, 6*8),(10*8, 9*8),(7*8, 9*8)]))
        self.image = pyglet.image.load("rsc/arena3.png")
        self.image.anchor_x = 0
        self.image.anchor_y = 0
        self.sprite = pyglet.sprite.Sprite(self.image, subpixel = True)
        points = [] #[pymunk.Vec2d(102, 20), (10, 31), (102, 65), (10, 40)]
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
            physics_server._space.add(body, shape)
            body.position = point + pymunk.Vec2d(12, 3)
            body.angle = math.pi/2
            self.sprites.append(sprite)
            self.containers.append(body)
    
        self.friction = 100
