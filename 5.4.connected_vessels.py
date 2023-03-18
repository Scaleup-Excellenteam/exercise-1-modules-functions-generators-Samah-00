
def interleave(*iters):
    """
    aggregate the corresponding characters into tuples using zip.
    for each tuple, yield its items one by one.
    :param iters: one or more iterable
    :return: a list of interleaved items.
    """
    for items in zip(*iters):
        for item in items:
            yield item


result = list(interleave('abc', [1, 2, 3], ('!', '@', '#')))
print(result)
