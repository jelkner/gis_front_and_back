# Scripts Using Python to Read Shapefiles and Draw a Map of Roads in Arlington

## Required Packages on Ubuntu 14.04:

* python-pyshp (or python3-pyshp)
* python-mapnik

## Data Sources

* [Arlington County Roads](http://gisdata.arlgis.opendata.arcgis.com/datasets/add6458ac5b241368d459fce8e53cfe9_10)
* [Arlington County Voter Precinct](http://gisdata.arlgis.opendata.arcgis.com/datasets/1ec04543da0546d38b63d8fd8e1019d5_17)

Unzip the data files into a `data` directory in the same location as the
scripts.

## Scripts

<dl>
  <dt>explore_roads_shapefile.py</dt>
  <dd>
  Reads and prints out details from the `Roads.shp` shapefile.
  This is written in Python 2/3 and requires either the `python-pyshp` or
  `python3-pyshp` debian package on Ubuntu.
  </dd>

  <dt>draw_roads.py</dt>
  <dd>
  Creates a map of all the roads in Arlington County, Virginia from the
  `Roads.shp`. Written in Python 2 and requires the `python-mapnik` debian
  package on Ubuntu.
  </dd>

  <dt>a_roads_shape.py</dt>
  <dd>
  Creates a map of of the precincts in Arlington County, Virginia from the
  `Voter_Precincts.shp` and adds a single road shape from `Roads.shp` as a
  second layer. Written in Python 2.
  </dd>

  <dt>roads_near_columbia_pike.py</dt>
  <dd>
  Creates a map of selected roads near Columbia Pike in Arlington County,
  Virginia from the `Roads.shp`. Written in Python 2.
  </dd>
</dl>
