# convert the encoding of file
# install Chardet
# in the terminal (virtual environment), run
# chardect filepath
# then you will get the encoding
# when you open the file, use it
# when you open the target file, open it with the encoding you wanted
# write the content from the source file to the target file
def convert_file_encoding(src_file, src_encoding, dest_file, dest_encoding):
    # f1 = open('/Users/duxingyu/Downloads/gb1212_file.txt', 'r', encoding='gb2312')
    # f2 = open('/Users/duxingyu/Downloads/utf8_file.txt', 'w', encoding='utf8')
    f1 = open(src_file, 'r', src_encoding)
    f2 = open(dest_file, 'w', dest_encoding)
    f2.write(f1.read())
    f1.close()
    f2.close()
