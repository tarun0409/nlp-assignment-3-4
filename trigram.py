word_one = None
word_two = None
word_three = None
master_list = list()
def is_english_word(word):
    if word == "":
        return False
    for l in word:
        if (ord(l)>=65 and ord(l)<=90) or (ord(l)>=97 and ord(l)<=122):
            continue
        else:
            return False
    return True

def add_to_list(word,N):
    if len(master_list) < N:
        master_list.append(word)
        return
    master_list.pop(0)
    master_list.append(word)

with open("../Data_sets/corpus_2_0_tokenized.txt") as fileobj:
    for line in fileobj:
        line_split = line.split(' ')
        
