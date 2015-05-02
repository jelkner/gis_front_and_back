#!/usr/bin/env python3
"""Use pyshp to explore Arlington County, Virginia roads data"""
import shapefile

sf = shapefile.Reader('data/Roads')
sr = sf.shapeRecords()

print("sf = shapefile.Reader('data/Roads'), sr = sf.shapeRecords()")
print('type(sr): {0}'.format(type(sr)))

print('len(sr): {0}'.format(len(sr)))

print('type(sr[0]): {0}'.format(type(sr[0])))

print("Names that don't start with '__' in sr[0]:")
print([name for name in dir(sr[0]) if not name.startswith('__')])

print('type(sr[0].record): {0}'.format(type(sr[0].record)))
print('type(sr[0].shape): {0}'.format(type(sr[0].shape)))

print('sr[0].record): {0}'.format(sr[0].record))

print("Names that don't start with '__' in sr[0].shape:")
print([name for name in dir(sr[0].shape) if not name.startswith('__')])

print('sf.fields: {0}'.format(sf.fields))
