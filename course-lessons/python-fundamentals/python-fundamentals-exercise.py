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
# 3. Create a list that contains the converted monthly average precipitation values in millimeters. Print your list (hint: `print(list_name)`).
#
# 4. Create a list that contains the month names from the table above.
#
# </div>

# + tags=["hide"]
# Create monthly variables
jan = 0.70 
feb = 0.75 
mar = 1.85 
apr = 2.93 
may = 3.05 
june = 2.02
july = 1.93
aug = 1.62
sept = 1.84
oct = 1.31
nov = 1.39
dec = 0.84

# Convert to mm
jan = jan * 25.4
feb = feb * 25.4
mar = mar * 25.4
apr = apr * 25.4
may = may * 25.4
june = june * 25.4
july = july * 25.4
aug = aug * 25.4
sept = sept * 25.4
oct = oct * 25.4
nov = nov * 25.4
dec = dec * 25.4

listname_months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
listname_precip = [jan, feb, mar, apr, may, june, july, aug, sept, oct, nov, dec]

print(listname_precip)
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
# 1. Replacing `listname_months` and `listname_precip` with the names of the lists that you created. 
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
# Import necessary plot package
import matplotlib.pyplot as plt

# Plot monthly precipitation values
fig, ax = plt.subplots(figsize=(10, 10))
ax.bar(listname_months, listname_precip, color="blue")
ax.set(title="Add plot title here.",
       xlabel="Add x axis label here.", ylabel="Add y axis label here.");
