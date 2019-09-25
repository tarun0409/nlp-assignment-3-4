master_dict = dict()
with open("../Data_sets/corpus_2_unigram.txt") as fileobj:
    for line in fileobj:
        if line == "" or line == " " or line == "\n":
            continue
        l = line.strip(' ')
        l = l.strip('\n')
        line_split = l.split(' ')
        master_dict[line_split[0]] = int(line_split[1])

with open("../Data_sets/corpus_2_16_unigram.txt") as fileobj:
    for line in fileobj:
        if line == "" or line == " " or line == "\n":
            continue
        l = line.strip(' ')
        l = l.strip('\n')
        line_split = l.split(' ')
        if line_split[0] not in master_dict:
            master_dict[line_split[0]] = 0
        master_dict[line_split[0]] = master_dict[line_split[0]] + int(line_split[1])

f = open("../Data_sets/corpus_2_unigram.txt","w+")
for key in master_dict:
    f.write(key)
    f.write(' ')
    f.write(str(master_dict[key]))
    f.write('\n')
f.close()