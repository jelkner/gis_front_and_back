#!/usr/bin/env python3
import osgeo.ogr

SHAPE_FILE = 'data/Voter_Precinct.shp'


def analyze_geometry(geometry, indent=0):
    s = []
    s.append('    ' * indent)
    s.append(geometry.GetGeometryName())
    if geometry.GetPointCount() > 0:
        s.append(' with {0} data points'.format(geometry.GetPointCount()))
    if geometry.GetGeometryCount() > 0:
        s.append(' containing:')

    print(''.join(s))

    for i in range(geometry.GetGeometryCount()):
        analyze_geometry(geometry.GetGeometryRef(i), indent+1)


shapefile = osgeo.ogr.Open(SHAPE_FILE)
num_layers = shapefile.GetLayerCount()

print('Shapefile contains {0} layers\n'.format(num_layers))

for layer_num in range(num_layers):
    layer = shapefile.GetLayer(layer_num)
    spatial_ref = layer.GetSpatialRef().ExportToProj4()
    num_features = layer.GetFeatureCount()
    print('Layer {0} has spatial reference {1}'.format(layer_num, spatial_ref))
    print()
    print('Layer {0} has {1} features:\n'.format(layer_num, num_features))

    for feature_num in range(num_features):
        feature = layer.GetFeature(feature_num)
        feature_name = feature.GetField('PRECINCT')

        print()
        print('Feature {0} is precinct #{1}'.format(feature_num, feature_name))
        print('This precinct has the following features:')

        attributes = feature.items()

        for key, value in attributes.items():
            print('    {0} = {1}'.format(key, value))

        geometry = feature.GetGeometryRef()
        print("Feature's geometry is a ", end='')
        analyze_geometry(geometry)
