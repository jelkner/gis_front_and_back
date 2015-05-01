#!/usr/bin/env python3
"""Compute bounding boxes for Arlington, Virginia voter precincts.

This script uses the osgeo module to compute the bounding boxes of the 52
polygons desribing the boundaries of the voter precincts in Arlington County,
Virginia.

Requires `Voter_Precinct <http://gisdata.arlgis.opendata.arcgis.com/datasets/1ec04543da0546d38b63d8fd8e1019d5_17>`_ data set.
"""
from osgeo import ogr


class Precinct:
    def __init__(self, num, name):
        self.num = num
        self.name = name

    def __str__(self):
        return 'Precinct {0}: {1}'.format(self.num, self.name)


shapefile = ogr.Open('data/Voter_Precinct.shp')
layer = shapefile.GetLayer(0)

precincts = []

for i in range(layer.GetFeatureCount()):
    feature = layer.GetFeature(i)
    num = feature.GetField('PRECINCT')
    name = feature.GetField('PREC_NAME')

    precinct = Precinct(num, name)

    geometry = feature.GetGeometryRef()
    min_long, max_long, min_lat, max_lat = geometry.GetEnvelope()
    precinct.min_long = min_long
    precinct.max_long = max_long
    precinct.min_lat = min_lat
    precinct.max_lat = max_lat

    precincts.append(precinct)


def by_num_key(precinct):
    return precinct.num

fstr = '\n  lat={0}..{1}\n  long={2}..{3}\n\n'

precincts_by_number = sorted(precincts, key=by_num_key)

for p in precincts_by_number:
    print(p, fstr.format(p.min_lat, p.max_lat, p.min_long, p.max_long))
