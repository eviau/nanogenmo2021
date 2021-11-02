import pycorpora
import random

import pandas as pd

import numpy as np

df = pd.read_csv('SPY.csv', index_col=0)

print(df.head(10))


print((pycorpora.words.literature.shakespeare_words['words'][0]))

df2 = pd.read_csv("letters_inversed.csv", index_col=0)

df2 = df2.sort_values(ascending=True, by='Frequency')

print(df2)

# first save the daily percentage change in an array

# then iterate on letters. when there is a negative value it adds randomly a comma, a space, a colon, etc.

percentage = df.pct_change()

print(percentage.head(10))

print(percentage.stack())

stack_perc = percentage.stack()*100

bins = df2["Frequency"]
names = df2.index

print(names)
print(stack_perc)

(pd.cut(stack_perc, bins, labels=names[1:])).to_csv('test.csv')

