s = 'café'

print(len(s))
print([c for c in s])
s_code = s.encode('utf-8')
print(s_code)
print(len(s_code))
print(s_code.decode('utf-8'))

# the only sequence type where s[0] == s[:1]  is str.
# for every other sequence type ,s[i] returns one item, and s[i:i+1] returns a sequence of the same type with the s[1]
# item inside it.
tp = (1, 2, 4)
print(tp[:1])
ls = [1, 2, 3]
print(ls[:1])
str = 'this'
print(str[:1])

# bytes and bytearray support every str method except a few others that do format and depend on Unicode data
# regular expresion in re module can also be supported is the regex is compiled from binary sequence instead of a str
s_code = s_code.upper()
print(s_code)
print(s_code.isascii())
print(s_code.decode('utf8'))

# formhex is the method that only Binary sequence have and str don't
# byte or bytearray can be built:
# fromhex
# constructor: str and encode method
# constructor: iterable of which items are in range of 0~255
# constructor: a single int, create a sequence of that size with null byte
bf = bytes.fromhex('31 4B CE A9')
print(bf)
print(bf.decode())
