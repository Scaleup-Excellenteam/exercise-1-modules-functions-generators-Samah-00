def join(*lists, sep="-"):
    if not len(lists):
        return None

    result = []
    for i, lst in enumerate(lists):
        result.extend(lst)
        # if the current list isn't the last list, append sep to result:
        if i < len(lists) - 1:
            result.append(sep)
    return result


print(join([1, 2], [8], [9, 5, 6], sep='@'))
print(join([1, 2], [8], [9, 5, 6]))
print(join([1]))
print(join())
