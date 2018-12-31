import fuzzyset
from fuzzyset import *

# a = fuzzyset.FuzzySet
f = open("/Users/dongxinyuan/Desktop/Projektpraktikum Information Service Engineering/data/rawdata/split/test.txt", "r")
testlist = f.read().split("\n")
a = fuzzyset.FuzzySet(testlist)

for l in testlist:
    a.add(l)


# a.add("asd")

# a = f.read().split("\n")
print(a.get("history"))
