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

# about literal displays of bytes. three three of them
# ASCII :  just display the character
# tab,newline,carriage return, and \   :    \t,\n,\r etc.
# other byte value:   hexadecimal escape sequence is used e.g., \x0041
for codec in ['latin_1', 'utf_8', 'utf_16']:
    print(codec, 'El Niño'.encode(codec), sep='\t')

# Encode/Decode Problem
# three kinds of code error: UnicodeEncodeError UnicodeDecodeError SyntaxError

print('+++++++++++++++++++++++++++++++++++++')
# copy with UnicodeEncodeError
# most non-UTF codecs are just a small set of unicode, so when the encode can not be handled, UnicodeEncodeError occur
city = 'São Paulo'
print(city.encode('utf-8'))
print(city.encode('utf-16'))
print(city.encode('iso8859_1'))
# print(city.encode('cp437'))  # UnicodeEncodeError: 'charmap' codec can't encode character '\xe3' in position 1...
# below is how you deal with it
print(city.encode('cp437', errors='ignore'))  # just not showing it
print(city.encode('cp437', errors='replace'))  # replace it with a ? mark
print(city.encode('cp437', errors='xmlcharrefreplace'))  # replace with an xml entity

print('+++++++++++++++++++++++++++++++++++++')
# not every byte holds a valid ASCII character and not every byte sequence is valid UTF8 or UTF16
# when the decode can not complete, the UnicodeDecodeError will show
# BUT, legacy 8-bit encodings like 'cp1252' 'iso8859_1' 'koi8_r'  are able to decode any stream of bytes, so valid
# characters will just become noise
octets = b'Montr\xe9al'
print(octets.decode('cp1252'))
print(octets.decode('iso_8859_7'))
print(octets.decode('koi8_r'))
# print(octets.decode('utf8')) # UnicodeDecodeError
print(octets.decode('utf8', errors='replace'))  # replace by � (Official unicode replacement character)

# SyntaxError happen when loading Modules
# python3 using UTF-8 as the default source encoding
# python2 using ASCII as the default
# if you load some .py module containing non-utf8 data and no encoding declaration, you may get SyntaxError
# To fix this problem, add a magic coding comment at the top of the file. NOTE: the # is needed
#  # coding: cp1252


# how to discover the encoding of a byte sequence
# Chardet---- the Universal Character Encoding Detector

# BOM - byte-order mark
# used at the begining of the bytes in utf16 format
# not recommend and should not used in utf8 bytes, but you might encounter that
# since UTF8 if bytes oriented, so not BOM is not needed, since no matter big or little-indian is the machine
# the sequence of the bytes will be the same. see the video below to know how utf8 works
# https://www.youtube.com/watch?v=tbdym9ZtepQ


print('+++++++++++++++++++++++++++++++++++++')
# the encoding parameter in two open below can be omitted, but that is not the best practice from the encode/decode
# perspective, since it will only work fine because I am using OSX which utf8 is the default encoding format
f1 = open('text_byte.txt', 'w', encoding='utf-8')
f1.write('café')
f1.close()
f2 = open('text_byte.txt', encoding='utf-8')
print(f2.read())

print('+++++++++++++++++++++++++++++++++++++')
# if you run the flowing digest on windows, you will get different output since windows use different encoding under
# different circumstances, which is painful. BUT, you can always ease lots of pains when you are explicit about the
# encodings in you programs
import sys

expressions = """
        locale.getpreferredencoding()
        type(my_file)
        my_file.encoding
        sys.stdout.isatty()
        sys.stdout.encoding
        sys.stdin.isatty()
        sys.stdin.encoding
        sys.stderr.isatty()
        sys.stderr.encoding
        sys.getdefaultencoding()
        sys.getfilesystemencoding()
    """

my_file = open('dummy', 'w')
sys.stdout.isatty()
for expression in expressions.split():
    value = eval(expression)
    print(expression.rjust(30), '->', repr(value))
