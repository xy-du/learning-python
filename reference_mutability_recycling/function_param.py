# Function Parameter as References
#  Python uses a mechanism, which is known as "Call-by-Object", sometimes also called "Call by Object Reference" or
#  "Call by Sharing".
# If you pass immutable arguments like integers, strings or tuples to a function, the passing acts like call-by-value.
# The object reference is passed to the function parameters. They can't be changed within the function, because they
# can't be changed at all, i.e. they are immutable.
# It's different, if we pass mutable arguments. They are also passed by object reference, but they can be changed
# in place in the function.
# If we pass a list to a function, we have to consider two cases: Elements of a list can be changed in place,
# i.e. the list will be changed even in the caller's scope. If a new list is assigned to the name, the old list will
# not be affected, i.e. the list in the caller's scope will remain untouched.

# when pass integer variables, The parameter inside of the function remains a reference to the arguments  variable,
# as long as the parameter is not changed. As soon as a new value will be assigned to it, Python creates a separate
# local variable. The caller's variable will not be changed this way.
# This means that Python initially behaves like call-by-reference, but as soon as we are changing the value of such
# a variable, Python "switches" to call-by-value.

def f(a, b):
    a += b
    return a


x = 1
y = 2
print(f(x, y))
print(x, y)  # unchanged
a = [1, 2]
b = [3, 4]
print(f(a, b))  # a is changed
print(a, b)
t = (10, 20)
u = (30, 40)
print(f(t, u))
print(t, u)  # unchanged
