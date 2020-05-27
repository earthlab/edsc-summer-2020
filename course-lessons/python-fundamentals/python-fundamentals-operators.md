---
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.4.2
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

<!-- #region -->
<div class='notice--success' markdown="1">

## <i class="fa fa-graduation-cap" aria-hidden="true"></i> Learning Objectives

* Explain how operators are used in **Python** to execute a specific computation or operation.
* Write **Python** code to run different operations on data (e.g. arithmetic calculations)

</div>


## What are Operators in Python?

Operators are symbols in Python that carry out a specific computation, or operation. The value or condition that the operator operates on is called the operand. 

The operand can be a variable (e.g. `jan_precip_in` which has some value, say, 0.70) or data structure like a list (e.g. `months`). The operand can also be an expression or statement (e.g. checking that list `months` contains the value `January`). 

There are <a href="https://python-reference.readthedocs.io/en/latest/docs/operators/" target="_blank">many different types of operators</a> in **Python** including: 

| Operator | Usage | Example |
|:-----------------------------------|:-----------------------------------|:-----------------------------------|
| Arithmetic  | to complete mathematical calculations | `boulder_precip_in * 25.4` |
| Assignment  | to assign new values (typically as a result of a arithmetic calculation) | `boulder_precip_in *= 25.4` |
| Comparison or Relational  | to compare operands (e.g. greater than symbol `>`)  | `boulder_precip_in > phoenix_precip_in`|
| Identity  | to check whether operands are the same | `boulder_precip_in is not phoenix_precip_in` |
| Membership  | to check whether one operand is contained within another operand | `"January" in months` |
| Logical  | to check whether operands are `true` | `"January" in months AND "Jan" in months` |
<!-- #endregion -->

## Arithmetic Operators

In **Python**, there are <a href="https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex" target="_blank">many arithmetic operations</a> that can be completed, including operators for: 
* addition (`+`)
* subtraction (`-`)
* multiplication (`*`)
* division (`/`)
* exponents (`**`)

Review the cells below and notice that the output is automatically printed without the need to tell **Python** to display the output. 

```python
a = 2
b = 3

a + b
```

```python
b - a
```

```python
b / a
```

```python
a * b
```

```python
a ** b
```

For scientific workflows, these arithmetic operators are very useful for converting the units of measurements, for example, from inches to millimeters (1 inch = 25.4 mm) for precipitation values.

The example belows converts the average precipitation value for Boulder, CO in January from inches to millimeters.

```python
jan_precip = 0.70

jan_precip * 25.4
```

## Assignment Operators

While arithmetic operators are very useful for calculations, they do not change the original values. 

For example, the variable `jan_precip` continues to store the value `0.7` (the measurement in inches), even after the calculations completed above. 

```python
jan_precip
```

If you want to assign a new value as a result of a calculation, you can use an assignment operator, which combines the arithmetic operator (e.g. `*`) with the `=` to set a new value. 

For example, you can combine `*` and `=` to multiple a value and set the result equal to itself plus the new value. 

```python
jan_precip *= 25.4
```

Recall that on the previous page on working with lists, you also used an assignment operator to add items to the end of a list. 

This is a special case of the addition assignment operator `+=` because it is not actually completing a mathematical operation on the list.  It simply adds the values as new items to the end of the list. 

```python
months = ["January", "February"]

months
```

```python
months += ["March", "April"]

months
```

<!-- #region -->
However, not all assignment operators can be used on all object types. For example, the following code will result in an error because lists cannot have mathematical operations executed on them.  

```python
boulder_precip_in = [0.70, 0.75, 1.85]
boulder_precip_in *= 25.4
```

You can review the <a href="https://docs.python.org/3/library/stdtypes.html#" target="_blank">Python docs on types and operations</a> to see what kinds of operations can be run on different object types. 
<!-- #endregion -->

## Print Output

Notice now that the output is not automatically printed.

```python
jan_precip = 0.70

jan_precip *= 25.4
```

To see the new value, you can call the variable name (e.g. `jan_precip`), or you can use the print statement (e.g. `print(jan_precip)`) to display the new value. 

Using the print statement can be very helpful because then you can print multiple values. 

For example, notice calling only the variable names (e.g. `a`, `jan_precip`, `b`), you are only shown the value of the last variable.

```python
a
jan_precip
b
```

Using `print()`, you can print as many things as you want. 

```python
print(a)
print(jan_precip)
print(b)
```

You can even combine the variables with a text string in a print statement by including a text string `"text"` within the print statement.

To do this, simply separate the text string from the object that is being printed using a comma `,`. 

```python
print("January precipitation:", jan_precip)
```

Notice that the word `print` does not show up the output. Instead, you simply see the result, without the parentheses or quotations for the text string. 

**You have now deliberately used your first **Python** function!** Functions in **Python** are commands that can take inputs that are used to produce output. 

You will learn more about functions later in this textbook, and you will use the `print` function a lot, as it can be very handy for viewing results and for communicating the status of your code. 


## Relational Operators

Often in python you need to compare two values against each other. For these checks, you can check a statement, such as `3 < 4` and get returned one of two values from python: `True` or `False`. These are called boolean values, and can be very powerful in scripts. A boolean is simply one bit of data that is either 1 (True), or 0 (False). Like strings or integers, booleans are there own data type.

In **Python**, there are <a href="https://python-reference.readthedocs.io/en/latest/docs/operators/#relational-operators" target="_blank">many relational operations</a> that can be completed, including operators for: 
* equal (`==`)
* not equal (`!=`)
* greater than (`>`)
* greater than or equal (`>=`)
* less than (`<`)
* less than or equal (`<=`)

Review the cells below to see what these operations return in different circumstances.

```python
type(True)
```

Relational operations return a boolean value. 

```python
3 < 4
```

```python
3 > 4
```

```python
3 == 3
```

```python
3 == 4
```

```python
3 != 4
```

```python
3 <= 4
```

```python
3 <= 3
```

```python
3 >= 4
```

## Identity Operators

An identity operator, such as `is`, will check if two variables are referring to the same object. It is similar to the `==` operator, except that it will not only check that the values of two variables are identical, but it will check that they are referring to the exact same thing. It's a subtle distinction, but can be very useful. 

```python
temps1 = [70, 68, 74]
temps2 = [70, 68, 74]
temps3 = temps2

temps1 is temps3
```

```python
temps1 == temps3
```

```python
temps1 == temps2
```

Here we can see the distinction. Even though `temps1` and `temps2` are identical to one another, they are technically not the same list. But, since `temps3` was set to equal `temps1`, they are the exact same object. 

```python
temps1 is temps2
```

`is` can be combined with `not` to check that two items are NOT the same

```python
temps1 is not temps2
```

## Membership Operators

A membership operator, such as `in`, will check if one item contains another item. This can be useful with strings, lists, or other data storage objects such as dataframes. 

```python
precip = "Precipitation"


'Precip' in precip
```

```python
68 in temps1
```

```python
69 not in temps1
```

## Logical Operators

Logical operators can be used to check combinations of booleans. The most common logical operators are `and` and `or`. 

`and` will check that both of the statements being checked are true. `True and True` will return `True`, but `True and False` will return `False`. 

`or` will check that one of the statements being checked are true. Unlike `and`, `True or True` will return `True`, and `True or False` will return `True` as well. 

Both `False and False` and `False or False` will return `False`. 

```python
# True and True
68 in temps1 and 70 in temps1
```

```python
# True and False
68 in temps1 and 69 in temps1
```

```python
# True or True
68 in temps1 or 70 in temps1
```

```python
# True or False
68 in temps1 or 69 in temps1
```

<!-- #region -->


 <div class="notice--info" markdown="1">

## Additional Resources

* <a href="https://docs.python.org/3/library/stdtypes.html#" target="_blank">Python docs on types and operations</a>

* <a href="https://python-reference.readthedocs.io/en/latest/docs/operators/" target="_blank">Reference docs on operators</a>

</div>   
<!-- #endregion -->
