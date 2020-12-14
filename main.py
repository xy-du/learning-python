firstname = 'austin'
lastname = 'duke'
print(f"{firstname} {lastname}")

fullname = f"{firstname} {lastname}"
print(f"hello, {fullname.title()}. Welcome!!!")

# the f-string is only begin with python 3.6, so for early version, you have to use format(), like bellow
# fullname = "{} {}".format(firstname, lastname)
# print(fullname)

space_str = ' python '
print('-', space_str.rstrip(), '-')
print('-', space_str.lstrip(), '-')
print('-', space_str.strip(), '-')
print('-', space_str, '-')  # only return changed values, no change happens to the original one.
space_str = space_str.strip()
print('-', space_str, '-')

# \t a tab, \n a newline
print('\tpython')
print('\npython')
print('\n\tpython')

# attention to syntax error, if you want use apostrophe in a string, make sure use double quote to quote it
print("this is dick's house")

# use % to do the string formation <format_string> % <values>
# if there are multiple values, they have to be enclosed in a tuple
line = '%d %s cost $%.2f' % (6, 'bananas', 1.74)
print(line)
# if there is only one value, it doesn't have to be enclosed
line = '%d is a number' % 10
print(line)
