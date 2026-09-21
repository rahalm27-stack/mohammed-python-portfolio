"""
Calculator Assignment
==========================================================

YOUR MISSION: Complete the calculator functions below!

Each function has specific requirements that you must implement.
Read the docstrings and requirements carefully before coding.

HOW TO WORK ON THIS FILE:
- Complete ONE function at a time, top to bottom.
- After each function, save the file and run it:  python calculator_assignment.py
- The test suite at the bottom runs automatically and tells you exactly what
  passed, what failed, and what it expected instead.
- Keep going until every function reports a full score.

RESOURCES YOU CAN USE:
- Python arithmetic operators: +, -, *, /, %, **
- Conditional statements: if, elif, else
- Loops: while, for
- Built-in functions: abs(), int(), float()

TWO THINGS TO KNOW BEFORE YOU START:
1. The tests pass in floats (5.0, not 5), because get_number() returns floats.
   That is why the examples show "5.0 + 3.0 = 8.0" instead of "5 + 3 = 8".
2. Your printed output has to match the required format. The tests ignore
   blank lines and leading/trailing spaces, but everything else must match.
"""


def addition(a, b):
    """
    Add two numbers together and display the result.

    *** THIS ONE IS DONE FOR YOU AS A WORKED EXAMPLE. ***
    Study it -- every other function follows the same three-step shape:
    calculate, print, return.

    Parameters:
    a (float): First number
    b (float): Second number

    Returns:
    float: Sum of a and b

    REQUIREMENTS:
    1. Calculate the sum of a and b
    2. Print the result in the format: "a + b = result"
    3. Return the calculated sum

    EXAMPLE:
    addition(5.0, 3.0) should print: "5.0 + 3.0 = 8.0" and return 8.0
    """
    result = a + b

    print(str(a) + " + " + str(b) + " = " + str(result))

    return result


def subtraction(a, b):
    """
    Subtract the second number from the first number.

    Parameters:
    a (float): First number (minuend)
    b (float): Second number (subtrahend)

    Returns:
    float: Difference of a and b

    REQUIREMENTS:
    1. Calculate a minus b
    2. Print the result in the format: "a - b = result"
    3. Return the calculated difference

    EXAMPLE:
    subtraction(10.0, 4.0) should print: "10.0 - 4.0 = 6.0" and return 6.0
    """
    result = a - b
    print(str(a) + " - " + str(b) + " = " + str(result))
    return result


def multiplication(a, b):
    """
    Multiply two numbers together.

    Parameters:
    a (float): First number
    b (float): Second number

    Returns:
    float: Product of a and b

    REQUIREMENTS:
    1. Calculate the product of a and b
    2. Print result using the × symbol: "a × b = result"
    3. Return the calculated product

    EXAMPLE:
    multiplication(6.0, 7.0) should print: "6.0 × 7.0 = 42.0" and return 42.0

    HINT: Copy the × symbol straight out of this docstring so you know it is
    the right character.
    """
    result = a * b
    print(str(a) + " × " + str(b) + " = " + str(result))
    return result


def division(a, b):
    """
    Divide the first number by the second number.

    Parameters:
    a (float): Dividend (number being divided)
    b (float): Divisor (number dividing by)

    Returns:
    float: Quotient of a divided by b, or None if division by zero

    REQUIREMENTS:
    1. Check if b is zero - if so, print error message and return None
    2. If valid, calculate a divided by b
    3. Print result using the ÷ symbol: "a ÷ b = result"
    4. Return the calculated quotient

    ERROR MESSAGE: "Error: Cannot divide by zero!"

    EXAMPLES:
    division(15.0, 3.0) should print: "15.0 ÷ 3.0 = 5.0" and return 5.0
    division(10.0, 0.0) should print: "Error: Cannot divide by zero!" and return None

    HINT: Check for the zero FIRST and return early. Only the divisor (b)
    causes an error -- 0.0 ÷ 5.0 is a perfectly good calculation.
    """
    if b == 0:
        print("Error: Cannot divide by zero!")
        return None

    result = a / b
    print(str(a) + " ÷ " + str(b) + " = " + str(result))
    return result


def modulo(a, b):
    """
    Find the remainder when first number is divided by second number.

    Parameters:
    a (float): Dividend
    b (float): Divisor

    Returns:
    float: Remainder of a divided by b, or None if division by zero

    REQUIREMENTS:
    1. Check if b is zero - if so, print error message and return None
    2. If valid, calculate a mod b (remainder)
    3. Print result: "a mod b = result"
    4. Print explanation: "(This means a ÷ b leaves a remainder of result)"
    5. Return the calculated remainder

    ERROR MESSAGE: "Error: Cannot find remainder when dividing by zero!"

    EXAMPLES:
    modulo(17.0, 5.0) should print:
    "17.0 mod 5.0 = 2.0"
    "(This means 17.0 ÷ 5.0 leaves a remainder of 2.0)"
    and return 2.0
    """
    if b == 0:
        print("Error: Cannot find remainder when dividing by zero!")
        return None

    result = a % b
    print(str(a) + " mod " + str(b) + " = " + str(result))
    print("(This means " + str(a) + " ÷ " + str(b) + " leaves a remainder of " + str(result) + ")")
    return result


def exponentiation(a, b):
    """
    Raise the first number to the power of the second number.

    Parameters:
    a (float): Base number
    b (float): Exponent (power)

    Returns:
    float: a raised to the power of b

    REQUIREMENTS:
    1. Calculate a to the power of b
    2. Print result using the ^ symbol: "a^b = result"
    3. Return the calculated result

    EXAMPLE:
    exponentiation(2.0, 3.0) should print: "2.0^3.0 = 8.0" and return 8.0

    HINT: Use the ** operator for exponentiation. Note there are NO spaces
    around the ^ in the printed output.
    """
    result = a ** b
    print(str(a) + "^" + str(b) + " = " + str(result))
    return result


def greatest_common_factor(a, b):
    """
    Find the Greatest Common Factor (GCF) of two numbers using the Euclidean algorithm.

    Parameters:
    a (int): First number
    b (int): Second number

    Returns:
    int: Greatest Common Factor of a and b

    REQUIREMENTS:
    1. Convert inputs to positive integers using int(abs(a)) and int(abs(b))
    2. Print the opening line: "Finding GCF of original_a and original_b:"
    3. Handle special cases: if a is 0, return b; if b is 0, return a
    4. Use the Euclidean algorithm:
       - While b is not zero:
         - Calculate remainder = a % b
         - Print step: "Step X: a = b × (a // b) + remainder"
         - Set a = b, then b = remainder
         - Continue until b becomes 0
    5. Print final result: "GCF of original_a and original_b = final_a"
    6. Return the GCF (final value of a)

    EXAMPLE:
    greatest_common_factor(48, 18) should print:
    "Finding GCF of 48 and 18:"
    "  Step 1: 48 = 18 × 2 + 12"
    "  Step 2: 18 = 12 × 1 + 6"
    "  Step 3: 12 = 6 × 2 + 0"
    "GCF of 48 and 18 = 6"
    and return 6

    HINT: Save the original values before starting the algorithm for display.
    You will also want a step counter that starts at 1 and grows by 1 each
    time through the loop.
    """
    original_a = a
    original_b = b
    a = int(abs(a))
    b = int(abs(b))

    print("Finding GCF of " + str(original_a) + " and " + str(original_b) + ":")

    if a == 0:
        print("GCF of " + str(original_a) + " and " + str(original_b) + " = " + str(b))
        return b
    if b == 0:
        print("GCF of " + str(original_a) + " and " + str(original_b) + " = " + str(a))
        return a

    step = 1
    while b != 0:
        remainder = a % b
        print("Step " + str(step) + ": " + str(a) + " = " + str(b) + " × " + str(a // b) + " + " + str(remainder))
        a = b
        b = remainder
        step += 1

    print("GCF of " + str(original_a) + " and " + str(original_b) + " = " + str(a))
    return a


def get_number(prompt):
    """
    Get a valid number from the user with error handling.

    Parameters:
    prompt (str): Message to show the user

    Returns:
    float: Valid number entered by user

    REQUIREMENTS:
    1. Use a while loop that continues until valid input is received
    2. Use input(prompt) to get user input
    3. Use try-except to catch ValueError when converting to float
    4. If invalid input, print: "Invalid input! Please enter a valid number."
    5. Return the valid float value when successfully converted

    EXAMPLE INTERACTION:
    >>> get_number("Enter a number: ")
    Enter a number: abc
    Invalid input! Please enter a valid number.
    Enter a number: 5.5
    (returns 5.5)

    HINT: Make sure you return a float, not the string the user typed.
    """
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def display_menu():
    """
    Display the calculator menu options in a formatted way.

    *** THIS ONE IS DONE FOR YOU. *** Do not change it -- the tests check it
    character for character, and calculator() depends on it.

    Returns:
    None

    EXACT FORMAT REQUIRED:
    ==================================================
    PYTHON CALCULATOR
    ==================================================
    Choose an operation:
    1. Addition (+)
    2. Subtraction (-)
    3. Multiplication (×)
    4. Division (÷)
    5. Modulo/Remainder (%)
    6. Exponentiation (^)
    7. Greatest Common Factor (GCF)
    8. Quit
    --------------------------------------------------
    """
    print(
        "==================================================\n"
        "PYTHON CALCULATOR\n"
        "==================================================\n"
        "Choose an operation:\n"
        "1. Addition (+)\n"
        "2. Subtraction (-)\n"
        "3. Multiplication (×)\n"
        "4. Division (÷)\n"
        "5. Modulo/Remainder (%)\n"
        "6. Exponentiation (^)\n"
        "7. Greatest Common Factor (GCF)\n"
        "8. Quit\n"
        "--------------------------------------------------\n"
    )


def calculator():
    """
    Main calculator function - the heart of the program!

    This function should handle all user interaction and call other functions.

    Returns:
    None

    REQUIREMENTS:
    1. Print welcome message: "Welcome to the Python Calculator!"
    2. Use a while loop to keep the program running until user quits
    3. In each iteration:
       a. Call display_menu() to show options
       b. Get user's menu choice (1-8) with input()
       c. Validate the choice - if invalid, show error and continue
       d. If choice is 8, print goodbye message and break the loop
       e. Get two numbers from user using get_number()
          - For GCF (choice 7): mention it needs whole numbers
          - For other operations: get any numbers
       f. Call the appropriate function based on user's choice
       g. Ask if user wants to continue: "Would you like to perform another calculation? (yes/no): "
       h. If answer is not yes/y/yeah/yep, break the loop

    MENU CHOICE VALIDATION:
    - Only accept choices '1' through '8'
    - For invalid choices, print: "Invalid choice! Please enter a number between 1 and 8."

    GOODBYE MESSAGES:
    - When user chooses 8: "Thank you for using the Python Calculator! \nGoodbye!"
    - When user chooses not to continue: "Thank you for using the Python Calculator!"

    HINT: Use if-elif-else statements to call the right function:
    if choice == '1':
        addition(num1, num2)
    elif choice == '2':
        subtraction(num1, num2)
    # ... and so on

    HINT: The menu choice comes from input() directly, so it is a STRING.
    Compare it to '1', not to 1.
    """
    print("Welcome to the Python Calculator!")

    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ")

        if choice not in ['1', '2', '3', '4', '5', '6', '7', '8']:
            print("Invalid choice! Please enter a number between 1 and 8.")
            continue

        if choice == '8':
            print("Thank you for using the Python Calculator! \nGoodbye!")
            break

        if choice == '7':
            print("GCF requires whole numbers.")
            num1 = get_number("Enter the first number: ")
            num2 = get_number("Enter the second number: ")
            greatest_common_factor(num1, num2)
        else:
            num1 = get_number("Enter the first number: ")
            num2 = get_number("Enter the second number: ")

            if choice == '1':
                addition(num1, num2)
            elif choice == '2':
                subtraction(num1, num2)
            elif choice == '3':
                multiplication(num1, num2)
            elif choice == '4':
                division(num1, num2)
            elif choice == '5':
                modulo(num1, num2)
            elif choice == '6':
                exponentiation(num1, num2)

        answer = input("Would you like to perform another calculation? (yes/no): ")
        if answer.lower() not in ['yes', 'y', 'yeah', 'yep']:
            print("Thank you for using the Python Calculator!")
            break


# ===================================================================
# TESTING CODE - DO NOT MODIFY THIS SECTION!
# ===================================================================
#
# HOW TO READ THE RESULTS:
#   [OK] means that check passed.
#   [X]  means it failed -- the line underneath shows what was expected,
#        what your code actually did, and a hint about how to fix it.
#
# IF THE TESTS SEEM TO FREEZE: press Ctrl+C. That almost always means one of
# your while loops never ends. Look at what is supposed to make it stop.
#
# IF YOU SEE A UnicodeEncodeError ABOUT × OR ÷: your terminal cannot print
# those symbols. Try running the file from VS Code's terminal instead.

import builtins
import io
from contextlib import redirect_stdout

_SCORES = {}
_ORDER = []
_GROUP = [""]


class _OutOfInput(BaseException):
    """Raised by the test harness when a function asks for more input than the
    test scripted. Almost always means a loop is not stopping when it should."""


def _section(title):
    """Start a new group of checks."""
    _GROUP[0] = title
    if title not in _SCORES:
        _SCORES[title] = [0, 0]
        _ORDER.append(title)
    print("\n" + title)
    print("-" * 68)


def _run(func, args=(), inputs=None):
    """Call a student function, capturing everything it prints.

    Returns (return_value, printed_lines, error_text_or_None).
    If `inputs` is given, input() is replaced by a script of canned answers.
    """
    buffer = io.StringIO()
    real_input = builtins.input
    if inputs is not None:
        queue = list(inputs)
        calls = [0]

        def fake_input(prompt=""):
            print(prompt, end="")
            calls[0] += 1
            if calls[0] > 40 or not queue:
                raise _OutOfInput("your function kept asking for more input")
            return queue.pop(0)

        builtins.input = fake_input
    try:
        with redirect_stdout(buffer):
            value = func(*args)
        error = None
    except _OutOfInput as stop:
        value, error = None, str(stop)
    except Exception as problem:
        value, error = None, type(problem).__name__ + ": " + str(problem)
    finally:
        builtins.input = real_input
    return value, buffer.getvalue().splitlines(), error


def _tidy(lines):
    """Ignore blank lines and leading/trailing spaces when comparing output."""
    return [line.strip() for line in lines if line.strip() != ""]


def _pass(label):
    _SCORES[_GROUP[0]][0] += 1
    _SCORES[_GROUP[0]][1] += 1
    print("  [OK] " + label)


def _fail(label, detail, hint):
    _SCORES[_GROUP[0]][1] += 1
    print("  [X]  " + label)
    for line in detail:
        print("       " + line)
    print("       hint: " + hint)


def check_value(label, got, expected, hint, error=None, approx=False):
    """Check the value a function RETURNS."""
    if error:
        _fail(label, ["your code stopped with " + error], hint)
        return
    if got is None and expected is not None:
        _fail(label, ["expected " + repr(expected) + ", got None",
                      "(None usually means the function has no return statement yet)"], hint)
        return
    if approx:
        try:
            ok = abs(got - expected) < 1e-9
        except TypeError:
            ok = False
    else:
        ok = got == expected and isinstance(got, type(expected))
    if ok:
        _pass(label)
    else:
        _fail(label, ["expected " + repr(expected) + ", got " + repr(got)], hint)


def check_prints(label, printed, expected, hint, error=None):
    """Check the lines a function PRINTS, in order."""
    if error:
        _fail(label, ["your code stopped with " + error], hint)
        return
    actual = _tidy(printed)
    wanted = _tidy(expected)
    if actual == wanted:
        _pass(label)
        return
    detail = []
    for index in range(max(len(actual), len(wanted))):
        mine = actual[index] if index < len(actual) else "(nothing printed)"
        theirs = wanted[index] if index < len(wanted) else "(nothing expected)"
        if mine != theirs:
            detail.append("line " + str(index + 1) + " expected: " + theirs)
            detail.append("line " + str(index + 1) + " you had:  " + mine)
            break
    if not detail:
        detail.append("expected " + str(len(wanted)) + " lines, printed " + str(len(actual)))
    _fail(label, detail, hint)


def check_contains(label, printed, snippet, hint, error=None):
    """Check that SOMETHING in the output contains a required piece of text."""
    if error:
        _fail(label, ["your code stopped with " + error], hint)
        return
    if any(snippet in line for line in printed):
        _pass(label)
    else:
        _fail(label, ["nothing printed contained: " + snippet], hint)


def test_addition():
    _section("addition()  -- worked example, these should already pass")
    value, printed, error = _run(addition, (5.0, 3.0))
    check_value("addition(5.0, 3.0) returns 8.0", value, 8.0,
                "Calculate, print, then return the result.", error)
    check_prints("addition(5.0, 3.0) prints correctly", printed,
                 ["5.0 + 3.0 = 8.0"],
                 "Format is: a + b = result", error)

    value, printed, error = _run(addition, (-4.0, 4.0))
    check_value("negatives: addition(-4.0, 4.0) returns 0.0", value, 0.0,
                "Nothing special needed -- + handles negatives.", error)

    value, printed, error = _run(addition, (0.1, 0.2))
    check_value("float accuracy: 0.1 + 0.2 is about 0.3", value, 0.3,
                "Computers store 0.1 as a tiny bit off, so you get "
                "0.30000000000000004. That is normal, not a bug in your code.",
                error, approx=True)


def test_subtraction():
    _section("subtraction()")
    value, printed, error = _run(subtraction, (10.0, 4.0))
    check_value("subtraction(10.0, 4.0) returns 6.0", value, 6.0,
                "Return a - b, in that order.", error)
    check_prints("subtraction(10.0, 4.0) prints correctly", printed,
                 ["10.0 - 4.0 = 6.0"],
                 "Format is: a - b = result", error)

    value, printed, error = _run(subtraction, (3.0, 10.0))
    check_value("negative result: subtraction(3.0, 10.0) returns -7.0", value, -7.0,
                "Do not use abs() -- a smaller minus a bigger really is negative.", error)
    check_prints("negative result prints correctly", printed,
                 ["3.0 - 10.0 = -7.0"],
                 "Print the result exactly as Python calculates it.", error)

    value, printed, error = _run(subtraction, (7.0, 7.0))
    check_value("edge case: subtraction(7.0, 7.0) returns 0.0", value, 0.0,
                "A number minus itself is zero.", error)


def test_multiplication():
    _section("multiplication()")
    value, printed, error = _run(multiplication, (6.0, 7.0))
    check_value("multiplication(6.0, 7.0) returns 42.0", value, 42.0,
                "Return the product.", error)
    check_prints("multiplication(6.0, 7.0) prints correctly", printed,
                 ["6.0 × 7.0 = 42.0"],
                 "Use the × symbol, not the letter x and not *.", error)

    value, printed, error = _run(multiplication, (5.0, 0.0))
    check_value("edge case: anything × 0 returns 0.0", value, 0.0,
                "Zero times anything is zero -- no special case needed.", error)

    value, printed, error = _run(multiplication, (-3.0, -4.0))
    check_value("two negatives: multiplication(-3.0, -4.0) returns 12.0", value, 12.0,
                "Negative times negative is positive.", error)


def test_division():
    _section("division()")
    value, printed, error = _run(division, (15.0, 3.0))
    check_value("division(15.0, 3.0) returns 5.0", value, 5.0,
                "Return the quotient.", error)
    check_prints("division(15.0, 3.0) prints correctly", printed,
                 ["15.0 ÷ 3.0 = 5.0"],
                 "Use the ÷ symbol, not / and not the word divided.", error)

    value, printed, error = _run(division, (10.0, 0.0))
    check_value("EDGE CASE: division(10.0, 0.0) returns None", value, None,
                "Check b == 0 first, print the error, and return None.", error)
    check_prints("division by zero prints the error message", printed,
                 ["Error: Cannot divide by zero!"],
                 "The message must match exactly, capital E and the ! included. "
                 "Do NOT also print an answer line.", error)

    value, printed, error = _run(division, (0.0, 5.0))
    check_value("EDGE CASE: division(0.0, 5.0) returns 0.0, not None", value, 0.0,
                "Only the DIVISOR being zero is an error. Zero divided by five "
                "is a normal calculation.", error)

    value, printed, error = _run(division, (7.0, 2.0))
    check_value("does not floor: division(7.0, 2.0) returns 3.5", value, 3.5,
                "Use / (true division), not // (floor division).", error)

    value, printed, error = _run(division, (-9.0, 3.0))
    check_value("negatives: division(-9.0, 3.0) returns -3.0", value, -3.0,
                "Nothing special needed for negatives.", error)


def test_modulo():
    _section("modulo()")
    value, printed, error = _run(modulo, (17.0, 5.0))
    check_value("modulo(17.0, 5.0) returns 2.0", value, 2.0,
                "Use the % operator.", error)
    check_prints("modulo(17.0, 5.0) prints BOTH required lines", printed,
                 ["17.0 mod 5.0 = 2.0",
                  "(This means 17.0 ÷ 5.0 leaves a remainder of 2.0)"],
                 "Two separate print statements: the result, then the "
                 "explanation in parentheses.", error)

    value, printed, error = _run(modulo, (10.0, 0.0))
    check_value("EDGE CASE: modulo(10.0, 0.0) returns None", value, None,
                "Check b == 0 first and return None.", error)
    check_prints("modulo by zero prints its own error message", printed,
                 ["Error: Cannot find remainder when dividing by zero!"],
                 "This message is DIFFERENT from the division one -- read the "
                 "docstring and copy it exactly.", error)

    value, printed, error = _run(modulo, (9.0, 3.0))
    check_value("EDGE CASE: modulo(9.0, 3.0) returns 0.0 (divides evenly)", value, 0.0,
                "A remainder of zero is a real answer, not an error.", error)

    value, printed, error = _run(modulo, (3.0, 7.0))
    check_value("smaller divided by bigger: modulo(3.0, 7.0) returns 3.0", value, 3.0,
                "7 goes into 3 zero times with 3 left over.", error)

    value, printed, error = _run(modulo, (-7.0, 3.0))
    check_value("EDGE CASE: modulo(-7.0, 3.0) returns 2.0 in Python", value, 2.0,
                "Surprising but correct: in Python the remainder takes the sign "
                "of the DIVISOR. Just use %, do not try to fix it.", error)


def test_exponentiation():
    _section("exponentiation()")
    value, printed, error = _run(exponentiation, (2.0, 3.0))
    check_value("exponentiation(2.0, 3.0) returns 8.0", value, 8.0,
                "Use ** -- note that ^ is a completely different operator in "
                "Python, even though we PRINT a ^.", error)
    check_prints("exponentiation(2.0, 3.0) prints correctly", printed,
                 ["2.0^3.0 = 8.0"],
                 "No spaces around the ^ in the printed line.", error)

    value, printed, error = _run(exponentiation, (5.0, 0.0))
    check_value("EDGE CASE: anything to the power 0 returns 1.0", value, 1.0,
                "** already knows this rule.", error)

    value, printed, error = _run(exponentiation, (2.0, -2.0))
    check_value("EDGE CASE: negative exponent 2.0^-2.0 returns 0.25", value, 0.25,
                "A negative exponent means one over the positive power.", error)

    value, printed, error = _run(exponentiation, (9.0, 0.5))
    check_value("EDGE CASE: 9.0^0.5 returns 3.0 (a square root)", value, 3.0,
                "Raising to the power of one half is the same as a square root.",
                error, approx=True)


def test_gcf():
    _section("greatest_common_factor()")
    value, printed, error = _run(greatest_common_factor, (48, 18))
    check_value("greatest_common_factor(48, 18) returns 6", value, 6,
                "Return the last non-zero value of a.", error)
    check_prints("the full step-by-step output matches", printed,
                 ["Finding GCF of 48 and 18:",
                  "Step 1: 48 = 18 × 2 + 12",
                  "Step 2: 18 = 12 × 1 + 6",
                  "Step 3: 12 = 6 × 2 + 0",
                  "GCF of 48 and 18 = 6"],
                 "Print the opening line first, then one line per loop pass "
                 "with a counter, then the final answer using the ORIGINAL "
                 "numbers you saved.", error)

    value, printed, error = _run(greatest_common_factor, (18, 48))
    check_value("order does not matter: (18, 48) also returns 6", value, 6,
                "The first pass through the loop swaps them for you -- no extra "
                "code needed.", error)

    value, printed, error = _run(greatest_common_factor, (0, 5))
    check_value("EDGE CASE: greatest_common_factor(0, 5) returns 5", value, 5,
                "Every number divides 0, so the answer is the other number.", error)

    value, printed, error = _run(greatest_common_factor, (5, 0))
    check_value("EDGE CASE: greatest_common_factor(5, 0) returns 5", value, 5,
                "If b is already 0 the loop never runs and a is the answer.", error)

    value, printed, error = _run(greatest_common_factor, (0, 0))
    check_value("EDGE CASE: greatest_common_factor(0, 0) returns 0", value, 0,
                "Both zero means the answer is 0. Make sure this does not crash "
                "or loop forever.", error)

    value, printed, error = _run(greatest_common_factor, (-48, 18))
    check_value("EDGE CASE: negatives, (-48, 18) returns 6", value, 6,
                "Requirement 1: convert with int(abs(a)) and int(abs(b)) before "
                "you start.", error)

    value, printed, error = _run(greatest_common_factor, (48.0, 18.0))
    check_value("EDGE CASE: floats in, whole number out -- (48.0, 18.0) returns 6",
                value, 6,
                "int(abs(a)) also handles the float-to-int conversion. The "
                "answer must be an int (6), not a float (6.0).", error)

    value, printed, error = _run(greatest_common_factor, (17, 5))
    check_value("EDGE CASE: no common factors, (17, 5) returns 1", value, 1,
                "Numbers with nothing in common share only the factor 1.", error)

    value, printed, error = _run(greatest_common_factor, (12, 12))
    check_value("EDGE CASE: same number twice, (12, 12) returns 12", value, 12,
                "A number's greatest factor is itself.", error)


def test_get_number():
    _section("get_number()  -- tested with pretend typing")
    value, printed, error = _run(get_number, ("Enter a number: ",), inputs=["7"])
    check_value("typing 7 returns the FLOAT 7.0, not the string '7'", value, 7.0,
                "Return float(user_input), not user_input.", error)

    value, printed, error = _run(get_number, ("Enter a number: ",), inputs=["5.5"])
    check_value("typing 5.5 returns 5.5", value, 5.5,
                "float() handles the decimal point for you.", error)

    value, printed, error = _run(get_number, ("Enter a number: ",), inputs=["-2.5"])
    check_value("EDGE CASE: typing -2.5 returns -2.5", value, -2.5,
                "Negative numbers are valid input -- do not reject them.", error)

    value, printed, error = _run(get_number, ("Enter a number: ",), inputs=["abc", "5.5"])
    check_value("EDGE CASE: bad input then good input returns 5.5", value, 5.5,
                "Your while loop must go around again instead of giving up or "
                "crashing.", error)
    check_contains("a bad entry prints the warning", printed,
                   "Invalid input! Please enter a valid number.",
                   "Print that exact message inside your except block.", error)

    value, printed, error = _run(get_number, ("Enter a number: ",),
                                 inputs=["", "hello", "12"])
    check_value("EDGE CASE: empty line and a word, then 12, returns 12.0", value, 12.0,
                "An empty string fails float() too, so the same except block "
                "catches it. Keep looping until something works.", error)


def test_display_menu():
    _section("display_menu()  -- provided for you, do not change it")
    value, printed, error = _run(display_menu)
    check_prints("the menu matches the required format exactly", printed,
                 ["==================================================",
                  "PYTHON CALCULATOR",
                  "==================================================",
                  "Choose an operation:",
                  "1. Addition (+)",
                  "2. Subtraction (-)",
                  "3. Multiplication (×)",
                  "4. Division (÷)",
                  "5. Modulo/Remainder (%)",
                  "6. Exponentiation (^)",
                  "7. Greatest Common Factor (GCF)",
                  "8. Quit",
                  "--------------------------------------------------"],
                 "If this fails you have edited display_menu(). Put it back.",
                 error)


def test_calculator():
    _section("calculator()  -- whole-program tests, save these for last")
    print("  (These need get_number() finished too. If everything above passes")
    print("   and these fail, the problem is inside calculator() itself.)")

    value, printed, error = _run(calculator, inputs=["8"])
    check_contains("starts with the welcome message", printed,
                   "Welcome to the Python Calculator!",
                   "Print it once, before the loop starts.", error)
    check_contains("choice 8 quits with a goodbye", printed, "Goodbye!",
                   "Choice '8' should print the goodbye message and break.", error)

    value, printed, error = _run(calculator, inputs=["9", "8"])
    check_contains("EDGE CASE: choice 9 is rejected, then 8 still quits", printed,
                   "Invalid choice! Please enter a number between 1 and 8.",
                   "Validate before doing anything else, then loop around "
                   "again instead of crashing.", error)

    value, printed, error = _run(calculator, inputs=["1", "5", "3", "no"])
    check_contains("EDGE CASE: a full add-then-stop session does the math", printed,
                   "5.0 + 3.0 = 8.0",
                   "Choice '1' should collect two numbers with get_number() and "
                   "pass them to addition().", error)
    check_contains("answering 'no' ends the program politely", printed,
                   "Thank you for using the Python Calculator!",
                   "Anything other than yes/y/yeah/yep should break the loop.",
                   error)

    value, printed, error = _run(calculator, inputs=["4", "10", "0", "no"])
    check_contains("EDGE CASE: dividing by zero inside the menu is handled", printed,
                   "Error: Cannot divide by zero!",
                   "calculator() does not need its own zero check -- division() "
                   "already handles it. It just must not crash.", error)


def test_your_functions():
    """
    Run every test and print a scorecard.
    This runs automatically when you run this file.
    """
    print("=" * 68)
    print("TESTING YOUR CALCULATOR FUNCTIONS")
    print("=" * 68)

    test_addition()
    test_subtraction()
    test_multiplication()
    test_division()
    test_modulo()
    test_exponentiation()
    test_gcf()
    test_get_number()
    test_display_menu()
    test_calculator()

    print("\n" + "=" * 68)
    print("SCORECARD")
    print("=" * 68)
    total_passed = 0
    total_checks = 0
    for name in _ORDER:
        passed, count = _SCORES[name]
        total_passed += passed
        total_checks += count
        short = name.split("  ")[0]
        mark = "DONE " if passed == count else "     "
        dots = "." * max(3, 34 - len(short))
        print(mark + short + " " + dots + " " + str(passed) + "/" + str(count))
    print("-" * 68)
    print("TOTAL: " + str(total_passed) + " of " + str(total_checks) + " checks passed")
    if total_passed == total_checks:
        print("\nEverything passes. Now try your calculator for real:")
        print("open a Python prompt, import this file, and run calculator().")
    else:
        print("\nWork on the FIRST function that is not finished, then run this")
        print("file again. Read the hint under each [X] -- it tells you what to fix.")
    print("=" * 68)


if __name__ == "__main__":
    test_your_functions()


# ===================================================================
# SUBMISSION CHECKLIST
# ===================================================================
"""
BEFORE SUBMITTING, MAKE SURE:
[ ] All functions have code (no 'pass' statements remaining)
[ ] Every check in the scorecard passes
[ ] All functions print output in the required format
[ ] Error handling works for division and modulo
[ ] GCF function shows the step-by-step process
[ ] get_number() handles invalid input gracefully
[ ] calculator() has a complete, working menu system
[ ] You ran calculator() yourself and tried several operations
[ ] Your code has comments explaining your logic

WHAT THIS ASSIGNMENT COVERS:
- Basic operations (add, subtract, multiply, exponent)
- Division and modulo with error handling
- GCF with the Euclidean algorithm
- get_number() with try/except error handling
- calculator() main function with a menu loop
- Code quality and comments
"""
