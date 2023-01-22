#.keys() method; Link: https://www.tutorialspoint.com/python/dictionary_keys.htm
def combo_dicts (d1, d2):
    keys = set(d1.keys() & d2.keys())
    combo = {key: d1[key] + d2[key] for key in keys}
    return combo
d1 = {'a': 2, 'b': 3, 'c': 5, 'd': 30}
d2 = {'a': 3, 'b': 2, 'd': 3, 'f': 5}
print(combo_dicts(d1,d2))