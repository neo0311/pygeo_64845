from .objects import Ray, Sphere, Triangle, Point, Vector
import numpy as np

def intersect(first_object, second_object):
    ...


def _intersect_ray_with_sphere(ray, sphere):
    ray._origin = ray._origin._point
    ray._direction = ray._direction._vector
    sphere._center= sphere._center._point
    nabla = (np.dot(ray._direction,(ray._origin - sphere._center))**2 - (np.linalg.norm((ray._origin - sphere._center))**2 - sphere._radius**2))
    if nabla < 0:
        return "No Intersecction"

    if nabla == 0:
        return -1*np.dot(ray._direction,(ray._origin - sphere._center))

    if nabla > 0:
        if np.sum((ray._origin - sphere._center)**2) <= sphere._radius**2:
            d1 = -1*np.dot(ray._direction,(ray._origin - sphere._center)) + np.sqrt(nabla)
            vector_1 = d1*(ray._direction/np.sqrt(np.sum(ray._direction**2)))   + ray._origin
            point_1 = np.round(((ray._origin - 0*ray._origin) + (vector_1 - ray._origin)),decimals=2)
            return Point(point_1)

        if np.sum((ray._origin - sphere._center)**2 )> sphere._radius**2:
            d2 = -1*np.dot(ray._direction,(ray._origin - sphere._center)) + np.sqrt(nabla)
            d1 = -1*np.dot(ray._direction,(ray._origin - sphere._center)) - np.sqrt(nabla)
            vector_1 = d1*(ray._direction/np.sqrt(np.sum(ray._direction**2)))   + ray._origin
            vector_2 = d2*(ray._direction/np.sqrt(np.sum(ray._direction**2))) + ray._origin
            point_1 = np.round(((ray._origin - 0*ray._origin) + (vector_1 - ray._origin)),decimals=2)
            point_2 = np.round(((ray._origin - 0*ray._origin) + (vector_2 - ray._origin)),decimals=2)
            if np.isclose(((point_1 - ray._origin )/(np.sqrt(np.sum((point_1 - ray._origin)**2)))), ray._direction).all():
                return Point(point_1),Point(point_2)
            else:
                return "No Intersecction"
    ...


def _intersect_ray_with_triangle(ray, triangle):
    ...
