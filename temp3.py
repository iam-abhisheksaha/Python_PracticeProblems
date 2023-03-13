import itertools

s = "pwwkew"
list_s = list(s)
# list_s = set(s)
data = list(itertools.combinations(s))
print(list_s)