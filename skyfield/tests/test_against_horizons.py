'Auto-generated accuracy tests vs HORIZONS (build_horizons_tests.py).'

from numpy import max
from skyfield import api
from skyfield.constants import AU_M
from skyfield.jpllib import Kernel

one_second = 1.0 / 24.0 / 60.0 / 60.0
arcsecond = 1.0 / 60.0 / 60.0
ra_arcsecond = 24.0 / 360.0 / 60.0 / 60.0
meter = 1.0 / AU_M

def compare(value, expected_value, epsilon):
    if hasattr(value, 'shape') or hasattr(expected_value, 'shape'):
        assert max(abs(value - expected_value)) <= epsilon
    else:
        assert abs(value - expected_value) <= epsilon

def test_jupiter1():
    astrometric = api.sun(utc=(1980, 1, 1, 0, 0)).observe(api.jupiter)
    hlat, hlon, d = astrometric.ecliptic_latlon()
    compare(hlat.degrees, 1.013, 0.001)
    compare(hlon.degrees, 151.3229, 0.001)

def test_callisto():
    k = Kernel(open('jup310.bsp'))
    a = k.earth.observe(k.callisto).geometry_at(tdb=2471184.5)
    compare(a.position.AU,
      [-4.884815926454119E+00, -3.705745549073268E+00, -1.493487818022234E+00],
      0.0001 * meter)
