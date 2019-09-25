unigram_dict = dict()
def is_english_word(word):
    if word == "":
        return False
    for l in word:
        if (ord(l)>=65 and ord(l)<=90) or (ord(l)>=97 and ord(l)<=122):
            continue
        else:
            return False
    return True
with open("../Data_sets/corpus_2_16_tokenized.txt") as fileobj:
    for line in fileobj:
        line_split = line.split(' ')
        for word in line_split:
            word_lower = word.strip()
            proceed = False
            if is_english_word(word_lower):
                word_lower = word_lower.lower()
                proceed = True
            else:
                word_split = word_lower.split("'")
                if len(word_split)==2:
                    if is_english_word(word_split[0]) and is_english_word(word_split[1]):
                        temp1 = word_split[0].lower()
                        temp2 = word_split[1].lower()
                        word_lower = temp1+"'"+temp2
                        proceed = True
            if proceed:
                if word_lower not in unigram_dict:
                    unigram_dict[word_lower] = 0
                unigram_dict[word_lower] = unigram_dict[word_lower]+1

f = open("../Data_sets/corpus_2_16_unigram.txt","w+")
for key in unigram_dict:
    f.write(key)
    f.write(' ')
    f.write(str(unigram_dict[key]))
    f.write('\n')
f.close()

