# high-order functions: a function that takes a a function as a argument or returns a function as the result.

def reverse(word):
    return word[::-1]


print(reverse('abcde'))

fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
# words in fruits list are not changed, only the reversed spelling is used
s_list = sorted(fruits, key=reverse)
print(s_list)
