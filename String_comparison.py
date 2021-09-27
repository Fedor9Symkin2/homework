import difflib
import math

def string_comparison(x, y):
  general_comparison = difflib.SequenceMatcher(None, x, y)
  return print(math.ceil(general_comparison.ratio() * 100), '%')

string_comparison(input(), input())
