"""
"""
import numpy as np
from astropy.utils.misc import NumpyRNGContext

from rotations.rotate_vector_collection import rotate_vector_collection
from rotations.rotations2d import *

__all__ = ('test_rotation_matrices_from_vectors',
           'test_rotation_matrices_from_angles',
           'test_rotation_matrices_from_basis' )

fixed_seed = 43


def test_rotation_matrices_from_vectors_1():
    """
    test to make sure null rotations return identiy matrix
    """

    N = 1000
    
    v1 = np.random.random((N,2))
    rot_m = rotation_matrices_from_vectors(v1,v1)
    assert np.all(~np.isnan(rot_m))


def test_rotation_matrices_from_vectors():
    """
    validate 90 degree rotation result
    """

    N = 1000

    v1 = np.zeros((N,2))
    v1[:,0] = 1
    v2 = np.zeros((N,2))
    v2[:,1] = 1

    rot_m = rotation_matrices_from_vectors(v1,v2)

    v3 = rotate_vector_collection(rot_m, v1)

    assert np.allclose(v2,v3)


def test_rotation_matrices_from_angles():
    """
    test to make sure null rotations return identiy matrix
    """

    npts = 1000
    ndim = 2

    rot_m = rotation_matrices_from_angles(np.zeros(npts))

    assert np.all(~np.isnan(rot_m))


def test_rotation_matrices_from_basis():
    """
    test to make sure null rotations return identiy matrix
    """

    npts = 1000
    ndim = 2

    ux = np.zeros((npts,ndim))
    ux[:,0] = 1.0
    uy = np.zeros((npts,ndim))
    uy[:,1] = 1.0

    rot_m = rotation_matrices_from_basis(ux, uy)

    assert np.all(~np.isnan(rot_m))
