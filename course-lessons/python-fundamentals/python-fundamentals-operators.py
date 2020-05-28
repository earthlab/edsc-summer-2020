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

# ### Interactive Activity
#
# Below, you are given two variables. 
# ```
# a = 5
# b = 2
# ```
# Create a thrid variable, `c`, which is equal to 8. To do this, only use the given variables (`a` and `b`) and arithmetic operators!

a = 5
b = 2
# Using a and b, create a variable named c which is equal to 8


# The cell below is a set of automatic tests to see if you correctly completed the activity in the cell above. They will provide you with feedback on the activity. Please do not modify the cell below! 

# Test to make sure that the variable was assigned correctly
try:
    if c == 8:
        print("Correctly assigned c to be 8!")
    else:
        print("c doesn't equal 8, it instead equals {}. Make sure your arithmetic operators are accurate and correctly assigned to the variable.".format(c))
except NameError:
    print("We couldn't find any variable named c, make sure that you correctly assigned the variable and ran the cell above.")

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

# ### Interactive Activity
#
# Below, you are given two variables, `total_precip_nyc` and `december_precip_nyc`. Add `december_precip_nyc` to `total_precip_nyc` using the `+=` operator.

# +
total_precip_nyc = 42.65
december_precip_nyc = 3.5

# Below this line, combine the two variables
# -

# The cell below is a set of automatic tests to see if you correctly completed the activity in the cell above. They will provide you with feedback on the activity. Please do not modify the cell below! 

# + tags=["hide"]
# Tests to ensure the lists were added correctly

if total_precip_nyc == 46.15:
    print("Variables added correctly!")
else:
    print("Variables not added correctly, the variable total_precip_nyc is assigned {}.".format(total_precip_nyc))
# -

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
# **You have now deliberately used your first Python function!** Functions in **Python** are commands that can take inputs that are used to produce output. 
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
temps1 = [70, 68, 74]
temps2 = [70, 68, 74]
temps3 = temps1

temps1 is temps3
# -

temps1 == temps3

temps1 == temps2

# Here we can see the distinction. Even though `temps1` and `temps2` are identical to one another, they are technically not the same list. But, since `temps3` was set to equal `temps1`, they are the exact same object. 

temps1 is temps2

# `is` can be combined with `not` to check that two items are NOT the same

temps1 is not temps2

# ## Membership Operators
#
# A membership operator, such as `in`, will check if one item contains another item. This can be useful with strings, lists, or other data storage objects such as dataframes. 

# +
precip = "Precipitation"


'Precip' in precip
# -

68 in temps1

69 not in temps1

# ## Logical Operators
#
# Logical operators can be used to check combinations of booleans. The most common logical operators are `and` and `or`. 
#
# `and` will check that both of the statements being checked are true. `True and True` will return `True`, but `True and False` will return `False`. 
#
# `or` will check that one of the statements being checked are true. Unlike `and`, `True or True` will return `True`, and `True or False` will return `True` as well. 
#
# Both `False and False` and `False or False` will return `False`. 

# True and True
68 in temps1 and 70 in temps1

# True and False
68 in temps1 and 69 in temps1

# True or True
68 in temps1 or 70 in temps1

# True or False
68 in temps1 or 69 in temps1

# ### Interactive Activity
#
# Below, there are variables assigned to the output of either relational, identity, membership, or logical operations. Currently, each operation is returning `False`. Modify the operations so that they will all return `True`.

# +
# Relational operation currently returning False, change the below operation so it returns True
relational = 3 <= 2

# Identity operation currently returning False, change the below operation so it returns True
identity = 4 is 3

# Membership operation currently returning False, change the below operation so it returns True
membership = 72 in temps1

# Logical operation currently returning False, change the below operation so it returns True
logical = True and False
# -

# The cell below is a set of automatic tests to see if you correctly completed the activity in the cell above. They will provide you with feedback on the activity. Please do not modify the cell below! 

# + tags=["hide"]
# Tests to see if the operations have been modified correctly

operations = [relational, identity, membership, logical]
operation_names = ["relational", "identity", "membership", "logical"]

if all(operations):
    print("All operations are now returning True, good job!")
else:
    for i, operation in enumerate(operations):
        if not operation:
            print("Your {} operation is still returning False, check to see why that may be!".format(
                operation_names[i]))
# -

#  <div class="notice--info" markdown="1">
#
# ## Additional Resources
#
# * <a href="https://docs.python.org/3/library/stdtypes.html#" target="_blank">Python docs on types and operations</a>
#
# * <a href="https://python-reference.readthedocs.io/en/latest/docs/operators/" target="_blank">Reference docs on operators</a>
#
# </div>   
