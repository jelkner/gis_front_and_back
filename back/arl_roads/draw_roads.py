#!/usr/bin/env python
import mapnik


precinct_style = mapnik.Style()
roads_style = mapnik.Style()

for roads in range(1, 884):
    the_filter = '[OBJECTID] = {0}'.format(roads)

    rule = mapnik.Rule()
    rule.filter = mapnik.Filter(the_filter)
    symbolizer = mapnik.PolygonSymbolizer(mapnik.Color('#FF7700'))
    rule.symbols.append(symbolizer)
    roads_style.rules.append(rule)

    symbolizer = mapnik.LineSymbolizer()
    symbolizer.stroke = mapnik.Stroke(mapnik.Color('#FF7700'), 1)
    rule.symbols.append(symbolizer)
    roads_style.rules.append(rule)

layer = mapnik.Layer("Roads Layer")
layer.datasource = mapnik.Shapefile(file="data/Roads.shp")
layer.styles.append("Roads Style")

map1 = mapnik.Map(1024, 1024)
map1.background = mapnik.Color("#EEEEEE")
map1.append_style("Roads Style", roads_style)
map1.layers.append(layer)

map1.zoom_all()
mapnik.render_to_file(map1, "arl_roads.png", "png")
