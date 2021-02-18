# else can not only be used with if, but also with for, while, and try

# for
# The else block will run only if and when the for loop runs to
# completion (i.e., not if the for is aborted with a break).
# while
# The else block will run only if and when the while loop exits
# because the condition became falsy (i.e., not when the while is aborted with a break).
# try
# The else block will only run if no exception is raised in
# the try block. The official docs also state: “Exceptions in
# the else clause are not handled by the preceding except clauses.


# take the try/else block for example, what is the meaning for this 'meaningless' approach?

def dangerous_call():
    print('here is the dangeraous call')


def after_call():
    print('here is the after call')


try:
    dangerous_call()
    after_call()
except OSError:
    print('OSError ...')
# here only the dangerous call is possible to raise the exception that
# you expect, so put after_call in it is for no good reason
try:
    dangerous_call()
except OSError:
    print('OSError ...')
else:
    after_call()
# this is much more clear, try block is guarding against possible
# errors in dangerous_call() and not in after_call(). It’s also
# more obvious that after_call() will only execute if no exceptions
# are raised in the try block.

# EAFP
# Easier to ask for forgiveness than permission.
# This common Python coding style assumes the existence of valid keys
# or attributes and catches exceptions if the assumption proves false.
# This clean and fast style is characterized by the presence of many try
# and except statements. The technique contrasts with the LBYL style common
# to many other languages such as C.

# LBYL
# Look before you leap.
# This coding style explicitly tests for pre-conditions before making
# calls or lookups. This style contrasts with the EAFP approach and is
# characterized by the presence of many if statements. In a multi-threaded
# environment, the LBYL approach can risk introducing a race condition
# between “the looking” and “the leaping”. For example, the code, if key
# in mapping: return mapping[key] can fail if another thread removes key from
# mapping after the test, but before the lookup. This issue can be solved with
# locks or by using the EAFP approach.
