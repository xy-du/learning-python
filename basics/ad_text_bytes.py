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

# create a file named text_byte.txt, and put the word café into it
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

# this file will create automatically
my_file = open('dummy', 'w')
sys.stdout.isatty()
for expression in expressions.split():
    value = eval(expression)
    print(expression.rjust(30), '->', repr(value))

print('+++++++++++++++++++++++++++++++++++++')
# normalize unicode for 'normal' comparisons
# combining acute accent:
#   in unicode : é and \u0301 are 'canonical equivalent'
#   in python:  they are difference code point sequence, therefore is not equivalent
s1 = 'codé'
s2 = 'code\u0301'
print(s1, s2)
# print(bytes(s1, encoding='utf8'), bytes(s2, encoding='utf8'))
print(len(s1), len(s2))
print(s1 == s2)
# so how to compare them?
# Unicode Normalization!
# NFC: normalization form composition    produce shortest equivalent string
# NFD: normalization form decomposition   expandes composed character into base characters
from unicodedata import normalize

print(normalize('NFC', s1), normalize('NFC', s2))
print(len(normalize('NFC', s1)), len(normalize('NFC', s2)))
print(normalize('NFD', s1), normalize('NFD', s2))
print(len(normalize('NFD', s1)), len(normalize('NFD', s2)))
print(normalize('NFC', s1) == normalize('NFC', s2))
print(normalize('NFD', s1) == normalize('NFD', s2))

print('+++++++++++++++++++++++++++++++++++++')
# NFC may change the code for some characters, even they are visually same.
# so it's essential to normalize to avoid surprise
ohm = '\u2126'
print(ohm)
print(hex(ord(ohm)))
print(bytes(ohm, encoding='utf8'))
ohm_c = normalize('NFC', ohm)
print(ohm_c)
print(hex(ord(ohm_c)))
print(bytes(ohm_c, encoding='utf8'))
print(ohm == ohm_c)
print(normalize('NFC', ohm) == normalize('NFC', ohm_c))

print('+++++++++++++++++++++++++++++++++++++')
# some character may appear more than once in unicode for 'compatibility' reason, these character is considered
# 'compatibility character'
# e.g., 'μ' (U+00B5) (U+03BC)
# NFKD and NFKC
# K stands for 'compatibility'
# using this normalization form, compatibility character is replaced by 'compatibility decomposition' of one or more
# characters that are considered a 'preferred'  representation
# in the following case, 4² lost it's meaning in the transformation, so you have to be very careful when use NFKC,NFKD
# good places to use them is searching and indexing
half = '½'
print(normalize('NFKC', half))
print(normalize('NFKD', half))
four_square = '4²'
print(normalize('NFKC', four_square))

from unicodedata import name

micro = 'µ'
micro_kc = normalize('NFKC', micro)
print(micro, micro_kc)
print(hex(ord(micro)), hex(ord(micro_kc)))
print(name(micro), name(micro_kc))

print('+++++++++++++++++++++++++++++++++++++')
# Case Folding
# case folding is essentially converting all text to lowercase, with some exceptions
# str.casefold() new in python3.3
# python 4.4: there 116 character whose case folding form is difference lowcase() method return.
# here take Latin1 as a example, all the characters in latin1 returns
micro = 'µ'
print(name(micro))
micro_cf = micro.casefold()
print(name(micro_cf))
print(micro, micro_cf)
eszett = 'ß'
print(name(eszett))
eszett_cf = eszett.casefold()
# print(name(eszett_cf)) # this will get a error
print(eszett, eszett_cf)
print(micro.casefold() == micro_cf.casefold())

micro = '\u00b5'
micro2 = '\u03bc'
print(micro, micro2)
print(micro == micro2)
print(normalize('NFC', micro) == normalize('NFC', micro2))  # for compatible character, NFC can not do the work
print(normalize('NFKC', micro) == normalize('NFKC', micro2))  # NFKC is the choice for this situation
print(micro.casefold(), micro2.casefold())
print(hex(ord(micro.casefold())), hex(ord(micro2.casefold())))
print(micro.casefold() == micro2.casefold())  # seems casefold() can do it too

s1 = 'Codé'
s2 = 'code\u0301'
print(s1.casefold(), s2.casefold())
print(len(s1.casefold()), len(s2.casefold()))
# return False. so casefold is for single character,
# for composition and decomposition, NFC/NFD should be used.
print(s1.casefold() == s2.casefold())
# return False, so NFC can not resolve the lower or upper case issues
print(normalize('NFC', s1) == normalize('NFC', s2))
# All in All, maybe sometimes, it's necessary to combine NFC and casefold() to do the work
print(normalize('NFC', s1.casefold()) == normalize('NFC', s2.casefold()))

import unicodedata
import string


def shave_marks(str):
    str_nfd = normalize('NFD', str)
    str_shaved = ''.join(c for c in str_nfd
                         if not unicodedata.combining(c))
    return normalize('NFC', str_shaved)


# the most important logic below is that it assumes that the combining char is right behind the char it companies with
# you can use the έ in Ζέφυρος to try out the procedure in your mind
def shave_marks_latin(txt):
    str_nfd = normalize('NFD', txt)
    islatin = False  # considering the first char will never be a combining char
    keeper = []
    for c in str_nfd:
        if unicodedata.combining(c) and islatin:  # remove all the combining char for latin base
            continue
        keeper.append(c)
        if not unicodedata.combining(c):
            islatin = c in string.ascii_letters
    return normalize('NFC', ''.join(keeper))


# char-to-char, western character to ASCII
# if two arguments for maketrans, they are equal of length, return a char to char translation map
single_map = str.maketrans("""‚ƒ„†ˆ‹‘’“”•–—˜›""",
                           """'f"*^<''""---~>""")

#  If there is only one argument, it must be a dictionary mapping Unicode ordinals (integers) or characters
#  (strings of length 1) to Unicode ordinals, strings (of arbitrary lengths) or None.
multi_map = str.maketrans({  # <2>
    '€': '<euro>',
    '…': '...',
    'Œ': 'OE',
    '™': '(TM)',
    'œ': 'oe',
    '‰': '<per mille>',
    '‡': '**',
})
# merge two maps
multi_map.update(single_map)


def dewinize(txt):
    """replace win1253 symbols with ASCII chars or sequences"""
    return txt.translate(multi_map)


def asciize(txt):
    no_marks = shave_marks_latin(dewinize(txt))
    no_marks = no_marks.replace('ß', 'ss')
    return normalize('NFKC', no_marks)


order = '“Herr Voß: • ½ cup of Œtker™ caffè latte • bowl of açaí.”'
greek = 'Ζέφυρος, Zéfiro'

print(shave_marks(order))
print(shave_marks(greek))

print(shave_marks_latin(order))
print(shave_marks_latin(greek))

print(dewinize(order))
print(asciize(order))

# test='açaí'
# print(shave_marks_latin(test))


# for simple sorting, like the sort function, python will just compare the unicode, which will produce unwanted
# results for non-ASCII language
# the standard way to sort non-ASCII text python is to use the locale.strxfrm function, but the involve the locale
# setting of the system you are running and this produce many headache, so maybe it's best to just forget about it

# in short, pyuca is used for sorting non-English strings properly
import pyuca
import re

coll = pyuca.Collator()
fruits = ['açaí', 'acerola', 'atemoia', 'cajá', 'caju']
fruits = sorted(fruits, key=coll.sort_key)
print(fruits)

# \bXX   \b means the following two XX interpreted as hex for the char code
# \uXXXX  \n means unicode, so, four hex following
sample = '1\xbc\xb2\u0969\u136b\u216b\u2466\u2480\u3285'
# sample1 = '1\u00bc\u00b2\u0969\u136b\u216b\u2466\u2480\u3285'
# print(sample == sample1)

# r stands for raw string, use this to avoid escaping headache
#
re_digit = re.compile(r'\d')

for c in sample:
    print(
        'U+%04x' % ord(c),
        c.center(6),
        're_dig' if re_digit.match(c) else '-',
        'isdig' if c.isdigit() else '-',
        'isnum' if c.isnumeric() else '-',
        'isdeci' if c.isdecimal() else '-',
        format(unicodedata.numeric(c), '5.2f'),
        unicodedata.name(c),
        sep='\t'
    )

re_numbers_str = re.compile(r'\d+')
re_word_str = re.compile(r'\w+')
re_numbers_byte = re.compile(rb'\d+')
re_word_byte = re.compile(rb'\w+')

text_str = ("Ramanujan saw \u0be7\u0bed\u0be8\u0bef"
            " as 1729 = 1³ + 12³ = 9³ + 10³.")
text_str_byte = text_str.encode('utf8')

print('Text', repr(text_str), sep='\n')

# for number
# the unicode pattern can recognize  ௧௭௨௯  but the byte pattern can not
print('Number')
print(re_numbers_str.findall(text_str))
print(re_numbers_byte.findall(text_str_byte))

# for words
# the unicode pattern can recognize ௧௭௨௯ and superscripts which the byte type can not
print('Word')
print(re_word_str.findall(text_str))
print(re_word_byte.findall(text_str_byte))

# GNU/linux kernel is not Unicode savvy
# in real world you may find that the bytes of filenames are not sensible in any encoding schema

# all os function can accept str or bytes as arguments, and return the same type. internally, it use the
# sys.getfilesystemencoding() to get the codec and do the conversion automatically
# but, is you are dealing with filenames that can not be handled in this way, you can always pass bytes to the
# os functions and get bytes back, this will always work!  e.g.:
# os.listdir('.')     # pass str
# os.listdir(b'.')    # pass bytes

# two utils function, both use the sys.getfilessystemencoding()
# fsencode(filename)
# fsdecode(filename)

# unless you always use bytes, you may encounter encoding/decoding problem. To avoid this chokes the program,
# Unix-derived platforms use   surrogateescape   error handler
# Windows use  strict error handler

# surrogateescape : deal with unexpected butes or unknown encodingss
# the idea is the replace the unknow bytes with the Unicode range from U+DC00 to U+DCFF, in which range
# no characters assigned
# RUN the following lines in python terminal since there are non-unicode bytes that can not using print()
# since python will always try to show the text in unicode (utf8) format
# filename_bytes = b'digits-of-\xcf\x80.txt'
# filename_bytes.decode('ascii', 'surrogateescape')
# 'digits-of-\udccf\udc80.txt'
