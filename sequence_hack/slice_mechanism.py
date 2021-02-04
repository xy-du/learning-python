class MySeq:
    def __getitem__(self, item):
        return item


ms = MySeq()
print(ms[1])  # 1
print(ms[1:4])  # slice(1, 4, None)
print(ms[1:4:2])  # slice(1, 4, 2)
print(ms[1:4:2, 9])  # (slice(1, 4, 2), 9)
print(ms[1:4:2, 7:9])  # (slice(1, 4, 2), slice(7, 9, None))

# when slicing, the item argument in __getitem__ become a slice object
# when just one element is required, item is just a simple integer

print(slice)
print(dir(slice))
# you can find indices,start,step,stop
# indices method here is interesting
# S.indices(len) -> (start, stop, stride)
# In other words, indices exposes the tricky logic that’s implemented in the built-in sequences to gracefully handle
# missing or negative indices and slices that are longer than the target sequence. This method produces “normalized”
# tuples of non-negative start, stop, and stride integers adjusted to fit within the bounds of a sequence of the
# given length.

print(slice(None, 10, 2).indices(5))  # return (0, 5, 2), so it's ok even if you stop is beyond the length 5
