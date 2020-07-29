import numpy as np


class Point:
    """A point."""

    def __init__(self, point):
        self._point = np.array(point, dtype=float)

    def __repr__(self):
        return f"Point({self._point.tolist()})"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Point(self._point + other._vector)
        return NotImplemented

    def __radd__(self, other):
        if isinstance(other, Vector):
            return Point(other._vector + self._point)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Point):
            return Vector(self._point - other._point)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Point):
            return np.array_equal(other._point, self._point)
        return False


class Vector:
    """A vector."""

    def __init__(self, vector):
        self._vector = np.array(vector, dtype=float)

    def __repr__(self):
        return f"Vector({self._vector.tolist()})"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self._vector + other._vector)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self._vector - other._vector)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Vector):
            return np.array_equal(other._vector, self._vector)
        return False


class Ray:
    """A ray."""
    def __init__(self,origin=Point, direction=Vector):
        self._ray = np.array((origin, direction))
        self._origin = origin
        self._direction = np.array(direction._vector)
        self._direction = Vector((self._direction - origin._point)/(np.sqrt(np.sum((self._direction - origin._point)**2))))
    ...
    def __repr__(self):
        return f"Ray({self._ray})"

    def __eq__(self,other):
        if isinstance(other, Ray):
            if np.array_equal(self._ray, other._ray):
                return True
            else:
                return False
        return NotImplemented
    ...


class Sphere:
    """A sphere."""
    def __init__(self,center=Point,radius=float):
        self._sphere = np.array((center, radius), dtype=object)
        self._center = center
        self._radius = float(radius)

    def __repr__(self):
        return f"Sphere({self._sphere})"
    
    def __eq__(self,other):
        if isinstance(other,Sphere):
            if np.array_equal(self._sphere, other._sphere):
                return True
            else:
                return False
        return NotImplemented
    ...


class Triangle:
    """A triangle."""

    ...