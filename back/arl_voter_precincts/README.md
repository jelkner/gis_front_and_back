# Scripts Using Python to Read Shapefiles and Draw a Map

## Required Packages on Ubuntu 14.04:

* python3-gdal
* python-mapnik

## Data Source

* [Arlington County Voter Precinct](http://gisdata.arlgis.opendata.arcgis.com/datasets/1ec04543da0546d38b63d8fd8e1019d5_17)

Unzip the data files into a `data` directory in the same location as the
scripts.

## Scripts

<dl>
  <dt>analyze_voter_precinct_shapefile.py</dt>
  <dd>
  Reads and prints out details from the `Voter_Precinct.shp` shapefile.
  This is written in Python 3 and requires the `python3-gdal` debian package on
  Ubuntu.
  </dd>

  <dt>make_precinct_map.py</dt>
  <dd>
  Creates a map of the voter precincts in Arlington County, Virginia from the
  `Voter_Precinct.shp`. Written in Python 2 and requires the `python-mapnik`
  debian package on Ubuntu.
   </dd>
</dl>
