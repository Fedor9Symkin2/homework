# -*- coding: utf-8 -*-
"""string_comparisonipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qmpqalZWGOzRnEUj-_Umd0a6YOumoAjp
"""

import difflib
import math

def string_comparison(x, y):
  general_comparison = difflib.SequenceMatcher(None, x, y)
  return print(math.ceil(general_comparison.ratio() * 100), '%')

string_comparison(input(), input())