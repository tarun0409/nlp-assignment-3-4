import operator
master_dict = dict()
with open("../Data_sets/corpus_2_unigram.txt") as fileobj:
    for line in fileobj:
        if line == "" or line == " " or line == "\n":
            continue
        l = line.strip(' ')
        l = l.strip('\n')
        line_split = l.split(' ')
        master_dict[line_split[0]] = int(line_split[1])

master_dict_sorted = sorted(master_dict.items(), key=operator.itemgetter(1),reverse=True)
f = open("../Data_sets/corpus_2_unigram_sorted.txt","w+")
for tup in master_dict_sorted:
    f.write(tup[0])
    f.write(' ')
    f.write(str(tup[1]))
    f.write('\n')
f.close()