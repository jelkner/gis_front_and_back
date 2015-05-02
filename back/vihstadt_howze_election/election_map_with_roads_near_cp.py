#!/usr/bin/env python
import mapnik
import precinct_winners

RED = "#FF0000"
GREEN = "#00FF00"
ORANGE = "#FF7700"
GRAY = "#EEEEEE"
VIHSTADT = precinct_winners.CANDIDATE1
HOWZE = precinct_winners.CANDIDATE2

winners = precinct_winners.share_results()

precinct_style = mapnik.Style()
roads_style = mapnik.Style()

for precinct in range(1, 53):
    the_filter = '[PRECINCT] = {0}'.format(precinct)
    color = GREEN if winners[precinct] == HOWZE else RED

    rule = mapnik.Rule()
    rule.filter = mapnik.Filter(the_filter)
    symbolizer = mapnik.PolygonSymbolizer(mapnik.Color(color))
    rule.symbols.append(symbolizer)
    precinct_style.rules.append(rule)

    symbolizer = mapnik.LineSymbolizer()
    symbolizer.stroke = mapnik.Stroke(mapnik.Color("#000000"), 1)
    rule.symbols.append(symbolizer)
    precinct_style.rules.append(rule)

layer1 = mapnik.Layer("Precinct Layer")
layer1.datasource = mapnik.Shapefile(file="data/Voter_Precinct.shp")
layer1.styles.append("Map Style")

columbia_pike_area = [201, 323, 324, 325, 326, 327, 331, 332, 334]
columbia_pike_area += [335, 338, 376, 457, 466, 467]

for roads in columbia_pike_area:
    the_filter = '[OBJECTID] = {0}'.format(roads)

    rule = mapnik.Rule()
    rule.filter = mapnik.Filter(the_filter)
    symbolizer = mapnik.PolygonSymbolizer(mapnik.Color(ORANGE))
    rule.symbols.append(symbolizer)
    roads_style.rules.append(rule)

    symbolizer = mapnik.LineSymbolizer()
    symbolizer.stroke = mapnik.Stroke(mapnik.Color(ORANGE), 1)
    rule.symbols.append(symbolizer)
    roads_style.rules.append(rule)

layer2 = mapnik.Layer("CP Roads Layer")
layer2.datasource = mapnik.Shapefile(file="data/Roads.shp")
layer2.styles.append("Roads Style")

map1 = mapnik.Map(1024, 1024)
map1.background = mapnik.Color(GRAY)
map1.append_style("Map Style", precinct_style)
map1.layers.append(layer1)
map1.append_style("Roads Style", roads_style)
map1.layers.append(layer2)

map1.zoom_all()
mapnik.render_to_file(map1, "vihstadt_howze_with_roads_near_cp.png", "png")
