# Distinguish Interface Inheritance from Implementation Inheritance
#   Inheritance of interface creates a subtype, implying an “is-a” relationship.
#   Inheritance of implementation avoids code duplication by reuse.

# Make Interfaces Explicit with ABCs
#   In modern Python, if a class is designed to define an interface,
#   it should be an explicit ABC. In Python ≥ 3.4, this means:
#   subclass abc.ABC or another ABC

# Use Mixins for Code Reuse
#   If a class is designed to provide method implementations for
#   reuse by multiple unrelated subclasses, without implying an
#   “is-a” relationship, it should be an explicit mixin class.
#   Conceptually, a mixin does not define a new type; it merely
#   bundles methods for reuse. A mixin should never be instantiated,
#   and concrete classes should not inherit only from a mixin. Each
#   mixin should provide a single specific behavior, implementing few
#   and very closely related methods.

# Make Mixins Explicit by Naming
# There is no formal way in Python to state that a class is a mixin,
# so it is highly recom‐ mended that they are named with a ...Mixin suffix.

# An ABC May Also Be a Mixin; The Reverse Is Not True
#   Because an ABC can implement concrete methods, it works as a mixin
#   as well. An ABC also defines a type, which a mixin does not. And an
#   ABC can be the sole base class of any other class, while a mixin
#   should never be subclassed alone except by another, more specialized
#   mixin—not a common arrangement in real code.
#   One restriction applies to ABCs and not to mixins: the concrete methods
#   implemented in an ABC should only collaborate with methods of the same
#   ABC and its superclasses.

# Don’t Subclass from More Than One Concrete Class
#   Concrete classes should have zero or at most one concrete superclass.
#   In other words, all but one of the superclasses of a concrete class
#   should be ABCs or mixins.

# Provide Aggregate Classes to Users
#   If some combination of ABCs or mixins is particularly useful
#   to client code, provide a class that brings them together
#   in a sensible way.

# Favor Object Composition Over Class Inheritance.
#
