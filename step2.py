import pycorpora
import random

import pandas as pd

import numpy as np

df = pd.read_csv('test.csv', index_col=0)
spaces = 0
nanogenmo = ""
    
for index, row in df.iterrows():
    current_letter = row['Letter']
    


    
    if current_letter == "'space'":
        nanogenmo = nanogenmo + " "
        spaces = spaces + 1
    elif current_letter == "'dot'":
        nanogenmo = nanogenmo + ". /n"
    elif current_letter == "'comma'":
        nanogenmo = nanogenmo + ", "
    else:
        nanogenmo = nanogenmo + str(current_letter)
print(nanogenmo)
print(spaces)
