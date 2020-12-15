# the benefit for that range and slices exclude the last item

l = [1, 2, 3, 4, 5, 6, 7]
print(l[:3])  # produce the exact number of elements which in this case is three
print(l[3:])  # together with the previous line, the list is splited by a single same number 3
print(len(l[2:5]))  # the number of the element of the slicing is stop-start, which here is 5-2=3
