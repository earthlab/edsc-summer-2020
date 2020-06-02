---
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.3.2
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

<!-- #region -->
<div class='notice--success' markdown="1">

## <i class="fa fa-graduation-cap" aria-hidden="true"></i> Learning Objectives

At the end of this activity, you will be able to:

* Explain how **Python** uses variables to store data.
* Write **Python** code to:
    * create variables that store single data values (e.g. numeric values, text strings). 
    * check the type of a variable (e.g. integer, string).  

</div>
 

## What are Variables in Python?

Within a programming workflow, variables store data (i.e. information) that you want to re-use in your code (e.g. single numeric value, filename, path to a directory). 

In **Python**, variables can be created without explicitly defining the type of data that it will hold (e.g. integer, text string). 

You can easily create a variable in **Python** using the following syntax:

`variable_name = value`

This basic syntax is the same whether you are assigning a numeric value (e.g. `a = 3`) or a text string value (e.g. `a = "word"` which uses `""` to indicate a text string value). This differs from many other programming languages that require the variable to be explicitly assigned a data type when it is created.

### Importance of Clear and Distinct Variable Names

Just like you want to use good naming conventions for directories on your computer, you also want to assign clear and short names to variables, avoiding spaces or complicated wording, but still specific enough that you know what it is. Underscores (e.g. `boulder_precip_in`) can be helpful to add more detail to the name (e.g. location, measurement, units) and still preserve code readibility. 

A key characteristic of variables is that once a variable is created within your code (e.g. **Jupyter Notebook** file), the value of that variable will remain the same and can be reused throughout the code.

However, you can overwrite an existing variable if you create a new variable with the same name. 

While there are occassions in which you might want to overwrite an existing variable to assign a new value to it, you want to make sure that you give variables both clear and distinct names to avoid *accidentally* overwriting variable values.  


## Numeric Variables

In **Python**, you can create variables to store numeric values such as  integers (`int`) (i.e. whole numbers) and floating point numbers (`float`) (i.e. decimal values).  

For more advanced math applications, you can also use variables to work with <a href="https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex" target="_blank">complex numbers (see Python documentation for more details)</a>. 

As described previously, you do not need to define which numeric type you want to use to create a variable. 

For example, you can create a `int` variable called `boulder_precip_in`, which contains the value for the [average annual precipitation in inches (in) in Boulder, Colorado](https://psl.noaa.gov/boulder/Boulder.mm.precip.html), rounded to the nearest integer.
<!-- #endregion -->

```python
# This is a comment line in Python
boulder_precip_in = 20

# You can see the value of any variable by calling the variable name
boulder_precip_in
```

You could also create a `float` variable to capture the data using decimal units. 

```python
boulder_precip_in = 20.23

boulder_precip_in
```

Notice that in these examples, `boulder_precip_in` was overwritten by the second variable definition because both definitions assigned the same name to the variable. 


## Text String Variables

To create a variable containing a text string (`str`), you need to use quotations (`""`) around the value to identify the value as a text string (e.g. `variable_name = "text"`). 

While in **Python** the single quote (`''`) and the double quote (`""`) are used interchangeably (see the official <a href="https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str" target="_blank">Python Docs</a> for more examples), it is good to choose one option and use it consistently. The exercises and materials that you will explore use the double quote (`""`) for identifying text strings (`str`). 

Using quotes, you can create `str` variables that contain a single word or many words, including punctuation.

```python
city = "Boulder"

city
```

```python
city = "Boulder, CO"

city
```

```python
city = "Boulder, CO is the home of the University of Colorado, Boulder campus."

city
```

### Interactive Activity

Assign values to variables! In the cell below, create a variable called `precip_int` that has an integer as its value. Then, create another variable called `precip_float` that has a float as its value. Last, create another variable called `location` that has a string as its value. 

For these variables, use the [average annual precipitation in New York City](https://www.usclimatedata.com/climate/new-york/new-york/united-states/usny0996), which is 46.23 inches. 

Assign this precipitation value to variables as an integer (`precip_int`) and a float (`precip_float`). Then, assign the city name `New York City` to a string variable (`location`). 

```python
# Assign your variable values below this comment line!

```

The cell below includes a set of tests to see if you correctly assigned the variables in the cell above. They will provide you with feedback on each variable to ensure it was correctly assigned. 

Be sure to run the cell below to check your variables (please do not modify the cell!).

```python
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
```

## Check Variable Type

After you create a variable, you can check the type using the following syntax:

`type(variable_name)`

For example, you can check the type of `boulder_precip_in` after each time that a variable is created with that same name to see that the type changes from `int` to `float`. 

```python
boulder_precip_in = 21

type(boulder_precip_in)
```

```python
boulder_precip_in = 20.68

type(boulder_precip_in)
```

You can also check the type of the variable named `city`, which is a string (`str`) regardless of how many words (or punctuation) it contains. 

```python
city = "Boulder"

type(city)
```

```python
city = "Boulder, CO is the home of the University of Colorado, Boulder campus."

type(city)
```

Checking the type for a variable can help you make sure that you understand what a variable contains and how it can be used. 

For example, you can actually create a `str` variable that contain numbers if you use the syntax for creating a `str` variable (e.g. `variable_name = "value"`).

Notice below that `city_precip` is still a `str`, even though it contains a number.

```python
city_precip = "20.68"

type(city_precip)
```

Thus, the value itself is not important for determining whether the variable is a numeric or string type - the syntax does this. 

A good reminder that it is important to make sure that you are defining variables with the appropriate syntax to distinguish between numeric and string types. 


### Interactive Activity

Check the type of the variables that you made previously! In the cells below, use the `type()` function to check the type for each variable you created previously, i.e. `precip_int`, `precip_float`, and `location`.

```python
# Check your integer variable type here! 
# The output below the cell should be the word "int"

```

```python
# Check your float variable type here! 
# The output below the cell should be the word "float"

```

```python
# Check your string variable type here! 
# The output below the cell should be the word "str"

```
