# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.4.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# <img style="float: left;" src="../earth-lab-logo-rgb.png" width="150" height="150">
#
# # Earth Data Science Corps Summer 2020
#
# ![Colored Bar](../colored-bar.png)

# %% [markdown]
# <div class='notice--success' markdown="1">
#
# ## <i class="fa fa-graduation-cap" aria-hidden="true"></i> Learning Objectives
#
# At the end of this activity, you will be able to:
#
# * Define the structure of tabular data
# * Describe the difference between the two common types of tabular text file formats: `txt` and `csv` files
# * Be able to list some commonly used scientific data types that often are downloaded in a tabular format. 
#
# </div>

# %% [markdown]
# ## What is Tabular Data?
#
# Tabular data are data that are stored in a row / column format. Columns (and 
# sometimes rows) are often identified by headers which if named correctly, explain
# what is in that row or column. You may already be 
# familiar with spreadsheet tools such as Excel and Google Sheets that can be 
# used to open tabular data. 
#
# ## The Structure of a Text of Tabular Data Set 
#
# ### Tabular Data Is Defined by Rows and Columns 
# In the example below, you see a table of values 
# that represent precipitation for 3 days. The headers in the data include 
#
# * `day` and
# * `precipitation-mm`
#
#
# | day   | precipitation-mm    |  
# |:----------|:-------------|
# | monday | 0 | 
# | tuesday | 1   | 
# | wednesday | 5 | 
#
# The tabular data above contains 4 rows - the first of which (row 1) is a header row and subsequent rows contain data. The table also has 2 columns. 
#
#
# ## Common Tabular Data File Types: .csv and .txt
#
# Tabular data can be downloaded in many different file formats. Spreadsheet formats 
# include `.xls` and `xlsx` which can be directly opened in Microsoft 
# Excel. When you are downloading Earth and Environmental data, you will often 
# see tabluar data stored in file formats including: 
#
# * `.csv`: Comma Separate Values -- This file has each column separated (delimited) by a comma. 
# * `.txt`: A basic text file. In a `txt` file often the delimiter (the thing that separates out each column can vary. Delimiters are discussed below in more detail. 
#
# These formats are text based and often can be opened in a text editor like atom or notepad. 
# They can be then imported into `Python` using `Pandas` for further exploration 
# and processing. 
#
# <i class="fa fa-star"></i> **Data Tip:** The challenge with graphical user 
# interface (GUI) based tools like Excel
# is that they often have limitations when it comes to working with larger files. 
# Further, it ecomes difficult to recreate workflows implemented in Excel because
# you are often pressing buttons rather than scripting workflows. You can use 
# Open Source Python to implement any workflow you might implement in Excel 
# and that workflow can become fully sharable and reproducible! 
# {: .notice--success }
#
# ## Text Files & Delimiters
#
# A delimiter refers to the character that defines the boundary for different sets of information. 
# In a text file, the delimiter defines the boundary between columns. A line break (a return) defines 
# each row. 
#
# Below you will find an example of a space delimited text file. In the example below, each column of data 
# is separated by a comma `,`. The data also include a header row which is also separated by commas.
#
# ```
# site_code, year, month, day, hour, minute, second, time_decimal, value, value_std_dev  
# BRW,1973,1,1,0,0,0,1973.0,-999.99,-99.99
# BRW,1973,2,1,0,0,0,1973.0849315068492,-999.99,-99.99 
# BRW,1973,3,1,0,0,0,1973.1616438356164,-999.99,-99.99 
# ```
#
# Here is an example of a space delimited text file. In the example below, each column of data 
# are separated by a single space. 
#
# ```
# site_code year month day hour minute second time_decimal value value_std_dev  
# BRW 1973 1 1 0 0 0 1973.0 -999.99 -99.99
# BRW 1973 2 1 0 0 0 1973.0849315068492 -999.99 -99.99 
# BRW 1973 3 1 0 0 0 1973.1616438356164 -999.99 -99.99 
# ```
#
# There are many different types of delimiters including:
#
# * tabs
# * commas
# * 1 (or more) spaces
#
# Sometimes you will find other characters used as delimiters but the above-listed options are the most common. 
#
# <i class="fa fa-star"></i> **Data Tip:** The `.csv` file format is most often delimited by a comma. Hence the name: Comma Separated value.
# {: .notice--success }
#
#
# There are many different types of data that can come in a text or tabular format.
# These data include
#
#
# ## Earth and Environmental Data That Are Stored In Text File Format
#
# There are many different types of data that are stored in text and tabular file formats.
# Below you will see a few different examples of data that are provided in this format. You
# will also explore some of the cleanup steps that you need to import and begin to work with 
# the data. 
#
# <i class="fa fa-star"></i> **Data Tip:** Not all text files store tabular text (character) based data. The `.asc` file format is a text based format that stores spatial raster data.  
# {: .notice--success }
#
#

# %%
# Import packages
import os
import pandas as pd
import matplotlib.pyplot as plt


# %% [markdown]
# If you have a url that directly links directly to a file online, you can 
# open it directly using pandas `.read_csv()`. Have a look at the data below - 
# and notice that is has:
#
# * 3 columns: months, precip and seasons
# * 12 rows: notice that the first row is numered as `0`. This is because indexing 
# in Python always starts at 0 rather than 1. 
#
# # TODO add link to zero based indexing lesson wherever we talk about it in our textbook -- ask jenny

# %%
# Download and open the .csv file using Pandas
avg_monthly_precip = pd.read_csv(
    "https://ndownloader.figshare.com/files/12710618")

# View the data that you just downloaded and opened
avg_monthly_precip

# %% [markdown]
# You can view some stats about the data frame including the number of columns 
# and rows in the data using `.info()`
#

# %%
avg_monthly_precip.info()

# %% [markdown]
# And finally you can plot the data using `.plot()`

# %%
# Plot the data
f, ax = plt.subplots()
avg_monthly_precip.plot(x="months",
                        y="precip",
                        title="Precipitation (mm) for One Year",
                        ax=ax)
ax.set(xlabel='Month',
       ylabel='Precipitation (mm)')
plt.show()

# %% [markdown]
# <div class="notice--warning" markdown="1">
#
# ## <i class="fa fa-pencil-square-o" aria-hidden="true"></i> ## Challenge
#
# * Use Python to determine the `type` of data stored in `avg_monthly_precip`
#
# HINT: you learned how to do this in the variables lessons last week 
#
#
# </div>
#

# %%
# Check the type of the variable avg_monthly_precip in this cell  


# %% [markdown]
# <div class="notice--warning" markdown="1">
#
# ## <i class="fa fa-pencil-square-o" aria-hidden="true"></i> ## Challenge
#
# In most programming languages, you can customize the options for how a function 
# runs by using parameters. Examples of parameters in the plot above include: 
#
# * `x="months"` - tell python which data to place on the x-axis
# * `y="precip"` - tell python which data to place on the y-axis
#
# Above you created a line plot. You can use the `kind=""` parameter to 
# modify the type of plot that pandas created. You can use the `color=""` 
# parameter to specify a color that you wish to use for each bar in the plot. 
#
# Do the following:
#
# 1. copy the code below into the code cell below this markdown cell.
# 2. Add `kind="bar"` to the `.plot()` method. 
# 3. Specify the color of each bar using the `color=""` parameter. 
#
# Run your cell and see what the final plot looks like. You can select 
# any color that you wish to complete your plot. 
#
# Use this link to find a list of colors (open it in a new browser tab!) https://het.as.utexas.edu/HET/Software/Matplotlib/api/colors_api.html
#
#
# ```python
# f, ax = plt.subplots()
# avg_monthly_precip.plot(x="months",
#                         y="precip",
#                         title="Precipitation (mm) for One Year",
#                         ax=ax)
# ax.set(xlabel='Month',
#        ylabel='Precipitation (mm)')
# plt.show()
# ```
#
# </div>

# %%
# Modify your original plot to be a bar plot 
# Change the color of the bars using color=
f, ax = plt.subplots()
avg_monthly_precip.plot(x="months",
                        y="precip",
                        title="Precipitation (mm) for One Year",
                        ax=ax)
ax.set(xlabel='Month',
       ylabel='Precipitation (mm)')
plt.show()

# %% [markdown]
# ## Cleaning Tabular Text Files So You Can Open Them in Python
#
# ## Missing Data Values & Headers in Text Files
#
# Not all text files are as simple as the example above. Many text files have 
# several lines of header text above the data that provide you with useful information
# about the data itself. This data is referred to as metadata. 
#
# Also often times there are data missing from the data that were collected. 
# These missing values will be identified using a specific value that is hopefully
# documented in the metadata for that file. 
#
# Next you will explore some temperature data that need to be cleaned up. 
#

# %% [markdown]
# Data source: https://www.ncdc.noaa.gov/cag/city/time-series/
#
# Miami, Florida: https://www.ncdc.noaa.gov/cag/city/time-series/USW00012839-tmax-12-12-1895-2020.csv 
# Seattle, Washington: https://www.ncdc.noaa.gov/cag/city/time-series/USW00013895-tmax-1-5-1895-2020.csv 

# %%
# Maybe a city dataset would be better here?
temp_data = "https://www.ncdc.noaa.gov/cag/city/time-series/USW00012839-tmax-12-12-1895-2020.csv" 

miami_temp = pd.read_csv(temp_data)
miami_temp

# %% [markdown]
# Notice that the data above contain a few extra rows of information. This 
# information however is important for you to understand. 
#
# * `Missing: -99` -- this is the value that represents the no data value. Misisng data might occur if a sensor stops working or a measurement isn't recorded. You will want to remove any missing data values
# * `Units: Degrees Fahrenheit` -- it's always important to first understand the units of the data before you try to interpret what the data are showing!  
#
# Below you will use all of the information stored in the header to import your data.
# You will also remove the first few rows of data because they don't actually contain any
# data values. These rows contain metadata. 
#
# ### Function Parameters in Python
#
# A parameter refers to an option that you can specify when running a function 
# in Python. You can adjust the parameters associated with importing your data 
# in the same way that you adjusted the plot type and colors above. 
#
# Below you use: 
#
# * `skiprows=`: to tell python to skip the first 3 rows of your data
# * `na_values=`: to tell python to assign any misisng data values to NA 
#
# NA refers to missing data. when you specify a value as NA (NaN or Not a Number 
# in python) it will not be included in plots or any mathematical operations.
#
# # TODO -- add links to missing data in python here...

# %%
# Open the miami data skipping the first 3 rows and setting no data values
miami_temp = pd.read_csv(temp_data,
                        skiprows=3,
                        na_values=-99)
# View the first 5 rows of the data
miami_temp.head()

# %% [markdown]
# <div class="notice--warning" markdown="1">
#
# ## <i class="fa fa-pencil-square-o" aria-hidden="true"></i> ## Challenge
#
# Now that you have imported temperature data for Miami, plot the 
# data using the code example above!! In your plot code, set `Date` as your 
# `x-axis` value and `Value` column as your `y-axis` value.
#
# </div>

# %%
# Add the code needed to plot the miami_data object below



# %% [markdown]
# <div class="notice--warning" markdown="1">
#
# ## <i class="fa fa-pencil-square-o" aria-hidden="true"></i> ## Challenge
#
# Use the link below to open and plot temperature data for Seattle, Washington. 
#
# https://www.ncdc.noaa.gov/cag/city/time-series/USW00013895-tmax-1-5-1895-2020.csv 
#
# </div>
#

# %%
# Add your code to plot the data below


# %% [markdown]
# https://www.ncdc.noaa.gov/cag/county/time-series/CO-013/tavg/all/1/1895-2020?base_prd=true&begbaseyear=1901&endbaseyear=2000 
#
#
# # TODO -- let's use this for a final activity??-- so leave this for now but it's an even more complex challenge. or it can just be an example of another data type.  
#
# Turn the below into a semi interactive activity. Essentially we can all open it together. 
# And then note that there is some info at the top.
#
# Discussion points that we can talk about as a group
#
# 1. no data
# 2. additional rows at the top that we may not way
# 3. units are in there too
#
# Activity can be to 1) open the data - be sure to skip the top rows and assign the no data value
# we can provide them with an example of how to do this
#
# Plot -- Value  on the y and Date on the x
#

# %% [markdown]
# # TODO: this could be an interactive activity at the end.
#
# Let's come back to this as it could go here OR on the final activity page for this chapter?
#
#
# 1. provide the code they need to download the data.
# 2. then tell them to open the data and give them the parameters to open it successfully
# 3. then have them plot the data 
#
#
# Maybe we show them how to download the data and describe each step 
# THen the activity can walk them through handing the bad data and skipping rows and such 
#
# 1. they look at the text file 
# 2. we tell them to plot time_decimal on the x and y = vaue
# 3. we tell them that this particular function takes many different parameters -- 
#
# * delimiter, skip rows (trick -- 0 based indexing needs to be considered
# na_values -- note about missing data 
#
#

# %%
# Download greenhouse gas CO2 data
import urllib.request
greenhouse_gas_url = "ftp://aftp.cmdl.noaa.gov/data/trace_gases/co2/in-situ/surface/brw/co2_brw_surface-insitu_1_ccgg_MonthlyData.txt"
urllib.request.urlretrieve(url=greenhouse_gas_url,
                           filename="co2-emissions-barrow.csv")

greenhouse_gas_data = pd.read_csv("co2-emissions-barrow.csv",
                                  skiprows=148,
                                  delimiter=" ",
                                  na_values="-999.99")


greenhouse_gas_data

# %%
f, ax = plt.subplots(figsize=(12, 6))
greenhouse_gas_data.plot(x="time_decimal",
                         y="value",
                         title="CO2 emissions For Barrow, Alaska",
                         ax=ax)
plt.show()

# %% [markdown]
# # TODO -- leave this here for now but i think it would be a great final activity dataset for the spatial chapter potentially
#
# # this could be a final activity file -- because it includes spatial and tabular -- 
# https://opendata.arcgis.com/datasets/175425c25d8849b58feb89483ef02961_1.csv 
#

# %% [markdown]
# <div class="notice--info" markdown="1">
#
# ## Additional Resources
#
# </div>
#
#
# # TODO -- add links to relevant textbook chapters including
#
# * pandas in the intro textbook
# * time series in the advanced textbook
# * no data values 
