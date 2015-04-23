#!/usr/bin/env python2
import mapnik

SHAPE_FILE = 'data/Voter_Precinct.shp'

symbolizer = mapnik.PolygonSymbolizer(mapnik.Color("#FFEEEE"))

rule = mapnik.Rule()
rule.symbols.append(symbolizer)

style = mapnik.Style()
style.rules.append(rule)

symbolizer = mapnik.LineSymbolizer()
symbolizer.stroke = mapnik.Stroke(mapnik.Color("#000000"), 1)
rule.symbols.append(symbolizer)
style.rules.append(rule)

layer = mapnik.Layer("map_layer")
layer.datasource = mapnik.Shapefile(file=SHAPE_FILE)
layer.styles.append("map_style")

map1 = mapnik.Map(1024, 1024)
map1.background = mapnik.Color("#EEFFEE")
map1.append_style("map_style", style)
map1.layers.append(layer)

map1.zoom_all()
mapnik.render_to_file(map1, "arl_voter_precinct_map.png", "png")
