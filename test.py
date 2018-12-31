from fuzzywuzzy import process
import re
from Levenshtein import *
f = open("/Users/dongxinyuan/Desktop/Projektpraktikum Information Service Engineering/data/rawdata/split/uniq_finaldataset_random100000_title", "r")
testlist = f.read().split("\n")
print(len(testlist))
pattern = input("Enter a pattern: ")


def get_matches(query, choice, limit=100):
    results = process.extract(query, choice, limit=limit)
    return results

# process.extract using partial_ratio, the ratio of most similar substring.

print(get_matches(pattern, testlist))
