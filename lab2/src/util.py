def _round(n, precision):
    return "{:.{}f}".format(n, precision)


def to_lower_unicode(n):
    s = ""
    for c in str(n):
        s += chr(8320 + int(c))
    return s
