from math import sqrt, sin, cos, tan


def is_scalar(other):
    return type(other) in [int, float]

def is_vector2(other):
    return type(other) is Vector2

def is_vector3(other):
    return type(other) is Vector3


class Vector2:
    def __init__(self, x=0, y=0, thetta=None) -> None:
        if thetta is not None:
            self.x = cos(thetta)
            self.y = sin(thetta)
        elif not is_scalar(x):
            self.x = x[0]
            self.y = x[1]
        else:
            self.x = x
            self.y = y

    def apply_func(self, func): # apply a function in elements of the vector
        for i, v in enumerate(self):
            self[i] = func(v)

    def __iter__(self):
        yield self.x
        yield self.y

    def __getitem__(self, index):
        return list(self)[index]
    
    def __setitem__(self, index, value):
        if index == 0:
            self.x = value
            return
        if index == 1:
            self.y = value
        return
    
    def __neg__(self): # -Vector2
        return self.__mul__(-1)
    
    def __pos__(self): # +Vector2
        return self

    def __add__(self, other): # Vector2 + Vector2
        if is_vector2(other):
            return Vector2(self.x + other.x, self.y + other.y)
        return None
    
    def __sub__(self, other): # Vector2 - Vector2
        if is_vector2(other):
            return self.__add__(-other)
        return None
    
    def __mul__(self, other): # Vector2 * Vector2 | Vector2 * Scalar
        if is_scalar(other):
            return Vector2(self.x * other, self.y * other)
        else:
            return Vector2(self.x * other.x, self.y * other.y)

    def __rmul__(self, other): # Vector2 * Vector2 | Scalar * Vector2
        if is_scalar(other):
            return Vector2(self.x * other, self.y * other)
        else:
            return Vector2(self.x * other.x, self.y * other.y)
        
    def __truediv__(self, other): # Vector2 / Vector2 | Vector2 / Scalar
        if is_scalar(other):
            return Vector2(self.x / other, self.y / other)
        else:
            return Vector2(self.x / other.x, self.y / other.y)

    def __rtruediv__(self, other): # Vector2 / Vector2 | Scalar / Vector2
        if is_scalar(other):
            return Vector2(other / self.x, other / self.y)
        else:
            return Vector2(other.x / self.x, other.y / self.y)

    def __pow__(self, other): # Vector2 ^ Scalar
        if is_scalar(other):
            return Vector2(self.x ** other, self.y ** other)
        return None
    
    def rotate(self, thetta): # Rotate
        s, c = sin(thetta), cos(thetta)
        return Vector2(self.x * c - self.y * s, self.x * s + self.y * c)
    
    def dot(self, other): # Dot Product <Scalar>
        if is_vector2(other):
            return self.x * other.x + self.y * other.y
        return None
    
    def cross(self, other): # Cross Product <Scalar>
        if is_vector2(other):
            return self.x * other.y - self.y * other.x
        return None
    
    def magnitude(self):
        return sqrt(self.x*self.x + self.y*self.y)
    
    def normalize(self):
        return self / self.magnitude()
    
    def distance(self, other):
        if is_vector2(other):
            return (self - other).magnitude()
        return None
    
    def get_angle(self):
        return tan(self.x / self.y)


class Vector3:
    def __init__(self, x=0, y=0, z=0) -> None:
        if not is_scalar(x):
            self.x = x[0]
            self.y = x[1]
            self.z = x[2]
        else:
            self.x = x
            self.y = y
            self.z = z

    def apply_func(self, func): # apply a function in elements of the vector
        for i, v in enumerate(self):
            self[i] = func(v)

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z

    def __getitem__(self, index):
        return list(self)[index]
    
    def __setitem__(self, index, value):
        if index == 0:
            self.x = value
            return
        if index == 1:
            self.y = value
            return
        if index == 2:
            self.z = value
        return
    
    def __neg__(self): # -Vector3
        return self.__mul__(-1)
    
    def __pos__(self): # +Vector3
        return self

    def __add__(self, other): # Vector3 + Vector3
        if is_vector3(other):
            return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
        return None
    
    def __sub__(self, other): # Vector3 - Vector3
        if is_vector3(other):
            return self.__add__(-other)
        return None
    
    def __mul__(self, other): # Vector3 * Vector3 | Vector3 * Scalar
        if is_scalar(other):
            return Vector3(self.x * other, self.y * other, self.z * other)
        else:
            return Vector3(self.x * other.x, self.y * other.y, self.z * other.z)

    def __rmul__(self, other): # Vector3 * Vector3 | Scalar * Vector3
        if is_scalar(other):
            return Vector3(self.x * other, self.y * other, self.z * other)
        else:
            return Vector3(self.x * other.x, self.y * other.y, self.z * other)
        
    def __truediv__(self, other): # Vector3 / Vector3 | Vector3 / Scalar
        if is_scalar(other):
            return Vector3(self.x / other, self.y / other, self.z / other)
        else:
            return Vector3(self.x / other.x, self.y / other.y, self.z / other.z)

    def __rtruediv__(self, other): # Vector3 / Vector3 | Scalar / Vector3
        if is_scalar(other):
            return Vector3(other / self.x, other / self.y, other / self.z)
        else:
            return Vector3(other.x / self.x, other.y / self.y, other.z / self.z)

    def __pow__(self, other): # Vector3 ^ Scalar
        if is_scalar(other):
            return Vector3(self.x ** other, self.y ** other, self.z ** other)
        return None
    
    def rotateX(self, thetta): # Rotate in X axis
        c, s = cos(thetta), sin(thetta)
        return Vector3(self.x, self.y * c + self.z * s, self.z * c - self.y * s)

    def rotateY(self, thetta): # Rotate in Y axis
        c, s = cos(thetta), sin(thetta)
        return Vector3(self.x * c + self.z * s, self.y, self.z * c - self.x * s)
    
    def rotateZ(self, thetta): # Rotate in Z axis
        c, s = cos(thetta), sin(thetta)
        return Vector3(self.x * c - self.y * s, self.x * s + self.y * c, self.z)
    
    def dot(self, other): # Dot Product <Scalar>
        if is_vector3(other):
            return self.x * other.x + self.y * other.y + self.z * other.z
        return None
    
    def cross(self, other): # Cross Product <Vector3>
        if is_vector3(other):
            return Vector3(self.y * other.z - self.z * other.y, self.z * other.x - self.x * other.z, self.x * other.y - self.y * other.x)
        return None
    
    def magnitude(self):
        return sqrt(self.x*self.x + self.y*self.y + self.z*self.z)
    
    def normalize(self):
        return self / self.magnitude()
    
    def distance(self, other):
        if is_vector3(other):
            return (self - other).magnitude()
        return None