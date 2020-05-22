# ---
# jupyter:
#   jupytext:
#     formats: ipynb,md
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

# <div class='notice--success' markdown="1">
#
# ## <i class="fa fa-graduation-cap" aria-hidden="true"></i> Learning Objectives
#
# * Explain how operators are used in **Python** to execute a specific computation or operation.
# * Write **Python** code to run different operations on data (e.g. arithmetic calculations)
#
# </div>
#
#
# ## What are Operators in Python?
#
# Operators are symbols in Python that carry out a specific computation, or operation. The value or condition that the operator operates on is called the operand. 
#
# The operand can be a variable (e.g. `jan_precip_in` which has some value, say, 0.70) or data structure like a list (e.g. `months`). The operand can also be an expression or statement (e.g. checking that list `months` contains the value `January`). 
#
# There are <a href="https://python-reference.readthedocs.io/en/latest/docs/operators/" target="_blank">many different types of operators</a> in **Python** including: 
#
# | Operator | Usage | Example |
# |:-----------------------------------|:-----------------------------------|:-----------------------------------|
# | Arithmetic  | to complete mathematical calculations | `boulder_precip_in * 25.4` |
# | Assignment  | to assign new values (typically as a result of a arithmetic calculation) | `boulder_precip_in *= 25.4` |
# | Comparison or Relational  | to compare operands (e.g. greater than symbol `>`)  | `boulder_precip_in > phoenix_precip_in`|
# | Identity  | to check whether operands are the same | `boulder_precip_in is not phoenix_precip_in` |
# | Membership  | to check whether one operand is contained within another operand | `"January" in months` |
# | Logical  | to check whether operands are `true` | `"January" in months AND "Jan" in months` |
#
# ## Arithmetic Operators
#
# In **Python**, there are <a href="https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex" target="_blank">many arithmetic operations</a> that can be completed, including operators for: 
# * addition (`+`)
# * subtraction (`-`)
# * multiplication (`*`)
# * division (`/`)
# * exponents (`**`)
#
# Review the cells below and notice that the output is automatically printed without the need to tell **Python** to display the output. 

# +
a = 2
b = 3

a + b
# -

b - a

b / a

a * b

a ** b

# For scientific workflows, these arithmetic operators are very useful for converting the units of measurements, for example, from inches to millimeters (1 inch = 25.4 mm) for precipitation values.
#
# The example belows converts the average precipitation value for Boulder, CO in January from inches to millimeters.

# +
jan_precip = 0.70

jan_precip * 25.4
# -

# ## Assignment Operators
#
# While arithmetic operators are very useful for calculations, they do not change the original values. 
#
# For example, the variable `jan_precip` continues to store the value `0.7` (the measurement in inches), even after the calculations completed above. 

jan_precip

# If you want to assign a new value as a result of a calculation, you can use an assignment operator, which combines the arithmetic operator (e.g. `*`) with the `=` to set a new value. 
#
# For example, you can combine `*` and `=` to multiple a value and set the result equal to itself plus the new value. 

jan_precip *= 25.4

# Recall that on the previous page on working with lists, you also used an assignment operator to add items to the end of a list. 
#
# This is a special case of the addition assignment operator `+=` because it is not actually completing a mathematical operation on the list.  It simply adds the values as new items to the end of the list. 

# +
months = ["January", "February"]

months

# +
months += ["March", "April"]

months
# -

# However, not all assignment operators can be used on all object types. For example, the following code will result in an error because lists cannot have mathematical operations executed on them.  
#
# ```python
# boulder_precip_in = [0.70, 0.75, 1.85]
# boulder_precip_in *= 25.4
# ```
#
# You can review the <a href="https://docs.python.org/3/library/stdtypes.html#" target="_blank">Python docs on types and operations</a> to see what kinds of operations can be run on different object types. 

# ## Print Output
#
# Notice now that the output is not automatically printed.

# +
jan_precip = 0.70

jan_precip *= 25.4
# -

# To see the new value, you can call the variable name (e.g. `jan_precip`), or you can use the print statement (e.g. `print(jan_precip)`) to display the new value. 
#
# Using the print statement can be very helpful because then you can print multiple values. 
#
# For example, notice calling only the variable names (e.g. `a`, `jan_precip`, `b`), you are only shown the value of the last variable.

a
jan_precip
b

# Using `print()`, you can print as many things as you want. 

print(a)
print(jan_precip)
print(b)

# You can even combine the variables with a text string in a print statement by including a text string `"text"` within the print statement.
#
# To do this, simply separate the text string from the object that is being printed using a comma `,`. 

print("January precipitation:", jan_precip)

# Notice that the word `print` does not show up the output. Instead, you simply see the result, without the parentheses or quotations for the text string. 
#
# **You have now deliberately used your first **Python** function!** Functions in **Python** are commands that can take inputs that are used to produce output. 
#
# You will learn more about functions later in this textbook, and you will use the `print` function a lot, as it can be very handy for viewing results and for communicating the status of your code. 

# ## Relational Operators
#
# Often in python you need to compare two values against each other. For these checks, you can check a statement, such as `3 < 4` and get returned one of two values from python: `True` or `False`. These are called boolean values, and can be very powerful in scripts. A boolean is simply one bit of data that is either 1 (True), or 0 (False). Like strings or integers, booleans are there own data type.
#
# In **Python**, there are <a href="https://python-reference.readthedocs.io/en/latest/docs/operators/#relational-operators" target="_blank">many relational operations</a> that can be completed, including operators for: 
# * equal (`==`)
# * not equal (`!=`)
# * greater than (`>`)
# * greater than or equal (`>=`)
# * less than (`<`)
# * less than or equal (`<=`)
#
# Review the cells below to see what these operations return in different circumstances.

type(True)

# Relational operations return a boolean value. 

3 < 4

3 > 4

3 == 3

3 == 4

3 != 4

3 <= 4

3 <= 3

3 >= 4

# ## Identity Operators
#
# An identity operator, such as `is`, will check if two variables are referring to the same object. It is similar to the `==` operator, except that it will not only check that the values of two variables are identical, but it will check that they are referring to the exact same thing. It's a subtle distinction, but can be very useful. 

# +
list1 = [1, 2]
list2 = [1, 2]
list3 = list1

list1 is list3
# -

list1 == list3

list1 == list2

# Here we can see the distinction. Even though `list1` and `list2` are identical to one another, they are technically not the same list. But, since `list3` was set to equal `list1`, they are the exact same object. 

list1 is list2

# `is` can be combined with `not` to check that two items are NOT the same

list1 is not list2

# ## Membership Operators
#
# A membership operator, such as `in`, will check if one item contains another item. This can be useful with strings, lists, or other data storage objects such as dataframes. 

# +
precip = "Precipitation"


'Precip' in precip

# +
temps = [70, 68, 74]

68 in temps
# -

69 not in temps

#
#
#  <div class="notice--info" markdown="1">
#
# ## Additional Resources
#
# * <a href="https://docs.python.org/3/library/stdtypes.html#" target="_blank">Python docs on types and operations</a>
#
# * <a href="https://python-reference.readthedocs.io/en/latest/docs/operators/" target="_blank">Reference docs on operators</a>
#
# </div>   

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
