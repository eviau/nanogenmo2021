import random

import pandas as pd

df = pd.read_csv('SPY.csv', index_col=0)

percentage = df.pct_change()

with open('fluctuations.txt', 'w') as out:
    out.write("And now we are going ")

    for index, row in percentage.iterrows():
        value = row['Open']
        if value == 0:
            up_and_down = "nowhere"
        elif value >0:
            up_and_down = "up"
        else:
            up_and_down = "down"
        var = up_and_down +  " and now we are going "
        out.write(var)
        value = row['Close']
        if value == 0:
            how = 'silently'
        elif value > 0 :
            how = "somehow with good manners"
        else:
            how = "how?"
        out.write("[closing, " + how + "]")      
        out.write("\n")
