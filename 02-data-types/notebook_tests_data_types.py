import geopandas as gpd
from pyproj import crs
import numpy as np

# TESTS FOR THE VECTOR NOTEBOOK
def test_geopandas_dataframe_creation(populated_places):
    """Testing that the goepandas dataframe variable was correctly assigned."""
    return_message = ""

    if isinstance(populated_places, gpd.geodataframe.GeoDataFrame):
        return_message += """
Variable 'populated_places' is a GeoDataFrame, good job!\n"""
        if len(populated_places) == 1249:
            return_message += """
'populated_places' has the correct amount of data, good job!"""
        else:
            return_message += """Variable 'populated_places' exists and is
a GeoDataFrame, but has the wrong values in it. Make sure you opened the correct
file with GeoPandas (with the path that was provided)."""
    else:
        return_message += """Variable 'populated_places' exists, but is not
a GeoDataFrame. Make sure you opened up 'populated_places' with GeoPandas."""

    return return_message
