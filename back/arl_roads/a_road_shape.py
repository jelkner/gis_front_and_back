#!/usr/bin/env python
import mapnik


precinct_style = mapnik.Style()
roads_style = mapnik.Style()

for precinct in range(1, 53):
    the_filter = '[PRECINCT] = {0}'.format(precinct)
    color = '#FFFFFF'
    outline_color = '#000000'

    rule = mapnik.Rule()
    rule.filter = mapnik.Filter(the_filter)
    symbolizer = mapnik.PolygonSymbolizer(mapnik.Color(color))
    rule.symbols.append(symbolizer)
    precinct_style.rules.append(rule)

    symbolizer = mapnik.LineSymbolizer()
    symbolizer.stroke = mapnik.Stroke(mapnik.Color(outline_color), 1)
    rule.symbols.append(symbolizer)
    precinct_style.rules.append(rule)

layer1 = mapnik.Layer("Precinct Layer")
layer1.datasource = mapnik.Shapefile(file="data/Voter_Precinct.shp")
layer1.styles.append("Map Style")

# Add another layer with a record from the Roads file
rule = mapnik.Rule()
rule.filter = mapnik.Filter('[OBJECTID] = 324')
symbolizer = mapnik.PolygonSymbolizer(mapnik.Color('#FF7700'))
rule.symbols.append(symbolizer)
roads_style.rules.append(rule)

symbolizer = mapnik.LineSymbolizer()
symbolizer.stroke = mapnik.Stroke(mapnik.Color('#FF7700'), 1)
rule.symbols.append(symbolizer)
roads_style.rules.append(rule)

layer2 = mapnik.Layer("Roads Layer")
layer2.datasource = mapnik.Shapefile(file="data/Roads.shp")
layer2.styles.append("Roads Style")

map1 = mapnik.Map(1024, 1024)
map1.background = mapnik.Color("#EEEEEE")
map1.append_style("Map Style", precinct_style)
map1.layers.append(layer1)
map1.append_style("Roads Style", roads_style)
map1.layers.append(layer2)

map1.zoom_all()
mapnik.render_to_file(map1, "precincts_with_a_road_shape.png", "png")
