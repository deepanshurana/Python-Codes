"""
RETURNING FUNCTION FROM A FUNCTION.
"""
def name(name="Deepanshu"):
    print("INSIDE NAME() FUNCTION!")
    print("--"*25)

    def greet():
        return("Hello From greet() fn.")

    def welcome():
        return("Welcome... From welcome() fn.")
    print("--"*25)
    print("NAME() FUNCTION ENDED.")
    if name == 'Deepanshu':
        return greet
    else:
        return welcome


name()
x = name()  # return value from name() assigned to x
print(x())  # prints the function contents.
print(x)    # prints : <function name.<locals>.greet at <address>>.


"""
PASSING FUNCTION AS AN ARGUMENT.
"""


def hello():
    return "HI, DEEPANSHU."


def other(func):
    print("HELLO")
    print(func())


other(hello)


# Creating Decorator.

def newDecorator(func):

    def wrapFn():
        print("CODE HERE BEFORE EXECUTING FUNCTION. (Wrapper fn.)")
        print('-'*10)
        func()
        print("FUNC() has been called")
        print('-'*10)
    return wrapFn


def functionNeedsDecorator():
    print("This function is in the need of a decorator.")


# reassigning function.


functionNeedsDecorator = newDecorator(functionNeedsDecorator)
functionNeedsDecorator()
# using '@' keyword.

@newDecorator
def functionDec():
    print(" THIS FUNCTION IS IN NEED OF A DECORATOR. ")


functionDec()
