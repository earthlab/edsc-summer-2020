# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.4.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# <img style="float: left;" src="earth-lab-logo-rgb.png" width="150" height="150">
#
# # Earth Data Science Corps Summer 2020
#
# ![Colored Bar](colored-bar.png)
#
# ## Introduction to Vector Data

# <div class='notice--success' markdown="1">
#
# ## <i class="fa fa-ship" aria-hidden="true"></i> Fundamentals of Vector Data in Python 
#
# In this lesson, you will learn fundamental concepts related to working with vector data in **Python**, including understanding the spatial attributes of vector data, how to open vector data and access its metadata.
#
#
# ## <i class="fa fa-graduation-cap" aria-hidden="true"></i> Learning Objectives
#
# After completing this lesson, you will be able to:
#
# * Describe the characteristics of 3 key vector data structures: points, lines and polygons.
# * Open a shapefile in **Python** using **geopandas** - `gpd.read_file()`.
# * View the CRS and other spatial metadata of a vector spatial layer in **Python**
# * Access and view the attributes of a vector spatial layer in **Python**.
#
#
# ## About Vector Data
#
# Vector data are composed of discrete geometric locations (x, y values) known as **vertices** that define the "shape" of the spatial object. The organization of the vertices determines the type of vector that you are working 
# with. There are three types of vector data: 
#
# * **Points:** Each individual point is defined by a single x, y coordinate. There can be many points in a vector point file. Examples of point data include: sampling locations, the location of individual trees or the location of plots.
#
# * **Lines:** Lines are composed of many (at least 2) vertices, or points, that are connected. For instance, a road or a stream may be represented by a line. This line is composed of a series of segments, each "bend" in the road or stream represents a vertex that has defined `x, y` location.
#
# * **Polygons:** A polygon consists of 3 or more vertices that are connected and "closed". Thus the outlines of plot boundaries, lakes, oceans, and states or countries are often represented by polygons. Occasionally, a polygon can have a hole in the middle of it (like a doughnut), this is something to be aware of but not an issue you will deal with in this tutorial.
#
#
# <figure>
#     <a href="https://www.earthdatascience.org/images/earth-analytics/spatial-data/points-lines-polygons-vector-data-types.png">
#     <img src="https://www.earthdatascience.org/images/earth-analytics/spatial-data/points-lines-polygons-vector-data-types.png" alt="There are 3 types of vector objects: points, lines or polygons. Each object type has a different structure. Image Source: Colin Williams (NEON)."></a>
#     <figcaption> There are 3 types of vector objects: points, lines or polygons. Each object type has a different structure. Image Source: Colin Williams (NEON)
#     </figcaption>
# </figure>
#
#
# <i class="fa fa-star"></i> **Data Tip:** Sometimes, boundary layers such as states and countries, are stored as lines rather than polygons. However, these boundaries, when represented as a line, will not create a closed object with a defined "area" that can be "filled".
# {: .notice--warning }
#
#
# ## Shapefiles: Points, Lines, and Polygons
#
# Geospatial data in vector format are often stored in a `shapefile` format. Because the structure of points, lines, and polygons are different, each individual shapefile can only contain one vector type (all points, all lines 
# or all polygons). You will not find a mixture of point, line and polygon objects in a single shapefile.
#
# Objects stored in a shapefile often have a set of associated `attributes` that describe the data. For example, a line shapefile that contains the locations of streams, might contain the associated stream name, stream "order" and other 
# information about each stream line object.
#
# * More about shapefiles can found on <a href="https://en.wikipedia.org/wiki/Shapefile" target="_blank">Wikipedia</a>.
#
#
# ## One Dataset - Many Files
#
# A text file is often self contained. For example, one `.csv` file is composed of one unique file. Many spatial formats are composed of several files. A shapefile is created by 3 or more files, all of which must retain the same NAME and be
# stored in the same file directory, in order for you to be able to work with them.
#
# ### Shapefile Structure
#
# There are 3 key files associated with any and all shapefiles:
#
# * **`.shp`:** the file that contains the geometry for all features.
# * **`.shx`:** the file that indexes the geometry.
# * **`.dbf`:** the file that stores feature attributes in a tabular format.
#
# These files need to have the **same name** and to be stored in the same directory (folder) to open properly in a GIS, `R` or **Python** tool.
#
# Sometimes, a shapefile will have other associated files including:
#
# * `.prj`: the file that contains information on projection format including
# the coordinate system and projection information. It is a plain text file
# describing the projection using well-known text (WKT) format.
# * `.sbn` and `.sbx`: the files that are a spatial index of the features.
# * `.shp.xml`: the file that is the geospatial metadata in XML format, (e.g. ISO 19115 or XML format).
#
# ## Data Management - Sharing Shapefiles
#
# When you work with a shapefile, you must keep all of the key associated file types together. And when you share a shapefile with a colleague, it is important to zip up all of these files into one package before you send it to
# them!
#
# ## Import Shapefiles
#
# You will use the **geopandas** library to work with vector data in **Python**. You will also use `matplotlib.pyplot` to plot your data. 

# +
# Import packages
import os
import matplotlib.pyplot as plt
import geopandas as gpd
import earthpy as et

# Get data and set working directory
data = et.data.get_data('spatial-vector-lidar')
os.chdir(os.path.join(et.io.HOME, 'earth-analytics'))
# -

# The shapefiles that you will import are:
#
# * A polygon shapefile representing our field site boundary,
# * A line shapefile representing roads, and
# * A point shapefile representing the location of field sites at the <a href="http://www.neonscience.org/science-design/field-sites/harvard-forest" target="_blank"> San Joachin field site</a>.
#
# The first shapefile that you will open contains the point locations of plots where trees have been measured. To import shapefiles you use the `geopandas` function `read_file()`. Notice that you call the `read_file()` function using `gpd.read_file()` to tell python to look for the function within the `geopandas` library.
#

# +
# Define path to file
plot_centroid_path = os.path.join("data", "spatial-vector-lidar",
                                  "california", "neon-sjer-site",
                                  "vector_data", "SJER_plot_centroids.shp")

# Import shapefile using geopandas
sjer_plot_locations = gpd.read_file(plot_centroid_path)
# -

#
# ## Spatial Data Attributes
#
# Each object in a shapefile has one or more attributes associated with it.
# Shapefile attributes are similar to fields or columns in a spreadsheet. Each row
# in the spreadsheet has a set of columns associated with it that describe the row
# element. In the case of a shapefile, each row represents a spatial object - for
# example, a road, represented as a line in a line shapefile, will have one "row"
# of attributes associated with it. These attributes can include different types
# of information that describe objects stored within a shapefile. Thus, our road,
# may have a name, length, number of lanes, speed limit, type of road and other
# attributes stored with it.
#
#
# <figure>
#     <a href="https://www.earthdatascience.org/images/earth-analytics/spatial-data/spatial-attribute-tables.png">
#     <img src="https://www.earthdatascience.org/images/earth-analytics/spatial-data/spatial-attribute-tables.png" alt="A shapefile has an associated attribute table. Each spatial feature in a spatial object has the same set of
#     associated attributes that describe or characterize the feature.
#     Attribute data are stored in a separate .dbf file. Attribute data can be
#     compared to a spreadsheet. Each row in a spreadsheet represents one feature
#     in the spatial object. Image Source: National Ecological Observatory Network (NEON)"></a>
#     <figcaption>Each spatial feature in a spatial object has the same set of
#     associated attributes that describe or characterize the feature.
#     Attribute data are stored in a separate *.dbf file. Attribute data can be
#     compared to a spreadsheet. Each row in a spreadsheet represents one feature
#     in the spatial object.
#     Image Source: National Ecological Observatory Network (NEON)
#     </figcaption>
# </figure>
#
#
# You can view the attribute table associated with our geopandas `GeoDataFrame` by simply typing the object name into the console (e.g., `sjer_plot_locations`). 
#
# Or you can use the `.head(3)` function to only display the first 3 rows of the attribute table. The number in the `.head()` function represents the total number of rows that will be returned by the function. 

# View top 6 rows of attribute table
sjer_plot_locations.head(6)

# View the geometry type of each row
sjer_plot_locations.geom_type

# <div class="notice--warning" markdown="1">
#
# ## <i class="fa fa-pencil-square-o" aria-hidden="true"></i> Challenge : Open Spatial Data in Python
#
# Much like was done above, you're going to open your own spatial data with `geopandas`! Below we've provided a path to a dataset that contains spatial data similar to what we opened above. Open the spatial data with `geopandas`. Name the dataset `soap_plot_locations`. Once the dataset is opened, check the `geom_type`, and view the first few rows of the dataset using `dataset.head()`.
#
# </div>

# +
student_plot_centroid_path = os.path.join("data", "spatial-vector-lidar",
                                          "california", "neon-soap-site",
                                          "vector_data", "SOAP_centroids.shp")

# Open your dataset below this line. Make sure to view the geom_type and the first few rows of the dataset

soap_plot_locations = gpd.read_file(student_plot_centroid_path)
# -

# The cell below includes a set of tests to see if you correctly completed the activity in the cell above. They will provide you with feedback that can help you complete the activity. 
#
# Be sure to run the cell below to check your code (please do not modify the cell!).

# +
# Run this cell to ensure soap_plot_locations was created correctly

import notebook_tests_data_types

try:
    print(notebook_tests_data_types.test_geopandas_dataframe_creation(soap_plot_locations))
except NameError:
        print("'soap_plot_locations' is not defined. Make sure you spelled the variable name correctly!")
# -

# In this case, you have several attributes associated with our points including:
#
# * Plot_ID, Point, easting, geometry, northing, plot_type 
#
# <i class="fa fa-star"></i> **Data Tip:** The acronym, OGR, refers to the OpenGIS Simple Features Reference Implementation. <a href="https://trac.osgeo.org/gdal/wiki/FAQGeneral" target="_blank"> Learn more about OGR.</a>
# {: .notice--warning }
#
#
# ### The Geopandas Data Structure
#
# Notice that the geopandas data structure is a `dataframe` that contains a `geometry` column where the x, y point location values are stored. All of the other shapefile feature attributes are contained in columns, similar to what you may be used to if you've used a GIS tool such as ArcGIS or QGIS.
#
# ## Shapefile Metadata & Attributes
#
# When you import the `SJER_plot_centroids` shapefile layer into `Python` the `gpd.read_file()` function automatically stores information about the data as attributes. You are particularly interested in the geospatial **metadata**, describing the format, `CRS`, `extent`, and other components of the vector data, and the **attributes** which describe properties associated with each individual vector object.
#
#
# ## Spatial Metadata
#
# Key metadata for all shapefiles include:
#
# 1. **Object Type:** the class of the imported object.
# 2. **Coordinate Reference System (CRS):** the projection of the data.
# 3. **Extent:** the spatial extent (geographic area that the shapefile covers) of the shapefile. Note that the spatial extent for a shapefile represents the extent for ALL spatial objects in the shapefile.
#
# You can view these shapefile metadata using the `.crs` and `.total_bounds` attributes:

# View object type
type(sjer_plot_locations)

# View CRS of object
sjer_plot_locations.crs

# The CRS for the data is epsg code: `32611`. You will learn about CRS formats and structures in a later lesson but for now a quick google search reveals that this CRS is: <a href="http://spatialreference.org/ref/epsg/wgs-84-utm-zone-11n/" target="_blank">UTM zone 11 North - WGS84</a>.

# View the spatial extent
sjer_plot_locations.total_bounds

# <figure>
#     <a href="https://www.earthdatascience.org/images/earth-analytics/spatial-data/spatial-extent.png">
#     <img src="https://www.earthdatascience.org/images/earth-analytics/spatial-data/spatial-extent.png" alt="The spatial extent of a shapefile or geopandas GeoDataFrame represents the geographic edge or location that is the furthest north, south east and west. Thus is represents the overall geographic coverage of the spatial object. Image Source: National Ecological Observatory Network (NEON)."></a>
#     <figcaption>The spatial extent of a shapefile or geopandas GeoDataFrame represents
#     the geographic "edge" or location that is the furthest north, south east and
#     west. Thus is represents the overall geographic coverage of the spatial object.
#     Image Source: National Ecological Observatory Network (NEON)
#     </figcaption>
# </figure>

# ## How Many Features Are In Your Shapefile? 
#
# You can view the number of features (counted by the number of rows in the attribute table) and feature attributes (number of columns) in our data using the pandas `.shape` method. Note that the data are returned as a vector of two values:
#
# (rows, columns) 
#
# Also note that the number of columns includes a column where the geometry (the x, y coordinate locations) are stored. 

sjer_plot_locations.shape

# <div class="notice--warning" markdown="1">
#
# ## <i class="fa fa-pencil-square-o" aria-hidden="true"></i> Challenge : Get Metadata from GeoPandas
#
# Now you can get the same metadata, but for your `soap_plot_locations`. Assign the `crs` of your data to `soap_crs`, assign the bounds of your data to `soap_bounds`, and assign the shape of your data to `soap_shape`. You can `print()` those variables out to see how they differ from the metadata of the other dataset, and how they are similar as well! 
#
# </div>

# +
# Open your dataset below this line. Make sure to view the geom_type and the first few rows of the dataset

soap_crs = soap_plot_locations.crs

soap_bounds = soap_plot_locations.total_bounds

soap_shape = soap_plot_locations.shape

# -

# The cell below includes a set of tests to see if you correctly completed the activity in the cell above. They will provide you with feedback that can help you complete the activity. 
#
# Be sure to run the cell below to check your code (please do not modify the cell!).

# +
# Run this cell to ensure soap_crs, soap_bounds, and soap_shape were created correctly

try:
    print(notebook_tests_data_types.test_geopandas_dataframe_crs(soap_crs))
except NameError as e:
        print(e, "'soap_crs' is not defined. Make sure you spelled the variable name correctly!")
        
try:
    print(notebook_tests_data_types.test_geopandas_dataframe_bounds(soap_bounds))
except NameError:
        print("'soap_bounds' is not defined. Make sure you spelled the variable name correctly!")
        
try:
    print(notebook_tests_data_types.test_geopandas_dataframe_shape(soap_shape))
except NameError:
        print("'soap_shape' is not defined. Make sure you spelled the variable name correctly!")
