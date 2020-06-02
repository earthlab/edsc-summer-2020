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
# ## Introduction to Python

# <div class="notice--warning" markdown="1">
#
# ## <i class="fa fa-pencil-square-o" aria-hidden="true"></i> Practice Your Python Skills
#
# Data on average monthly precipitation for <a href="https://www.esrl.noaa.gov/psd/boulder/Boulder.mm.precip.html" target="_blank">Boulder, Colorado provided by the U.S. National Oceanic and Atmospheric Administration (NOAA).</a> 
#
# Month  | Precipitation (inches) |
# --- | --- |
# Jan | 0.70 |
# Feb | 0.75 |
# Mar | 1.85 |
# Apr | 2.93 |
# May | 3.05 |
# June | 2.02 |
# July | 1.93 |
# Aug | 1.62 |
# Sept | 1.84 |
# Oct | 1.31 |
# Nov | 1.39 |
# Dec | 0.84 |
#
# Test your `Python` skills to:
#
# 1. Create variables for monthly average precipitation values (inches) for Boulder, CO for January through December (i.e. one variable for `jan`, one for `feb`, etc through `dec`).
#
# 2. Use the appropriate arithmetic operator to convert the monthly variables for `jan` through `dec` from inches to millimeters (1 inch = 25.4 mm).
#
# 3. Create a list called `precip` that contains the converted monthly average precipitation values in millimeters. (After step 2, you should have monthly variables with converted values. Consider how you can create a list using these variables, rather than typing out the values.)
#
# 4. Create a list called  `months` that contains the abbreviated month names from the table above. 
#
# </div>

# +
# Create monthly precipitation variables


# Convert monthly precipitation variables from inches to mm


# Create lists: one list of month names and one of precip (mm)

# -

# <div class="notice--warning" markdown="1">
#
# ## <i class="fa fa-pencil-square-o" aria-hidden="true"></i> Challenge Your Python Skills
#
# Modify the following code to create a plot of your data:
#
# ```python
# # Import necessary plot package
# import matplotlib.pyplot as plt
#
# # Plot monthly precipitation values
# fig, ax = plt.subplots(figsize=(6, 6))
# ax.bar(listname_x_axis, 
#        listname_y_axis, 
#        color="red")
# ax.set(title="Add plot title here",
#        xlabel="Add x axis label here", 
#        ylabel="Add y axis label here");
# ```
#
# Customize this plot by completing the following tasks:
# 1. Replace `listname_x_axis` and `listname_y_axis` with the names of the lists that you created (`months` and `precip`).
# 2. Change the <a href="https://matplotlib.org/mpl_examples/color/named_colors.hires.png" target="_blank">color of the plot</a> to a blue color such as aqua.
# 3. Update the text for the titles and axes labels. 
# 4. Modify the values in `figsize=(6, 6)` to change the size of your plot. 
#
# For your titles and labels, be sure to think about the following pieces of information that could help someone easily interpret the plot:
#
# * geographic coverage or extent of data.
# * duration or temporal extent of the data.
# * what was actually measured and/or represented by the data.
# * units of measurement.
#
# </div>

# + caption="This plot displays monthly average precipitation values in millimeters for Boulder, CO." label="fig:bar_boulder_monthly_avg_precip"
# Copy/paste the code from the cell above to this cell
# Modify values as instructed

# -

# The cell below includes a set of tests to see if you correctly completed the activity in the cell above. They will provide you with feedback that can help you complete the activity. 
#
# Be sure to run the cell below to check your code (please do not modify the cell!).

# +
# This code is here to check your plot
# Please put the code for your plot in the previous cell
import matplotcheck.base as mpc
import notebook_tests_fundamentals

try:
    print(notebook_tests_fundamentals.exercise_test_months_list(months))
except NameError:
    print("""Could not find a list named 'months', please ensure that your list containing
the month names has been assigned to the variable name 'months'.""")

try:
    print(notebook_tests_fundamentals.exercise_test_precip_list(precip))
except NameError:
    print("""Could not find a list named 'precip', please ensure that your list containing
the converted month precip values has been assigned to the variable name 'precip'.""")

try:
    print(notebook_tests_fundamentals.exercise_test_plot(ax))
except NameError:
    print("Could not find variable 'ax', please make sure you copy and pasted the code correctly into the cell above.")
