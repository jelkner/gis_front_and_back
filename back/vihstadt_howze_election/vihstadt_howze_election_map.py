#!/usr/bin/env python
import mapnik
import precinct_winners

RED = "#FF0000"
GREEN = "#00FF00"
VIHSTADT = precinct_winners.CANDIDATE1
HOWZE = precinct_winners.CANDIDATE2

winners = precinct_winners.share_results()

style = mapnik.Style()

for precinct in range(1, 53):
    the_filter = '[PRECINCT] = {0}'.format(precinct)
    color = GREEN if winners[precinct] == HOWZE else RED

    rule = mapnik.Rule()
    rule.filter = mapnik.Filter(the_filter)
    symbolizer = mapnik.PolygonSymbolizer(mapnik.Color(color))
    rule.symbols.append(symbolizer)
    style.rules.append(rule)

    symbolizer = mapnik.LineSymbolizer()
    symbolizer.stroke = mapnik.Stroke(mapnik.Color("#000000"), 1)
    rule.symbols.append(symbolizer)
    style.rules.append(rule)


layer = mapnik.Layer("mapLayer")
layer.datasource = mapnik.Shapefile(file="data/Voter_Precinct.shp")
layer.styles.append("mapStyle")

map1 = mapnik.Map(1024, 1024)
map1.background = mapnik.Color("#EEEEEE")
map1.append_style("mapStyle", style)
map1.layers.append(layer)

map1.zoom_all()
mapnik.render_to_file(map1, "vihstadt_howze_nov_2014.png", "png")
