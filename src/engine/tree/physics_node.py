from .node_2d import Node2D
from .node import Node
from typing import List
from .shape_node import ShapeNode
from ..base.physics_server import PhysicsServer
from ..base.physics_server import BodyType
import pymunk

class PhysicsNode(Node2D):
    body : pymunk.Body
    shapes : List[pymunk.Shape]
    def __init__(self, name:str, body_type : BodyType):
        super().__init__(name)
        physics_server = PhysicsServer.instance()
        self.body = physics_server.body_create(body_type)

    def add_child(self, child: Node):
        if isinstance(child, ShapeNode):
            self.shapes.append(child.shape)
            child.shape.body = self.body
            if self.in_tree:
                physics_server = PhysicsServer.instance()
                physics_server.commit(None, [child.shape])
    
    def add_to_tree(self):
        physics_server = PhysicsServer.instance()
        physics_server.commit(self.body, self.shapes)

    def remove_from_tree(self):
        physics_server = PhysicsServer.instance()
        physics_server.remove(self.body, self.shapes)
