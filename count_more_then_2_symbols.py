import collections # should copy to codewars
# inputs for testing
text1 = 'Indivisibi22lities'
text2 = ''
i = 0
# ready function
def duplicate_count(text):
    i = 0
    text = text.lower() # set lowercase
    # count in collection
    d = collections.defaultdict(int)
    for c in text:
        d[c] += 1
    a = dict.values(d)
    # count not 0 not 1 num chars
    for j in a:
        if j > 1:
            i += 1
    return i

print(duplicate_count(text1))
