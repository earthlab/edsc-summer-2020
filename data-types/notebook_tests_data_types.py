import geopandas as gpd
from pyproj import crs
import numpy as np

# TESTS FOR THE VECTOR NOTEBOOK
def test_geopandas_dataframe_creation(soap_plot_locations):
    """Testing that the goepandas dataframe variable was correctly assigned."""
    return_message = ""

    if isinstance(soap_plot_locations, gpd.geodataframe.GeoDataFrame):
        return_message += """
Variable 'soap_plot_locations' is a GeoDataFrame, good job!\n"""
        if len(soap_plot_locations) == 50:
            return_message += """
'soap_plot_locations' has the correct amount of data, good job!"""
        else:
            return_message += """Variable 'soap_plot_locations' exists and is
a GeoDataFrame, but has the wrong values in it. Make sure you opened the correct
file with GeoPandas (with the path that was provided)."""
    else:
        return_message += """Variable 'soap_plot_locations' exists, but is not
a GeoDataFrame. Make sure you opened up 'soap_plot_locations' with GeoPandas."""

    return return_message


def test_geopandas_dataframe_crs(soap_crs):
    """Testing that the goepandas dataframe crs variable was correctly
    assigned."""

    return_message = ""

    if isinstance(soap_crs, crs.CRS):
        return_message += """Variable 'soap_crs' is a CRS object.\n"""
        if soap_crs.name == "WGS 84 / UTM zone 11N":
            return_message += """'soap_crs' has the correct projection data!"""
        else:
            return_message += """Variable 'soap_crs' exists and is
a CRS object, but has the wrong values in it. Make sure you checked the correct
GeoDataFrame"""
    else:
        return_message += """
Variable 'soap_crs' exists, but is not a CRS object."""

    return return_message


def test_geopandas_dataframe_bounds(soap_bounds):
    """Testing that the goepandas dataframe bounds variable was correctly
    assigned."""

    return_message = ""

    correct_array = np.array(
        [296955.1971, 4100083.0279, 300555.1971, 4101493.0279]
    )

    if isinstance(soap_bounds, np.ndarray):
        return_message += """Variable 'soap_bounds' is a numpy array.\n"""
        if np.allclose(soap_bounds, correct_array):
            return_message += """'soap_bounds' has the correct data!"""
        else:
            return_message += """Variable 'soap_bounds' exists and is
a numpy array, but has the wrong values in it. Make sure you checked the correct
GeoDataFrame"""
    else:
        return_message += """
Variable 'soap_bounds' exists, but is not a numpy array."""

    return return_message


def test_geopandas_dataframe_shape(soap_shape):
    """Testing that the goepandas dataframe shape variable was correctly
    assigned."""

    return_message = ""

    correct_shape = (50, 7)

    if isinstance(soap_shape, tuple):
        return_message += """Variable 'soap_shape' is a tuple.\n"""
        if soap_shape == correct_shape:
            return_message += """'soap_shape' has the correct data!"""
        else:
            return_message += """Variable 'soap_shape' exists and is
a tuple, but has the wrong values in it. Make sure you checked the correct
GeoDataFrame"""
    else:
        return_message += """
Variable 'soap_shape' exists, but is not the correct data type."""

    return return_message
