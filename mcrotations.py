r"""
A set of rotation utilites that apply monte carlo
roations to collections of 2D and 3D vectors
"""


from __future__ import (division, print_function, absolute_import,
                        unicode_literals)
import numpy as np
from astropy.utils.misc import NumpyRNGContext
from .vector_calculations import *


__all__=['random_rotation_3d', 'random_rotation_2d',
         'random_perpendicular_directions']
__author__ = ['Duncan Campbell']


def random_rotation_3d(vectors, seed=None):
    r"""
    Apply a random rotation to a set of 3d vectors.

    Parameters
    ----------
    vectors : ndarray
        Numpy array of shape (npts, 3) storing a collection of 3d vectors
    
    seed : int, optional
        Random number seed
    
    Returns
    -------
    rotated_vectors : ndarray
        Numpy array of shape (npts, 3) storing a collection of 3d vectors
    """

    ran_angle = np.random.random(size=1)*(np.pi)
    
    with NumpyRNGContext(seed):
        ran_direction = normalized_vectors(np.random.random((3,)))*2.0 - 1.0
    
    ran_rot = rotation_matrices_from_angles(ran_angle, ran_direction)

    return rotate_vector_collection(ran_rot, vectors)


def random_rotation_2d(vectors, seed=None):
    r"""
    Apply a random rotation to a set of 3d vectors.

    Parameters
    ----------
    vectors : ndarray
        Numpy array of shape (npts, 3) storing a collection of 3d vectors
    
    seed : int, optional
        Random number seed
    
    Returns
    -------
    rotated_vectors : ndarray
        Numpy array of shape (npts, 3) storing a collection of 3d vectors
    """

    ran_angle = np.random.random(size=1)*(np.pi)

    with NumpyRNGContext(seed):
        ran_direction = normalized_vectors(np.random.random((2,)))*2.0 - 1.0
    
    ran_rot = rotation_matrices_from_angles(ran_angle, ran_direction)

    return rotate_vector_collection(ran_rot, vectors)


def random_perpendicular_directions(v, seed=None):
    r"""
    Given an input list of 3d vectors, v, return a list of 3d vectors
    such that each returned vector has unit-length and is
    orthogonal to the corresponding vector in v.
    
    Parameters
    ----------
    v : ndarray
        Numpy array of shape (npts, 3) storing a collection of 3d vectors
    
    seed : int, optional
        Random number seed used to choose a random orthogonal direction
    
    Returns
    -------
    result : ndarray
        Numpy array of shape (npts, 3)
    """

    v = np.atleast_2d(v)
    npts = v.shape[0]
    
    with NumpyRNGContext(seed):
        w = np.random.random((npts, 3))

    vnorms = elementwise_norm(v).reshape((npts, 1))
    wnorms = elementwise_norm(w).reshape((npts, 1))

    e_v = v/vnorms
    e_w = w/wnorms

    v_dot_w = elementwise_dot(e_v, e_w).reshape((npts, 1))

    e_v_perp = e_w - v_dot_w*e_v
    e_v_perp_norm = elementwise_norm(e_v_perp).reshape((npts, 1))
    
    return e_v_perp/e_v_perp_norm

