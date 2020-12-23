s = 'café'

print(len(s))
print([c for c in s])
s_code = s.encode('utf-8')
print(s_code)
print(len(s_code))
print(s_code.decode('utf-8'))
