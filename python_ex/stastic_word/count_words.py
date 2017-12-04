import collections

def count_words(text, segment_num):
    # todo: implement method rather than return hard code sample
    # return [('butter', 2), ('a', 1), ('betty', 1)]
    # a = {}
    sp = text.split()
    words = sorted(sp)
    a = collections.OrderedDict()
    for w in words:
        if a.has_key(w):
            a[w] += 1
        else:
            a[w] = 1

    sorted_items = sorted(a.iteritems(), key=lambda a:a[1], reverse=True)
    # print sorted_items

    return sorted_items[0:segment_num]