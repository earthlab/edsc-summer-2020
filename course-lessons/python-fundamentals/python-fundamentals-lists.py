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
# At the end of this activity, you will be able to:
#
# * Explain how **Python** uses lists to store multiple data values.
# * Create new **Python** lists that contain `int`, `float` and `str` values.
# * Use the list index to update, add, and remove items in a **Python** list.
#
# </div>
#
#
# ## What are Python Lists?
#
# A **Python** list is a data structure that stores a collection of values in a specified order (or sequence). **Python** lists are mutable, which means that they can be changed or updated.
#
# Another interesting feature of **Python** lists is that they can store data of different types, including a mix of `int`, `float`, `str`, etc, values, all in the same list.  You can even create a list that is composed of other lists!
#
# Each value in a list is called an item.  Since lists are sequences of items in a specified order, there is a label for the location (i.e. order number) of each item in the list.
#
# This order label is referred to as an index. Indexing allows lists to be iterable, meaning that you can access the each item in list, in the order in which they appear in the sequence.
#
#
# ### List Index in Python
#
# In **Python**, indexing is used by many data structures, such as lists, to organize data and manage the order of the items within the data structure.
#
# By default, **Python** indexing will always begin at `[0]`, rather `[1]`.
#
# Thus, the first item in a **Python** list has an index `[0]`, the second item in a list has an index `[1]`, and so on.
#
# You can use the index of an item to query its value. For example, you can use the index `[1]` to get the value for the 2nd item (`0.75`) in the following list of values (`0.70, 0.75, 1.85`).
#
#
# ## Create Python Lists
#
# Previously in this chapter, you learned how to create variables to store single data values such as `boulder_precip_in = 20.68`, which contained the the average annual precipitation in inches (in) in Boulder, Colorado.
#
# To create a **Python** list, you use the following syntax:
#
# `list_name = [item_1, item_2, item_3]`
#
# Notice that the values (soon to be items in a list) are enclosed within brackets `[]` and are separated from each other using commas `,`.
#
# Similar to defining variables, you do not have to define what types of values will be stored in the list.
#
# For example, you can create lists of numeric values such as `floats`.

# +
boulder_precip_in = [0.70, 0.75, 1.85]

boulder_precip_in
# -

# You can also create lists of `str` values. Just like defining `str` variables, you need to enclose the individual text strings using quotes `""`.

# +
months = ["January", "February", "March"]

months
# -

# You can also create a list that contains different types of data (e.g. `int`, `float`, `str`), including other defined variables.

# +
jan = 0.70

boulder_avg_precip = [1, jan, "January"]

boulder_avg_precip
# -

# ### Check Type
#
# Just like you are able to check the type of data stored in a variable, you can also check the object type for lists to confirm that it is indeed a list:
#
# `type(list_name)`
#

type(boulder_avg_precip)

# ## Print the Length of a List
#
# To work efficiently with the list index, it is very helpful to know how long the list is, meaning how many items are stored in the list.
#
# You can use the **Python** function `len()` to query this information by including the name of the list as a parameter, or input, to the function as follows:
#
# `len(list_name)`
#
# Using `len()`, you can see that `months` contains 3 items, as it only contained `str` values for January through March.

months

len(months)

# ### Interactive Activity
#
# Create a list! Make a list called `precip_by_location` that has a length of 3 and contains a string for `New York City` at index `2`, a float for the [average annual precipitation in New York City](https://www.usclimatedata.com/climate/new-york/new-york/united-states/usny0996) (46.23 inches), and a string for the units (`inches`).
#
# Note that this means the float value for precipitation and the string value for units can be in any location, but the string for `New York City` needs to be at index `2`.

# +
# Create your list below this line!
# -

# The cell below includes a set of tests to see if you correctly completed the activity in the cell above. They will provide you with feedback that can help you complete the activity.
#
# Be sure to run the cell below to check your code (please do not modify the cell!).

# Run this cell to ensure precip_by_location was created correctly
try:
    if isinstance(precip_by_location, list):
        print("precip_by_location is a list!")
        if len(precip_by_location) == 3:
            print("precip_by_location has the correct length!")
            if isinstance(precip_by_location[2], str):
                print("precip_by_location contains a string value at index 2!")
            else:
                print(
                    "precip_by_location does not contain a string value at index 2.\n",
                    "Make sure to add a string value at list index 2.\n",
                    "Remember python list indexing starts at 0!",
                )
        else:
            print(
                "precip_by_location does not have the correct length.\n",
                "Make sure that the list has exactly 3 values in it.",
            )
        if any([isinstance(i, str) for i in precip_by_location]):
            print("precip_by_location contains a string value!")
        else:
            print(
                "precip_by_location does not contain a string value.\n",
                "Make sure to make one of the values in your list a string.",
            )
        if any([isinstance(i, float) for i in precip_by_location]):
            print("precip_by_location contains a float value!")
        else:
            print(
                "precip_by_location does not contain a float value.\n",
                "Make sure to make one of the values in your list a float.",
            )
    else:
        print(
            "precip_by_location is not a list. Make sure that you formatted the list\n",
            "correctly and spelled the variable name correctly.",
        )
except NameError:
    print(
        "'precip_by_location' is not defined. Make sure you spelled the variable name correctly!"
    )

# ## Query List Items Using Index
#
# As **Python** indexing begins at `[0]`, you can use the list index to query the value of the nth item in the list with `month[index]`, where index is equal to:
#
# `number of items - 1` or `n-1`
#
# For example, if you want to query the second item in the `months` list, you will need to use the index value that results from `2-1`, or `1`.

months[1]

# Note that calling an index value that is larger than `n-1` will result in an error that the index does not exist.
#
# In this example, `months[3]` results in the following error:
#
# `IndexError: list index out of range`
#
# because there are only three items in the list.

# ## Update Items in Lists
#
# In addition to querying values, you can also use the list index to update items in a list by assigning a new value to that index location.
#
# For example, if you want to update the value stored at `months[index]`, you can assign a new value with:
#
# `months[index] = value`

# +
boulder_precip_in[1] = 0

boulder_precip_in

# +
months[1] = "Feb"

months
# -

# ## Insert Items into Lists
#
# You can also use the list index to insert new items into a list by specifying at which index location you want to new value to be. The index locations for the other values in the list will be automatically updated.
#
# For example, if you want to insert a value at the beginning of the list, you can use:
#
# `list_name.insert(0, value)`
#
# In the example below, the months list is incomplete, and the value for January is inserted at the beginning of the list. This automatically updates the index locations for the existing items, such as `February`, which began as index `0` and becomes index `1` when `January` is inserting at the beginning of the list.

# +
# Month list missing the first value for January
months = ["February", "March"]

# Check index value at 0
months[0]

# +
# Modify list to add January at the beginning
months.insert(0, "January")

months
# -

# Check index value at 0 in modified list
months[0]

# February is now at index 1
months[1]

# ## Delete Items From List
#
# You can delete unwanted items from an existing list using the `del` statement:
#
# `del list_name[index]`
#
# Once again, checking the length of a list is helpful before using the list index to modify the list.

len(boulder_precip_in)

# +
del months[2]

months
# -

# ## Append an Item to List
#
# To add an item to the end of a list, you can use the `.append()` function that is associated with lists (referred to as a method of the list object).
#
# You can call this method to add values to a list using the syntax:
#
# `listname.append(value)`

# +
months.append("March")

months

# +
boulder_precip_in.append(2.93)

boulder_precip_in
# -

# ## Add Items to List
#
# You can also add items to a list using the addition operation `+`.
#
# For example, you can add items to the beginning of a list using the following syntax:
#
# `listname = [value] + listname`

# +
boulder_precip_in = [-9999] + boulder_precip_in

boulder_precip_in
# -

# You can also add items to the end of a list by combining the addition `+` with an `=`:
#
# `listname += [value]`
#
# which combines the steps to add and set the list equal to itself plus the new value.

# +
months += ["April"]

months
# -

# You can even use this same assignment operator to add multiple values to the end of a list.

# +
months += ["May", "June"]

months
# -

# By using the `+` and `+=` syntax to add new values to a list, you have actually just used **Python** operators, which are symbols used in **Python** to execute specific operations on variables and data structures such as lists.
#
# You will learn more about different operators in **Python** on the next page of this chapter.

# ### Interactive Activity
#
# Use the skills you just learned to modify the list that you created previously.
#
# Modify `precip_by_location` to look like:
#
# `[1, 20.23, 'inches', 'Boulder', 'Colorado']`
#
# There are a lot of ways to go about this, so don't be afraid to be creative!

# +
# Use the list operators you learned to modify precip_by_location
# -

# The cell below includes a set of tests to see if you correctly completed the activity in the cell above. They will provide you with feedback that can help you complete the activity.
#
# Be sure to run the cell below to check your code (please do not modify the cell!).

# +
# Run this cell to ensure the list was modified correctly
answer = [1, 20.23, "inches", "Boulder", "Colorado"]

try:
    if precip_by_location == answer:
        print("You correctly modified the list, good job!")
    else:
        print(
            "Your list didn't match the expected list. Here is the list you produced: {}".format(
                precip_by_location
            )
        )
except NameError:
    print(
        "Couldn't find list named precip_by_location, make sure the cells where you assigned the \n",
        "list have been run properly.",
    )
