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
# <img style="float: left;" src="earth-lab-logo-rgb.png" width="150" height="150">
#
# # Earth Data Science Corps Summer 2020
#
# ![Colored Bar](colored-bar.png)
#
# ## Python Fundamentals -- Exercises 
#
# Now that you have learned the basics of using **Python** it's time to test your skills. Complete the activities below. Feel free to work with a colleague or friend!
#

# %% [markdown]
# <div class="notice--warning" markdown="1">
#
# ## <i class="fa fa-pencil-square-o" aria-hidden="true"></i> Challenge: Lists and Variables  
#
# The data below represent average monthly precipitation for <a href="https://www.esrl.noaa.gov/psd/boulder/Boulder.mm.precip.html" target="_blank">Boulder, Colorado provided by the U.S. National Oceanic and Atmospheric Administration (NOAA).</a> 
#
# Month  | Precipitation (inches) |
# --- | --- |
# jan | 0.70 |
# feb | 0.75 |
# mar | 1.85 |
# apr | 2.93 |
# may | 3.05 |
# june | 2.02 |
# july | 1.93 |
# aug | 1.62 |
# sept | 1.84 |
# oct | 1.31 |
# nov | 1.39 |
# dec | 0.84 |
#
# Create two **python** `lists` as follows:
# 1. the first list should contain the months and should be called `boulder_precip_months`
# 2. the second list should be a list of precipitation values and should be called `boulder_precip_inches`
#
# Both lists should contain the data in the table above in the order they are in - in the table above!
#
# To make this easier, here are all of the data formatted to make it easier to create your list! 
#
# `0.70, 0.75,  1.85 , 2.93, 3.05 , 2.02, 1.93, 1.62, 1.84, 1.31, 1.39, 0.84`
#
# And here are the months:
#
# `jan , feb, mar, apr, may, june, july, aug, sept, oct, nov, dec`
#
#
# **HINT: that the month values should be strings and the precipitation values should be floating point numbers!**
#
# </div>

# %%
# Create your lists in this cell!


# %%
# TODO: add tests here that each item is in fact a list and that the one contains strings and the other contains floats

# %% [markdown]
# ### Convert Precipitation Data From Inches to mm Within the List 
#
# Next, convert each floating point value in the `boulder_precip_inches` to mm creating a new list variable called `boulder_precip_mm`. One way to do this is to create a copy of the old list and assign it to a new variable name - like this:
#
# `new_list = old_list.copy()`
#
# HINT: There are several efficient ways of converting your data to mm including list comprehensions. But for this exercise, you can make a copy of the `boulder_precip_inches` object using
#
# `boulder_precip_inches.copy()` 
#
# Reassign that copy to the new variable called `boulder_precip_mm`.
#
# Finally, you can replace each value in your new list using indexing. Refer back to the lesson on lists if you don't remember how to replace a value in a list. 

# %%
# Add code here that creates a new list by copying the old list to create a new variable


# Convert each item in your new boulder_precip_mm list to mm



# %% [markdown]
# ### Create a List of Lists
#
# You can make a list of lists (a list which contains multiple sublists) using the following syntax:
#
# `list_of_lists = [list_one, list_two]'`
#
# In the cell below create a list called `all_boulder_data` thaht contains the 
# `boulder_precip_months` and `boulder_precip_mm` objects as sublists

# %%
# Turn your two new lists in a single list with two sublists called all_boulder_data.


# %% [markdown]
#
# ## THIS IS THE ORIGINAL ACTIVITY -- we can potentially delete it
# Test your `Python` skills to:
#
# 1. Create variables for monthly average precipitation values (inches) for Boulder, CO for January through December (i.e. one variable for `jan`, one for `feb`, etc through `dec`).
#
# 2. Use the appropriate arithmetic operator to convert the monthly variables for `jan` through `dec` from inches to millimeters (1 inch = 25.4 mm).
#
# 3. Create a list called `precip` that contains the converted monthly average precipitation values in millimeters. (After step 2, you should have monthly variables with converted values. Consider how you can create a list using these variables, rather than typing out the values.)
#
# 4. Create a list called  `months` that contains the abbreviated month names from the table above. 

# %%
# Create monthly precipitation variables


# Convert monthly precipitation variables from inches to mm


# Create lists: one list of month names and one of precip (mm)


# %% [markdown]
# <div class="notice--warning" markdown="1">
#
# ## <i class="fa fa-pencil-square-o" aria-hidden="true"></i> Challenge Your Python Skills
#
# Modify the following code to create a plot of your data. Be sure to use the 
# `all_boulder_data` object for your plot:
#
# HINT: you will need to properly index the all_boulder_data object to access each 
# sublist within it. 
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
#        ylabel="Add y axis label here")
# plt.show()
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

# %% caption="This plot displays monthly average precipitation values in millimeters for Boulder, CO." label="fig:bar_boulder_monthly_avg_precip"
# Copy/paste the code from the cell above to this cell
# Modify values as instructed


# %% [markdown]
# The cell below includes a set of tests to see if you correctly completed the activity in the cell above. They will provide you with feedback that can help you complete the activity. 
#
# Be sure to run the cell below to check your code (please do not modify the cell!).

# %%
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

# %% [markdown]
# <div class="notice--warning" markdown="1">
#
# ## <i class="fa fa-pencil-square-o" aria-hidden="true"></i> BONUS Challenge: List Comprehensions
#
# Above you performed many tasks manually. Included in those manual steps was one 
# where you converted each individual value in your list from inches to mm.
# In Python, list comprehensions are a great way to perform operations on a sequence 
# of values stored within a list. The syntax for a list comprehension is below. 
# Essentially what is happening below, is that Python is iterating through each value
# in the old list (`for i in my_old_list`) and multiplying it by 2 (`i*2`). In each 
# loop, the value `i` represents the next value in the list. IN the example below i will 
# first be the value 1, and then 2 and finally 3 given the list values are: `[1, 2, 3]`
#
#
# ```python
# my_old_list = [1, 2, 3]
# my_new_list = [i *2 for i in my_old_list] 
# my_new_list
# ```
#
# Try to experiment with writing more efficient code. Convert your 
# `boulder_precip_inches` list of values to a new list called 
# `boulder_precip_mm` using a list comprehension using the syntax above! 
# </div>

# %%
# Perform your conversion here


# %%

# %%
