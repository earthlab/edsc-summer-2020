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
# 1. Create new variables for monthly average precipitation values (inches) for Boulder, CO for January through December.
#
# 2. Use the appropriate arithmetic operator to convert the monthly variables for `jan` to `dec` from inches to millimeters (1 inch = 25.4 mm).
#
# 3. Create a list that contains the converted monthly average precipitation values in millimeters. Name it `precip`. Print your list (hint: `print(list_name)`).
#
# 4. Create a list that contains the month names from the table above. Name it `months`.
#
# </div>

# + tags=["hide"]
# Create monthly variables

# Convert to mm

# Assign lists, one list of monthly name variables and one with the converted measurment variables.
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
# fig, ax = plt.subplots(figsize=(10, 10))
# ax.bar(listname_months, listname_precip, color="blue")
# ax.set(title="Add plot title here.",
#        xlabel="Add x axis label here.", ylabel="Add y axis label here.");
# ```
#
# Customize this plot by:
# 1. Replacing `listname_months` and `listname_precip` with the names of the lists that you created (`months` and `precip`)
# 2. Change the <a href="https://matplotlib.org/mpl_examples/color/named_colors.hires.png" target="_blank">color of the plot</a> to aqua.
# 3. Update the text for the titles and axes labels.
# 4. Modifying the values in `figsize=(10, 10)` to change the size of your plot.
#
# For your titles and labels, be sure to think about the following pieces of information that could help someone easily interpret the plot:
#
# * geographic coverage or extent of data.
# * duration or temporal extent of the data.
# * what was actually measured and/or represented by the data.
# * units of measurement.
#
# </div>

# + caption="This plot displays monthly average precipitation values in millimeters for Boulder, CO." label="fig:bar_boulder_monthly_avg_precip" tags=["hide"]
# Copy and paste the code from the cell above here. Modify the values as instructed.
# -

# The cell below includes a set of tests to see if you correctly completed the activity in the cell above. They will provide you with feedback that can help you complete the activity.
#
# Be sure to run the cell below to check your code (please do not modify the cell!).

# +
### DO NOT MODIFY THE CODE BELOW ###
# This code is here to check your plot, please put your code for your plot above these comments
import matplotcheck.base as mpc

correct_month_names = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "June",
    "July",
    "Aug",
    "Sept",
    "Oct",
    "Nov",
    "Dec",
]
correct_month_precip = [
    17.779999999999998,
    19.049999999999997,
    46.99,
    74.422,
    77.46999999999998,
    51.308,
    49.022,
    41.148,
    46.736,
    33.274,
    35.306,
    21.336,
]

try:
    if months == correct_month_names:
        print("List of month names successfully assigned and has correct values!")
    else:
        error_msg = """There is a variable named 'months', but it is assigned these values:\n{}
Please ensure that the values are strings with the month names from the table above."""
        print(error_msg.format(months))
except NameError:
    print(
        "Could not find a list named 'months', please ensure that your list containing\n",
        "the month names has been assigned to the variable name 'months'.",
    )

try:
    if precip == correct_month_precip:
        print(
            "List of month precip values successfully assigned and has correct converted values!"
        )
    else:
        error_msg = """There is a variable named 'precip', but it is assigned these values:\n{}
Please ensure that the values are the values from the table above, 
but converted to be mm instead of inches"""
        print(error_msg.format(precip))
except NameError:
    print(
        "Could not find a list named 'precip', please ensure that your list containing\n",
        "the converted month precip values has been assigned to the variable name 'precip'.",
    )

try:
    plot_test = mpc.PlotTester(ax)
    try:
        plot_test.assert_plot_type(
            "bar",
            "Plot is not a bar type, make sure that the original code you copied wasn't modified to change the plot type!",
        )
        print("Plot is a bar type.")
    except AssertionError as error:
        print(error)

    try:
        needed_titles = [["Boulder"], ["average", "mean"], ["month"], ["precip"]]
        plot_test.assert_title_contains(
            strings_expected=needed_titles,
            message_default="Please make sure that the title contains all needed keywords specified in the instructions",
        )
        print("Plot has all of the needed keywords in the title.")
    except AssertionError as error:
        print(error)

    try:
        needed_xaxis_words = [["precip"], ["mm", "millimeters"]]
        plot_test.assert_axis_label_contains(
            strings_expected=needed_xaxis_words,
            message_default="Please make sure that the x axis contains all needed keywords specified in the instructions",
        )
        print("Plot has all of the needed keywords in the x axis.")
    except AssertionError as error:
        print(error)

    try:
        needed_yaxis_words = ["month"]
        plot_test.assert_axis_label_contains(
            strings_expected=needed_yaxis_words,
            message_default="Please make sure that the y axis contains all needed keywords specified in the instructions",
        )
        print("Plot has all of the needed keywords in the y axis.")
    except AssertionError as error:
        print(error)
except NameError:
    print(
        "Can't find variable 'ax', please make sure you copy and pasted the code correctly into the cell above."
    )
