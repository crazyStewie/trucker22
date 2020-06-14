from ..engine.tree.physics_node import PhysicsNode
from ..engine.base.physics_server import PhysicsServer, BodyType
import pymunk
import pyglet
from pyglet.window import key


class Player(PhysicsNode):
    def __init__(self):
        super().__init__("Player", BodyType.DYNAMIC)
        physics_server = PhysicsServer.instance();
        self.shape = pymunk.Poly(self.body, [(-3,-6), (3,-6), (3,6),(-3,6)])
        self.shape.density = 1
        self.body.position = pymunk.Vec2d(16,4)
        self.steering = 0
        self.power = 0
        self.keys = key.KeyStateHandler()
        self.image = pyglet.image.load("rsc/player.png")
        self.image.anchor_x = 3
        self.image.anchor_y = 6
        self.sprite = pyglet.sprite.Sprite(self.image, subpixel = True)
        self.friction = 1000
        
        self.damage = 0
        self.damage_factor = 1/20000

        self.cont_body = pymunk.body.Body()
        self.cont_shape = pymunk.Poly(self.cont_body, [(-3,-12), (3,-12), (3,12),(-3,12)])
        self.cont_shape.density = 1
        self.cont_image = pyglet.image.load("rsc/container.png")
        self.cont_image.anchor_x = 3
        self.cont_image.anchor_y = 12
        self.cont_sprite = pyglet.sprite.Sprite(self.cont_image, subpixel = True)
        self.cont_body.position = pymunk.Vec2d(16,-10)

        self.cabin_body = pymunk.body.Body()
        self.cabin_shape = pymunk.Poly(self.cabin_body, [(-3, -3),(3, -3),(3, 3),(-3, 3)])
        self.cabin_shape.density = 1
        self.cabin_body.position = pymunk.Vec2d(16,7)
        self.cabin_joint_constraint = pymunk.SimpleMotor(self.body, self.cabin_body, 0)
        self.cabin_joint = pymunk.PivotJoint(self.body, self.cabin_body, (16,3))
        self.cabin_joint.collide_bodies = False

        self.joint = pymunk.constraint.PivotJoint(self.body, self.cont_body, (16.0, 0.0))
        self.joint.collide_bodies = False
        physics_server._space.add(self.body, self.shape, self.cont_body, self.cont_shape, self.joint, self.cabin_body, self.cabin_shape, self.cabin_joint, self.cabin_joint_constraint)
        
        
    def update_damage(self, arbiter : pymunk.Arbiter):
        self.damage += self.damage_factor*arbiter.total_impulse.get_length()
    
    def update(self, delta : float):
        self.cont_body.each_arbiter(self.update_damage)
        print(self.damage)
        forward : pymunk.Vec2d = pymunk.Vec2d(0, 1).rotated(self.body.angle).normalized()
        right : pymunk.Vec2d = forward.rotated_degrees(-90).normalized()
        max_steering = 0.6
        max_power = 100
        self.steering = 0
        self.power = 0
        back_wheel = forward
        front_wheel = forward
        if self.keys[key.D]:
            self.steering -= max_steering
        if self.keys[key.A]:
            self.steering += max_steering
        front_wheel = front_wheel.rotated(self.steering)
        if self.keys[key.W]:
            self.power += 10
        if self.keys[key.S]:
            self.power -= 10
        if self.keys[key.SPACE]:
            self.power = -10*self.body.velocity_at_local_point((0, 4)).dot(front_wheel)
        front_wheel_velocity : pymunk.Vec2d = self.body.velocity_at_local_point((0, 4))
        back_wheel_velocity : pymunk.Vec2d = self.body.velocity_at_local_point((0, -4))
        back_wheel_friction = -back_wheel_velocity.projection(back_wheel.rotated_degrees(90))
        front_wheel_friction = -front_wheel_velocity.projection(front_wheel.rotated_degrees(90))
        power =100*front_wheel*self.power
        self.body.apply_force_at_world_point(self.friction*front_wheel_friction, self.body.local_to_world((0, 4)))
        self.body.apply_force_at_world_point(self.friction*back_wheel_friction, self.body.local_to_world((0, -4)))
        self.body.apply_force_at_world_point(power, self.body.local_to_world((0, 4)))

        cont_back_wheel_velocity : pymunk.Vec2d = self.cont_body.velocity_at_local_point((0, -10))
        cont_direction = pymunk.Vec2d(0, 1).rotated(self.cont_body.angle).normalized()
        cont_back_wheel_friction = -cont_back_wheel_velocity.projection(cont_direction.rotated_degrees(90))
        self.cont_body.apply_force_at_world_point(self.friction*cont_back_wheel_friction, self.cont_body.local_to_world((0, -10)))
    def draw(self):
        self.sprite.update(x = self.body.position.x, y =self.body.position.y, rotation = -self.body.rotation_vector.get_angle_degrees())
        pyglet.gl.glTexParameteri(pyglet.gl.GL_TEXTURE_2D, pyglet.gl.GL_TEXTURE_MAG_FILTER, pyglet.gl.GL_NEAREST) 
        pyglet.gl.glTexParameteri(pyglet.gl.GL_TEXTURE_2D, pyglet.gl.GL_TEXTURE_MIN_FILTER, pyglet.gl.GL_NEAREST)
        self.sprite.draw()
        self.cont_sprite.update(x = self.cont_body.position.x, y =self.cont_body.position.y, rotation = -self.cont_body.rotation_vector.get_angle_degrees())
        pyglet.gl.glTexParameteri(pyglet.gl.GL_TEXTURE_2D, pyglet.gl.GL_TEXTURE_MAG_FILTER, pyglet.gl.GL_NEAREST) 
        pyglet.gl.glTexParameteri(pyglet.gl.GL_TEXTURE_2D, pyglet.gl.GL_TEXTURE_MIN_FILTER, pyglet.gl.GL_NEAREST)
        self.cont_sprite.draw()
        