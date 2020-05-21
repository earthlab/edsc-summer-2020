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
# Create a list! Make a list called `multi_type_list` that has a length of 5, contains a string, a float, and an integer, and has a string at index `1`. 

# +
# Create your list below this line!

# + tags=["hide"]
try:
    if isinstance(multi_type_list, list):
        print("mutli_type_list is a list!")
        if len(multi_type_list) == 5:
            print("mutli_type_list has the correct length!")
            if isinstance(multi_type_list[1], str):
                print("mutli_type_list contains a string value at index 1!")
            else: 
                print("mutli_type_list does not contain a string value at index 1.\n",
                      "Make sure to add a string value at list index 1.\n", 
                      "Remember python list indexing starts at 0!")
        else:
            print("multi_type_list does not have the correct length.\n",
                  "Make sure that the list has exactly 5 values in it.")
        if any([isinstance(i, str) for i in multi_type_list]):
            print("mutli_type_list contains a string value!")
        else:
            print("mutli_type_list does not contain a string value.\n",
                  "Make sure to make one of the values in your list a string.")
        if any([isinstance(i, int) for i in multi_type_list]):
            print("mutli_type_list contains an integer value!")
        else:
            print("mutli_type_list does not contain an integer value.\n",
                  "Make sure to make one of the values in your list an integer.")
        if any([isinstance(i, float) for i in multi_type_list]):
            print("mutli_type_list contains a float value!")
        else:
            print("mutli_type_list does not contain a float value.\n",
                  "Make sure to make one of the values in your list a float.")
    else:
        print("mutli_type_list is not a list. Make sure that you formatted the list\n",
              "correctly and spelled the variable name right.")
except NameError:
    print("'multi_type_list' is not defined. Make sure you spelled the variable name right!")
# -

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
# Let's use these skills we just learned to modify an existing list. Below is a list called `modify_me`. Modify the list from what it is now, `[1, 3.2, 5, 9, "hi!"]`, to `["first!", 1, 3.2, 8, 9, "hello!", "last!"]`. There are a lot of ways to go about this, so don't be afraid to be creative! 

# Use the operators we learned to modify the list below! 
modify_me = [1, 3.2, 5, 9, "hi!"]
# Add your code below this line. Don't modify line above, and don't manually type out the answer. 
# Use the operators from the lesson! 

# + tags=["hide"]
answer = ["first!", 1, 3.2, 8, 9, "hello!", "last!"]
if modify_me == answer:
    print("You correctly modified the list, good job!")
else: 
    print("Your list didn't match the expected list. Here is the list you produced: {}".format(modify_me))
