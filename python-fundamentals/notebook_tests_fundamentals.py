import matplotcheck.base as mpc

# TESTS FOR THE VARIABLES NOTEBOOK
def variables_test_int(precip_int):
    """Testing that the integer variable was correctly assigned."""
    return_message = ""

    if isinstance(precip_int, int):
        return_message += "Variable precip_int is an integer, good job!\n"
        if precip_int == 46:
            return_message += "Variable precip_int equals 46, good job!"
        else:
            return_message += """Variable precip_int exists and is an integer,
but has the wrong value.
Make sure you assigned the value of precip_int to be a whole number closest
to the average annual rainfall in NYC."""
    else:
        return_message += """Variable precip_int exists, but is not an integer.
Make sure you assigned the value of precip_int to be a whole number."""

    return return_message


def variables_test_float(precip_float):
    """Testing that the float variable was correctly assigned."""
    return_message = ""

    if isinstance(precip_float, float):
        return_message += "Variable precip_float is a float, good job!\n"
        if precip_float == 46.23:
            return_message += "Variable precip_float equals 46.23, good job!"
        else:
            return_message += """Variable precip_float exists and is a float,
but has the wrong value.
Make sure you assigned the value of precip_float to be equivalent
to the average annual rainfall in NYC."""
    else:
        return_message += """Variable precip_float exists, but is not a float.
Make sure you assigned the value of precip_float to be a number
with a decimal value."""

    return return_message


def variables_test_string(location):
    """Testing that the string variable was correctly assigned."""
    return_message = ""

    if isinstance(location, str):
        return_message += "Variable location is a string, good job!\n"
        if location == "New York City":
            return_message += "Variable location equals New York City!"
        else:
            return_message += """Variable location exists and is a string,
but has the wrong value.
Make sure you assigned the value of location to be
a string of the location: New York City."""
    else:
        return_message += """Variable location exists, but is not a string.
Make sure you assigned the value of location
to be a value surrounded by quotes."""

    return return_message


# TESTS FOR THE LISTS NOTEBOOK
def lists_test_precip_by_location(precip_by_location):
    """Test to ensure precip_by_location list contains all of the laid
    out requirements provided in the notebook."""
    return_message = ""
    if isinstance(precip_by_location, list):
        return_message += "precip_by_location is a list!"
        if len(precip_by_location) == 3:
            return_message += "\nprecip_by_location has the correct length!"
            if isinstance(precip_by_location[2], str):
                return_message += (
                    "\nprecip_by_location contains a string value at index 2!"
                )
            else:
                return_message += """
precip_by_location does not contain a string value at index 2.
Make sure to add a string value at list index 2.
Remember python list indexing starts at 0!"""
        else:
            return_message += """
precip_by_location does not have the correct length.
Make sure that the list has exactly 3 values in it."""
        if any([isinstance(i, str) for i in precip_by_location]):
            return_message += "\nprecip_by_location contains a string value!"
        else:
            return_message += """
precip_by_location does not contain a string value.
Make sure to make one of the values in your list a string."""
        if any([isinstance(i, float) for i in precip_by_location]):
            return_message += "\nprecip_by_location contains a float value!"
        else:
            return_message += """
precip_by_location does not contain a float value.
Make sure to make one of the values in your list a float."""
    else:
        return_message += """
precip_by_location is not a list. Make sure that you formatted the list
correctly and spelled the variable name correctly."""

    return return_message


def lists_test_precip_by_location_modify(precip_by_location):
    """Test to ensure that precip_by_location was correctly modified."""
    answer = [1, 20.23, "inches", "Boulder", "Colorado"]
    return_message = ""

    if precip_by_location == answer:
        return_message = "You correctly modified the list, good job!"
    else:
        return_message = """Your list didn't match the expected list. Here is
the list you produced:
{}""".format(
            precip_by_location
        )

    return return_message


# TESTS FOR THE OPERATORS NOTEBOOK
def operators_test_march_precip(march_precip_mm):
    """Test to make sure that march_precip_mm was assigned correctly"""
    if march_precip_mm == 46.99:
        return "Correctly assigned march_precip_mm to be 46.99!"
    else:
        return """march_precip_mm doesn't equal 46.99, it instead equals {}.
Make sure your arithmetic operators are accurate and correctly assigned
to the variable.""".format(
            march_precip_mm
        )


def operators_test_nyc_precip(annual_avg_precip_nyc):
    """Test to make sure that annual_avg_precip_nyc was assigned correctly"""
    if annual_avg_precip_nyc == 46.23:
        return "Variables added correctly!"
    else:
        return """Variables not added correctly, the variable total_precip_nyc
is assigned
{}.""".format(
            annual_avg_precip_nyc
        )


def operators_test_operation_modifications(relational, identity, membership, logical):
    """Tests to see if the operations have been modified correctly"""
    operations = [relational, identity, membership, logical]
    operation_names = ["relational", "identity", "membership", "logical"]

    return_message = ""
    if all(operations):
        return_message = "All operations are now returning True, good job!"
    else:
        for i, operation in enumerate(operations):
            if not operation:
                return_message += """Your {} operation is still returning False,
check to see why that may be!""".format(
                    operation_names[i]
                )

    return return_message


# TESTS FOR THE EXERCISE NOTEBOOK

# Answer lists for exercise

correct_month_names = [
    "jan",
    "feb",
    "mar",
    "apr",
    "may",
    "june",
    "july",
    "aug",
    "sept",
    "oct",
    "nov",
    "dec",
]

correct_month_precip_in = [
    0.70,
    0.75,
    1.85,
    2.93,
    3.05,
    2.02,
    1.93,
    1.62,
    1.84,
    1.31,
    1.39,
    0.84,
]

correct_month_precip_mm = [i * 25.4 for i in correct_month_precip_in]

correct_list_of_lists = [correct_month_names, correct_month_precip_mm]


def exercise_test_months_list(boulder_precip_months):
    """Testing that the boulder_precip_months list created is correct"""
    if boulder_precip_months == correct_month_names:
        return """List 'boulder_precip_months' successfully assigned and has correct values!"""
    else:
        if not all([type(i) == str for i in boulder_precip_months]):
            return """The list 'boulder_precip_months' was successfully created,
but not all of the values in the list are strings."""
        else:
            error_msg = """The list 'boulder_precip_months' was successfully
created, but it is assigned these values: \n{}
Please ensure that the values are strings with the month names from the table
above."""
            return error_msg.format(boulder_precip_months)


def exercise_test_precip_inches_list(boulder_precip_inches):
    """Testing that the boulder_precip_inches list was created is correct"""
    if boulder_precip_inches == correct_month_precip_in:
        return (
            "List 'boulder_precip_inches' successfully assigned and has correct values!"
        )
    else:
        if not all([type(i) == float for i in boulder_precip_inches]):
            return """The list 'boulder_precip_inches' was successfully created,
but not all of the values in the list are float values."""
        else:
            error_msg = """The list 'boulder_precip_inches' was successfully
created, but it is assigned these values:\n{}
Please ensure that the values are the values from the table above."""
            return error_msg.format(boulder_precip_inches)


def exercise_test_precip_mm_list(boulder_precip_mm):
    """Testing that the boulder_precip_mm list created is correct"""
    if boulder_precip_mm == correct_month_precip_mm:
        return "List 'boulder_precip_mm' was successfully assigned and has the correct converted values!"
    else:
        if not all([type(i) == float for i in boulder_precip_mm]):
            return """The list 'boulder_precip_mm' was successfully created,
but not all of the values in the list are float values."""
        else:
            error_msg = """There is a variable named 'boulder_precip_mm', but
it is assigned these values:\n{}
Please ensure that the values are the values from the table above,
but converted to be mm instead of inches. Hint: Multiply the original values by
25.4."""
            return error_msg.format(boulder_precip_mm)


def exercise_test_list_of_lists(all_boulder_data):
    """Testing that the all_boulder_data list created is correct"""
    if all_boulder_data == correct_list_of_lists:
        return "List 'all_boulder_data' was successfully assigned and has the correct converted values!"
    else:
        if not all([type(i) == list for i in all_boulder_data]):
            return """The list 'all_boulder_data' was successfully created,
but not all of the values in the list are lists."""
        else:
            error_msg = """There is a variable named 'all_boulder_data', but
it is assigned these values:\n{}
Please ensure that the values are the lists you created above.
Also make sure you put the names list in index 0 and the list of precipitation
values at index 1 of the all_boulder_data list."""
            return error_msg.format(all_boulder_data)


def exercise_test_plot(ax):
    """Testing the plot made by the student."""
    plot_test = mpc.PlotTester(ax)

    return_message = ""

    try:
        plot_test.assert_plot_type(
            "bar",
            """Plot is not a bar type, make sure that the original code you
copied wasn't modified to change the plot type!""",
        )
        return_message += "Plot is a bar type."
    except AssertionError as error:
        return_message += str(error)

    try:
        needed_title_words = [["Boulder"], ["average", "mean"], ["month"], ["precip"]]
        plot_test.assert_title_contains(
            strings_expected=needed_title_words,
            message_default="Please make sure that the title contains all needed keywords specified in the instructions",
        )
        return_message += "\nPlot has all of the needed keywords in the title."
    except AssertionError as error:
        return_message += "\n" + str(error)

    try:
        needed_xaxis_words = ["month"]
        plot_test.assert_axis_label_contains(
            axis="x",
            strings_expected=needed_xaxis_words,
            message_default="Please make sure that the x axis contains all needed keywords specified in the instructions",
        )
        return_message += "\nPlot has all of the needed keywords in the x axis."
    except AssertionError as error:
        return_message += "\n" + str(error)

    try:
        needed_yaxis_words = [["precip"], ["mm", "millimeters"]]
        plot_test.assert_axis_label_contains(
            axis="y",
            strings_expected=needed_yaxis_words,
            message_default="Please make sure that the y axis contains all needed keywords specified in the instructions",
        )
        return_message += "\nPlot has all of the needed keywords in the y axis."
    except AssertionError as error:
        return_message += "\n" + str(error)

    return return_message
