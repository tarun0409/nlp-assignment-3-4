import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

master_list = list()
with open("../Data_sets/corpus_2_unigram_sorted.txt") as fileobj:
    for line in fileobj:
        if line == "" or line == " " or line == "\n":
            continue
        l = line.strip(' ')
        l = l.strip('\n')
        line_split = l.split(' ')
        master_list.append((line_split[0],int(line_split[1])))

index = list()
freq = list()
for i in range(10000,11000):
    freq.append(master_list[i][1])
    index.append(i)

df = pd.DataFrame({'10000-11000': freq}, index=index)
lines = df.plot.line()
lines.set_title('Corpus 2 Zipfs Law')
lines.set_xlabel('Rank')
lines.set_ylabel('Frequency')
plt.show()