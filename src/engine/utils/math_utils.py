import math as math

class Vector2: 
    x : float
    y : float
    def __init__(self, x : float = 0, y : float = 0) -> None:
        self.x = x
        self.y = y
    
    def __add__(self, other : 'Vector2') -> 'Vector2':
        result : Vector2 = Vector2(self.x + other.x, self.y + other.y)
        return result

    def __sub__(self, other: 'Vector2') -> 'Vector2':
        result : Vector2 = Vector2(self.x - other.x, self.y - other.y)
        return result
    
    def __iadd__(self, other: 'Vector2') -> None:
        self = self + other
    
    def __isub__(self, other: 'Vector2') -> None:
        self = self - other

    def __neg__(self) -> 'Vector2':
        result : 'Vector2' = Vector2(-self.x, -self.y)
        return result
    
    def __abs__(self) -> 'Vector2':
        result : 'Vector2' = Vector2(abs(self.x), abs(self.y))
        return result
    
    def __mul__(self, other : float) -> 'Vector2':
        result : 'Vector2' = Vector2(self.x * other, self.y * other)
        return result
    
    def __div__(self, other : float) -> 'Vector2':
        result : 'Vector2' = Vector2(self.x / other, self.y / other)
        return result

    def __imul__(self, other : float) -> None:
        self = self*other
    
    def __idiv__(self, other : float) -> None:
        self = self/other

    def __eq__(self, other : 'Vector2') -> bool:
        return (self.x == other.x) and (self.y == other.y)

    def __ne__(self, other : 'Vector2') -> bool:
        return not (self == other)

    def lenght(self) -> float:
        result : float = (self.x**2 + self.y**2)**(0.5)
        return result

    def normalized(self) -> 'Vector2':
        lenght = self.lenght()
        if lenght == 0:
            return Vector2(0,0)
        else:
            return self/lenght

    def rotated(self, angle : float) -> 'Vector2':
        sin : float = math.sin(angle)
        cos : float = math.cos(angle)
        result : 'Vector2' = Vector2(self.x*cos - self.y*sin, self.x*sin + self.y*cos)
        return result

    def angle(self) -> float:
        return math.atan2(self.y, self.x)