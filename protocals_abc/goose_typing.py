# the shortage of duck typing:

# first, take the following three class for example.
# Clearly, the mere existence of a method called draw, callable without
# arguments, is far from sufficient to assure us that two objects x and
# y such that x.draw() and y.draw() can be called are in any way exchangeable
# or abstractly equivalent—nothing about the similarity of the semantics
# resulting from such calls can be inferred. Rather, we need a knowledgeable
# programmer to somehow positively assert that such an equivalence holds at some level

# isinstance and issubclass is against duck typing, since it requires the test subject
# must be a certain type, and this  limitation is against the flexibility that duck typing
# is trying to bring out

class Artist:
    def draw(self):
        pass


class Gunslinger:
    def draw(self):
        pass


class Lottery:
    def draw(self):
        pass

# goose typing:

# isinstance(obj, cls) is now just fine, as long as cls is an abstract base class.
# because goose typing brings more flexibility to it.

# inheriting from an ABC is more than implementing the required methods:
# it’s also a clear declaration of intent by the developer.
# That intent can also be made explicit through registering a virtual subclass.

# whenever you’re implementing a class embodying any of the concepts represented
# in the ABCs in numbers, collections.abc, or other framework you may be using,
# be sure (if needed) to subclass it from, or register it into, the corresponding ABC.
# At the start of your programs using some library or framework defining classes which
# have omitted to do that, perform the registrations yourself;
# then, when you must check for (most typically) an argument being, e.g, “a sequence,” check whether:
# isinstance(the_arg, collections.abc.Sequence)

# don’t define custom ABCs (or metaclasses) in production code， thought you can do that.

# even with ABCs, you should beware that excessive use of isinstance checks may be a code
# smell—a symptom of bad OO design

# 3 ways to make a subclass:
#   by inherit
#   by register
#   sometime by just implement a certain method, it will be aware as a subclass, see __len__ and abc.Sized
