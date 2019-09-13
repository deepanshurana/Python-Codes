"""
There are two kinds of errors: SyntaxError and Exceptions.
Even if the statement or expression is syntactically correct,it may cause
an error when an attempt is made to execute it.

It is possible to handle selected exceptions. (using try and except)
firstly, the try clause is executed. If no exceptions, then except clause
is skipped and try statement is finished.

The finally clause runs whether or not the try statement produces an exception.
Following are the two examples.

"""


def divide(x, y):
    try:
        res = x / y
    except ZeroDivisionError:
        print("Divisible By Zero. Exception handled.", end='\n')

    else:
        print("RESULT: ", res)

    finally:
        print("FINALLY... I ALWAYS WORK, NO MATTER WHAT.")


def main():
    divide(2, 1)
    divide(2, 0)
    # divide("2", "1")
    # for this program with string I/P to work, use bare except clause,
    # this will handle any kind of exception occurance.


if __name__ == "__main__":
    main()
