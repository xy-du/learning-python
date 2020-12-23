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
