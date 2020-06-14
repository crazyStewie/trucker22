import pymunk
from enum import Enum
from typing import List

class BodyType(Enum):
    DYNAMIC = 1
    STATIC = 2
    KINEMATIC = 3

class PhysicsServer:
    _instance = None
    _space = pymunk.Space

    def __init__(self):
        self._space = pymunk.Space()
    
    def body_create(self, body_type : BodyType) -> pymunk.Body:
        body : pymunk.Body
        if body_type == BodyType.DYNAMIC:
            body = pymunk.Body(body_type=pymunk.Body.DYNAMIC)
        elif body_type == BodyType.STATIC:
            body = pymunk.Body(body_type=pymunk.Body.STATIC)
        elif body_type == BodyType.KINEMATIC:
            body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        return body
    

    def commit(self, body : pymunk.Body, shapes : List[pymunk.Shape]):
        if body is not None:
            self._space.add(body)
        for s in shapes:
            self._space.add(s)

    def remove(self, body : pymunk.Body, shapes : List[pymunk.Shape]):
        if body is not None:
            self._space.remove(body)
        for s in shapes:
            self._space.remove(s)

    def step(self, delta : float):
        self._space.step(delta)

    @classmethod
    def instance(cls) -> 'PhysicsServer':
        if cls._instance == None:
            cls._instance = cls()
        return cls._instance
