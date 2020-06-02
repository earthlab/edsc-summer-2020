# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.4'
#       jupytext_version: 1.2.4
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

#
# <div class='notice--success' markdown="1">
#
# ## <i class="fa fa-graduation-cap" aria-hidden="true"></i> Learning Objectives
#
# At the end of this activity, you will be able to:
#
# * Explain variables are used in **Python** to store information.
# * Use **Python** code to create variables that store single data values including numbers and text strings. 
# * Check the data type of a variable using **Python**
# </div>
#  

# ## What are Variables in Python?
#
# A variable in programming is used to store information that you want to re-use in your code. Examples of things that you may wish to save in your code include:
#
# * numeric values, 
# * filenames
# * paths 
# * or even larger datasets such as a remote sensing image or a terrain model
#
# In **Python**, variables can be created without explicitly defining the type of data that it will hold (e.g. integer, text string). 
#
# You can create a variable in **Python** using the following syntax:
#
# `variable_name = value`

# Try it out - run this cell
my_variable = 5

# +
# In this cell type my_variable and run the cell!
# -

# This syntax for creating variables is the same whether you are assigning a numeric or text value to a variable. For example below you assign the variable name `a` the value of 3 which is a number:  
#
# `a = 3`
#
# Here is an example of assigning the same variable name `a` a text string value 
#
# `a = "a word"`.
#
# Notice that strings (character values) use double quotes `""` to indicate a text string value. 
#
#
# <i class="fa fa-star"></i> **Data Tip:** Some programming languages require a variable to be explicitly assigned a data type when it is created. You do not need to worry about this when using `Python`, however! 
# {: .notice--success }
#
#
# ### Expressive Programming: Easy to Understand Variable Names Makes Your Code Easier to Read
#
# Just like you want to use <a href="https://www.earthdatascience.org/courses/intro-to-earth-data-science/open-reproducible-science/get-started-open-reproducible-science/best-practices-for-organizing-open-reproducible-science/"> expressive naming conventions (names that represent what is stored within the directory)</a> for directories on your computer, you also want to use short, clear names for your variables to make your code easier to read. Best practices for variable names include:
#
# When naming variables, you want to avoid: 
#
# * spaces in your variable names
# * complicated wording
# * long variable names
# * words that do not represent what the variable contains (example: `my_variable` vs `precip_data`)
#
# When naming a variable you want to keep the name short but specific enough that someone reading your code can understand what it contains. It is good practice to use underscores (e.g. `boulder_precip_in`) to create multi-word variable names that provide specifics regarding the variable's content. The underscore makes the variable name easier to read and follows python <a href="https://www.python.org/dev/peps/pep-0008/#naming-conventions" target="_blank">PEP8 best practices for code readability</a>. 
#
#
# <i class="fa fa-star"></i> **Data Tip:** Read more about expressive variable names and clean code <a href="https://www.earthdatascience.org/courses/intro-to-earth-data-science/write-efficient-python-code/intro-to-clean-code/expressive-variable-names-make-code-easier-to-read/">in this earth data science lesson.</a>
# {: .notice--success }
#
#
# ### Variables Are Available In Your Coding Environment Once Defined 
#
# A key characteristic of variables is that once you create a variable in your coding environment (that is to say you run the actual line of code that defines the variable), it is available throughout your code. So for example if you create a variable at the top of a Jupyter Notebook, the value of associated with that variable will remain the same and can be reused in cells lower down in the notebook.
#
# <i class="fa fa-star"></i> **Data Tip:** You can overwrite an existing variable if you create a new variable with the same name. For example if you assign `a = 5` in one cell and then assign `a = "dog"` in the next cell, the final value of `a` will be `"dog"`.
# {: .notice--success }
#
# While there are occasions in which you might want to overwrite an existing variable to assign a new value to it, you want to make sure that you give variables both clear and distinct names to avoid *accidentally* overwriting variable values.  

# Here you assign the variable name temperature the value 55 (a number)
temperature = 55
temperature

# Note that you can easily reassign a variable name to contain a new value (a string / word in this case)
temperature = "doctor"
temperature

#
# ## About Data Types in Python
#
# Python data types are important to understand when coding. Below you will learn 
# more about the different types of variables that you can store including:
#
# * Numbers (integers and floats)
# * Strings (letters / characters and words)
#
# ## Numeric Variables in Python
#
# In **Python**, you can create variables to store numeric values such as  
# integers (`int`) which represent whole numbers and floating point numbers 
# which represent decimal values (`float`).  
#
# <i class="fa fa-star"></i> **Data Tip:** For more advanced math applications, you can also use variables to work with <a href="https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex" target="_blank">complex numbers (see Python documentation for more details)</a>.
# {: .notice--success }
#
# As described previously, you do not need to define which numeric type you want to use to create a variable. 
#
# For example, you can create a `int` variable called `boulder_precip_in`, which contains the value for the [average annual precipitation in inches (in) in Boulder, Colorado](https://psl.noaa.gov/boulder/Boulder.mm.precip.html), rounded to the nearest integer.

# +
# This is a comment line in Python
boulder_precip_integer = 20

# You can see the value of any variable by calling the variable name
boulder_precip_integer
# -

# You can use the `type()` function to figure out the type of data stored in a 
# variable.

# What is the type of data stored in boulder_precip_in
type(boulder_precip_integer)

# If your data has decimal places associated with it, it will be stored in Python 
# as a type: `float`. 

# +
boulder_precip_float = 20.23

boulder_precip_float
# -

type(boulder_precip_float)

# ## How to Store Text Variables: Strings in Python
#
# To create a variable containing a text string (`str`), you use quotation marks 
# (`""`) around the value. For example: 
#
# `variable_name = "text"`
#
# While in **Python** the single quote (`''`) and the double quote (`""`) are 
# used interchangeably (see the official <a href="https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str" target="_blank">Python Docs</a> for more examples), we suggest 
# that you use double quotes `""` to define strings (type == `str`) following 
# `PEP8` code style for Python best practices. 
#
# Using quotes, you can create `str` variables that contain a single word or 
# many words, including punctuation. Below are some examples of creating a string. 

# +
city = "Boulder"

city

# +
city_state = "Boulder, CO"

city_state

# +
city_description = "Boulder, CO is the home of the University of Colorado, Boulder campus."

city_description

# +
<div class="notice--warning" markdown="1">

## <i class="fa fa-pencil-square-o" aria-hidden="true"></i> Interactive Activity

You can 
It's time for you to create some variables of your own! In the cell below, create the following: 

1. a variable called `precip_int` that stores an integer value
2. a variable called `precip_float` that stores a float
3. a variable called `location` that has a string as its value. 

For these variables, use the [average annual precipitation in New York City](https://www.usclimatedata.com/climate/new-york/new-york/united-states/usny0996), which is 46.23 inches. 

Assign this precipitation value to variables as an integer (`precip_int`) and a float (`precip_float`). Then, assign the city name `New York City` to a string variable (`location`). 

</div>
# -

# <div class="notice--warning" markdown="1">
#
# ## <i class="fa fa-pencil-square-o" aria-hidden="true"></i> Interactive Activity - What Does Float() Do?
#
# Run the code in the cell below. What does the `float()` function do to the value stored in the variable named `a`?
#
# </div>

# +
# Activity 1: run the code below - what does the float() function do? 
a = 75
b = float(a)
print(a, b)

# What data type is variable b? (hint: use the type() function to find out)


# -

# <div class="notice--warning" markdown="1">
#
# ## <i class="fa fa-pencil-square-o" aria-hidden="true"></i> Interactive Activity  - Create Some Variables
#
# It's time for you to create some variables of your own! In the cell below, create the following: 
#
# 1. a variable called `precip_int` that stores an integer value representing the average annual precipitation in New York City.
# 2. a variable called `precip_float` that stores a float value representing the average annual precipitation in New York City. 
# 3. a variable called `location` that stores the string New York City which is the name of the location for this precipipitation value.
#
# HINT: you can coerce a floating point value to a integer using the `int()` function. Using int() to convert your floating point value to an integer. The variable name should be precip_int. 
#
# Try the code below to see how this works:
#
# ```
# a = 75.643
# b = int(a)
# print(a, b)
# ```
#
# NOTE: The [average annual precipitation in New York City as seen on this website is ](https://www.usclimatedata.com/climate/new-york/new-york/united-states/usny0996), which   46.23 inches. 
#
# </div>

# +
# Activity 2: Assign your variable values below this comment line!
# -

# The cell below includes a set of tests to see if you correctly assigned the variables in the cell above. They will provide you with feedback on each variable to ensure it was correctly assigned. 
#
# Be sure to run the cell below to check your variables (please do not modify the cell!).

# +
# Run this cell to ensure variables were correctly assigned

# Integer tests
try:
    print("Variable precip_int has been assigned the value " +
          str(precip_int) + ".")
    if isinstance(precip_int, int):
        print("Variable precip_int is an integer, good job!")
        if precip_int == 46:
            print("Variable precip_int equals 46, good job!")
        else:
            print("Variable precip_int exists and is an integer, but has the wrong value.\n",
                  "Make sure you assigned the value of precip_int to be a whole number closest\n",
                  "to the average annual rainfall in NYC.")
    else:
        print("Variable precip_int exists, but is not an integer.\n",
              "Make sure you assigned the value of precip_int to be a whole number.")

except NameError:
    print("Can't find a variable named precip_int, make sure you've\n",
          "correctly spelled the variable name and assigned it a value!")

# Float tests
try:
    print("Variable precip_float has been assigned the value " +
          str(precip_float) + ".")
    if isinstance(precip_float, float):
        print("Variable precip_float is a float, good job!")
        if precip_float == 46.23:
            print("Variable precip_float equals 46.23, good job!")
        else:
            print("Variable precip_float exists and is a float, but has the wrong value.\n",
                  "Make sure you assigned the value of precip_float to be equivalent\n",
                  "to the average annual rainfall in NYC.")
    else:
        print("Variable precip_float exists, but is not a float.\n",
              "Make sure you assigned the value of precip_float to be a number with a decimal value.")
except NameError:
    print("Can't find a variable named precip_float, make sure you've\n",
          "correctly spelled the variable name and assigned it a value!")

# String tests
try:
    print("Variable location has been assigned the value " +
          str(location) + ".")
    if isinstance(location, str):
        print("Variable location is a string, good job!")
        if location == "New York City":
            print("Variable location equals New York City, good job!")
        else:
            print("Variable location exists and is a string, but has the wrong value.\n",
                  "Make sure you assigned the value of location to be \n",
                  "a string of the location: New York City.")
    else:
        print("Variable location exists, but is not a string.\n",
              "Make sure you assigned the value of location to be a value surrounded by quotes.")
except NameError:
    print("Can't find a variable named location, make sure you've\n",
          "correctly spelled the variable name and assigned it a value!")
# -

# ## Check Variable Type
#
# In the activities above, you used the `type()` function to determine what type of data are stored in a variable. 
#
# `type(variable_name)`
#
# For example, you can check the type of `boulder_precip_in` after each time that a variable is created with that same name to see that the type changes from `int` to `float`. 

# +
boulder_precip_in = 21

type(boulder_precip_in)

# +
boulder_precip_in = 20.68

type(boulder_precip_in)
# -

# You can also check the type of the variable named `city`, which is a string (`str`) regardless of how many words (or punctuation) it contains. 

# +
city = "Boulder"

type(city)

# +
city = "Boulder, CO is the home of the University of Colorado, Boulder campus."

type(city)
# -

# Checking the variable `type()` let's you test what a variable contains and 
# in turn how it can be used. 
#
# For example, you can actually create a `str` variable that contain numbers if you use the syntax for creating a `str` variable (e.g. `variable_name = "value"`).
#
# Notice below that `city_precip` is still a `str`, even though it contains a number.

# +
city_precip = "20.68"

type(city_precip)
# -

# If you wanted to perform math on that variable it would not work the way 
# you think it should. 

# Multiply city_precip by 2
city_precip*2

# Thus, the value itself is not important for determining whether the variable is a numeric or string type - the syntax does this. 
#
# A good reminder that it is important to make sure that you are defining variables with the appropriate syntax to distinguish between numeric and string types. 

# <div class="notice--warning" markdown="1">
#
# ## <i class="fa fa-pencil-square-o" aria-hidden="true"></i> Challenge - Data Types & Math
#
# In the cell below, run the following code which divides variable a by variable b (`a/b`). 
#
# ```
# a = 5
# b = 3
# c = a/b
# ```
#
# Use the `type()` function to determine what type of value is stored in each variable defined (a, b and c).
#
#
# </div>

# +
# Run the code above in this cell. Then determin the type of each variable (a, b, c)


