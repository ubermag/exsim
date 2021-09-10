# import pytest
import discretisedfield as df
import numpy as np
import mag2exp


def test_sans_analytical_parallel_bloch():
    region = df.Region(p1=(-50e-9, -100e-9, 0), p2=(50e-9, 100e-9, 30e-9))
    mesh = df.Mesh(region=region, cell=(5e-9, 5e-9, 1e-9))
    Ms = 1.1e6
    qx = 20e-9

    def m_fun(pos):
        x, y, z = pos
        return [0, Ms*np.sin(2*np.pi*x/qx), Ms*np.cos(2*np.pi*x/qx)]
    m = df.Field(mesh, dim=3, value=m_fun)

    sans = mag2exp.sans.cross_section(m, method='unpol').plane(z=0)
    idx = np.unravel_index(sans.array.argmax(), sans.array.shape)[0:3]
    q = sans.mesh.index2point(idx)[0]
    assert np.isclose(abs(q), 1/qx)
    peaks = (sans.array > 10).sum()
    assert peaks == 2

    sans = mag2exp.sans.cross_section(m, method='pp').plane(z=0)
    idx = np.unravel_index(sans.array.argmax(), sans.array.shape)[0:3]
    q = sans.mesh.index2point(idx)[0]
    assert np.isclose(abs(q), 1/qx)
    peaks = (sans.array > 10).sum()
    assert peaks == 2

    sans = mag2exp.sans.cross_section(m, method='nn').plane(z=0)
    idx = np.unravel_index(sans.array.argmax(), sans.array.shape)[0:3]
    q = sans.mesh.index2point(idx)[0]
    assert np.isclose(abs(q), 1/qx)
    peaks = (sans.array > 10).sum()
    assert peaks == 2

    sans = mag2exp.sans.cross_section(m, method='pn').plane(z=0)
    idx = np.unravel_index(sans.array.argmax(), sans.array.shape)[0:3]
    q = sans.mesh.index2point(idx)[0]
    assert np.isclose(abs(q), 1/qx)
    peaks = (sans.array > 10).sum()
    assert peaks == 2

    sans = mag2exp.sans.cross_section(m, method='np').plane(z=0)
    idx = np.unravel_index(sans.array.argmax(), sans.array.shape)[0:3]
    q = sans.mesh.index2point(idx)[0]
    assert np.isclose(abs(q), 1/qx)
    peaks = (sans.array > 10).sum()
    assert peaks == 2


def test_sans_analytical_parallel_neel():
    region = df.Region(p1=(-50e-9, -100e-9, 0), p2=(50e-9, 100e-9, 30e-9))
    mesh = df.Mesh(region=region, cell=(5e-9, 5e-9, 1e-9))
    Ms = 1.1e6
    qx = 20e-9

    def m_fun(pos):
        x, y, z = pos
        return [Ms*np.sin(2*np.pi*x/qx), 0, Ms*np.cos(2*np.pi*x/qx)]
    m = df.Field(mesh, dim=3, value=m_fun)

    sans = mag2exp.sans.cross_section(m, method='unpol').plane(z=0)
    idx = np.unravel_index(sans.array.argmax(), sans.array.shape)[0:3]
    q = sans.mesh.index2point(idx)[0]
    assert np.isclose(abs(q), 1/qx)
    peaks = (sans.array > 10).sum()
    assert peaks == 2

    sans = mag2exp.sans.cross_section(m, method='pp').plane(z=0)
    idx = np.unravel_index(sans.array.argmax(), sans.array.shape)[0:3]
    q = sans.mesh.index2point(idx)[0]
    assert np.isclose(abs(q), 1/qx)
    peaks = (sans.array > 10).sum()
    assert peaks == 2

    sans = mag2exp.sans.cross_section(m, method='nn').plane(z=0)
    idx = np.unravel_index(sans.array.argmax(), sans.array.shape)[0:3]
    q = sans.mesh.index2point(idx)[0]
    assert np.isclose(abs(q), 1/qx)
    peaks = (sans.array > 10).sum()
    assert peaks == 2

    sans = mag2exp.sans.cross_section(m, method='pn').plane(z=0)
    assert np.isclose(sans.array, 0).all()

    sans = mag2exp.sans.cross_section(m, method='np').plane(z=0)
    assert np.isclose(sans.array, 0).all()


def test_sans_analytical_perpendicular_neel():
    region = df.Region(p1=(-50e-9, -100e-9, 0), p2=(50e-9, 100e-9, 30e-9))
    mesh = df.Mesh(region=region, cell=(5e-9, 5e-9, 1e-9))
    Ms = 1.1e6
    qx = 20e-9

    def m_fun(pos):
        x, y, z = pos
        return [Ms*np.sin(2*np.pi*x/qx), 0, Ms*np.cos(2*np.pi*x/qx)]

    m = df.Field(mesh, dim=3, value=m_fun)
    sans = mag2exp.sans.cross_section(m, polarisation=[1, 0, 0],
                                      method='unpol').plane(z=0)
    idx = np.unravel_index(sans.array.argmax(), sans.array.shape)[0:3]
    q = sans.mesh.index2point(idx)[0]
    assert np.isclose(abs(q), 1/qx)
    peaks = (sans.array > 10).sum()
    assert peaks == 2

    sans = mag2exp.sans.cross_section(m, polarisation=[1, 0, 0],
                                      method='nn').plane(z=0)
    assert np.isclose(sans.array, 0).all()

    sans = mag2exp.sans.cross_section(m, polarisation=[1, 0, 0],
                                      method='pp').plane(z=0)
    assert np.isclose(sans.array, 0).all()

    sans = mag2exp.sans.cross_section(m, polarisation=[1, 0, 0],
                                      method='pn').plane(z=0)
    idx = np.unravel_index(sans.array.argmax(), sans.array.shape)[0:3]
    q = sans.mesh.index2point(idx)[0]
    assert np.isclose(abs(q), 1/qx)
    peaks = (sans.array > 10).sum()
    assert peaks == 2

    sans = mag2exp.sans.cross_section(m, polarisation=[1, 0, 0],
                                      method='np').plane(z=0)
    idx = np.unravel_index(sans.array.argmax(), sans.array.shape)[0:3]
    q = sans.mesh.index2point(idx)[0]
    assert np.isclose(abs(q), 1/qx)
    peaks = (sans.array > 10).sum()
    assert peaks == 2


def test_sans_analytical_perpendicular_bloch():
    region = df.Region(p1=(-50e-9, -100e-9, 0), p2=(50e-9, 100e-9, 30e-9))
    mesh = df.Mesh(region=region, cell=(5e-9, 5e-9, 1e-9))
    Ms = 1.1e6
    qx = 20e-9

    def m_fun(pos):
        x, y, z = pos
        return [0, Ms*np.sin(2*np.pi*x/qx), Ms*np.cos(2*np.pi*x/qx)]

    m = df.Field(mesh, dim=3, value=m_fun)
    sans = mag2exp.sans.cross_section(m, polarisation=[1, 0, 0],
                                      method='unpol').plane(z=0)
    idx = np.unravel_index(sans.array.argmax(), sans.array.shape)[0:3]
    q = sans.mesh.index2point(idx)[0]
    assert np.isclose(abs(q), 1/qx)
    peaks = (sans.array > 10).sum()
    assert peaks == 2

    sans = mag2exp.sans.cross_section(m, polarisation=[1, 0, 0],
                                      method='nn').plane(z=0)
    assert np.isclose(sans.array, 0).all()

    sans = mag2exp.sans.cross_section(m, polarisation=[1, 0, 0],
                                      method='pp').plane(z=0)
    assert np.isclose(sans.array, 0).all()

    sans = mag2exp.sans.cross_section(m, polarisation=[1, 0, 0],
                                      method='pn').plane(z=0)
    idx = np.unravel_index(sans.array.argmax(), sans.array.shape)[0:3]
    q = sans.mesh.index2point(idx)[0]
    assert np.isclose(q, 1/qx)
    peaks = (sans.array > 10).sum()
    assert peaks == 1

    sans = mag2exp.sans.cross_section(m, polarisation=[1, 0, 0],
                                      method='np').plane(z=0)
    idx = np.unravel_index(sans.array.argmax(), sans.array.shape)[0:3]
    q = sans.mesh.index2point(idx)[0]
    assert np.isclose(q, -1/qx)
    peaks = (sans.array > 10).sum()
    assert peaks == 1


def test_sans_chiral_parallel():
    region = df.Region(p1=(-50e-9, -100e-9, 0), p2=(50e-9, 100e-9, 30e-9))
    mesh = df.Mesh(region=region, cell=(5e-9, 5e-9, 1e-9))
    Ms = 1.1e6
    qx = 20e-9

    def m_fun(pos):
        x, y, z = pos
        return [Ms*np.sin(2*np.pi*x/qx), 0, Ms*np.cos(2*np.pi*x/qx)]
    m = df.Field(mesh, dim=3, value=m_fun)
    cf = mag2exp.sans.chiral_function(m).plane(z=0)
    assert np.isclose(cf.array, 0).all()

    def m_fun(pos):
        x, y, z = pos
        return [0, Ms*np.sin(2*np.pi*x/qx), Ms*np.cos(2*np.pi*x/qx)]
    m = df.Field(mesh, dim=3, value=m_fun)
    cf = mag2exp.sans.chiral_function(m).plane(z=0)
    assert np.isclose(cf.array, 0).all()


def test_sans_chiral_perpendicular():
    region = df.Region(p1=(-50e-9, -50e-9, -50e-9), p2=(50e-9, 50e-9, 50e-9))
    mesh = df.Mesh(region=region, cell=(5e-9, 5e-9, 5e-9))
    Ms = 1.1e6
    qx = 20e-9

    def m_fun(pos):
        x, y, z = pos
        return [0, Ms*np.sin(2*np.pi*x/qx), Ms*np.cos(2*np.pi*x/qx)]

    m = df.Field(mesh, dim=3, value=m_fun)
    cf = mag2exp.sans.chiral_function(m, polarisation=[1, 0, 0]).plane(z=0)
    idx = np.unravel_index(cf.array.argmax(), cf.array.shape)[0:3]
    q = cf.mesh.index2point(idx)[0]
    assert np.isclose(q, 1/qx)
    peaks = (cf.array > 10).sum()
    assert peaks == 1
    idx = np.unravel_index(cf.array.argmin(), cf.array.shape)[0:3]
    q = cf.mesh.index2point(idx)[0]
    assert np.isclose(q, -1/qx)
    peaks = (cf.array < -10).sum()
    assert peaks == 1

    def m_fun(pos):
        x, y, z = pos
        return [Ms*np.sin(2*np.pi*x/qx), 0, Ms*np.cos(2*np.pi*x/qx)]

    m = df.Field(mesh, dim=3, value=m_fun)
    cf = mag2exp.sans.chiral_function(m, polarisation=[1, 0, 0]).plane(z=0)
    assert np.isclose(cf.array, 0).all()
