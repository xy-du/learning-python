# The numbers package defines the so-called “numerical tower”
# (i.e., this linear hierarchy of ABCs), where Number is the topmost
# superclass, Complex is its immediate subclass, and so on, down to Integral
# Number
# Complex
# Real
# Rational
# Integral

# If you need to check for an integer
# use isinstance(x, numbers.Integral)
# It accept int, bool (which subclasses int) or other integer types register their types with the numbers ABCs.
# After registering any compatible type as a virtual subclass of numbers.Integral. this check can be satisfied

# likewise
# isinstance(x, numbers.Real)
# bool, int, float, fractions.Fraction,
# or any other noncomplex numerical type provided by an external library, such as NumPy, which is suitably registered.
