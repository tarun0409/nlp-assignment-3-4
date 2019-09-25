import sys
def is_email(token):
    at_i = token.find('@')
    dot_i = token.find('.')
    l = len(token)
    if at_i>=0 and at_i<l and dot_i>=0 and dot_i<l and at_i!=0 and at_i!=(l-1) and dot_i!=0 and dot_i!=(l-1):
        return True
    return False 
def is_number(token):
    puncts = ['.',',',':']
    if ord(token[0])<48 or ord(token[0])>57:
        return False
    for t in token:
        if (ord(t)>=48 and ord(t)<=57) or (t in puncts):
            continue
        else:
            return False
    return True
def is_url(token):
    url_parts = token.split('.')
    if token.startswith('http') or token.startswith('www.') or token.startswith('ww1.') or token.startswith('ww2.') or token.startswith('ww3.') or len(url_parts)>2:
        return True
    return False
def is_apos_word(token):
    token_split = token.split("'")
    if len(token_split)==2:
        return True
    return False
def is_mention(token):
    if token[0]=='@':
        return True
    return False
def is_hashtag(token):
    if token[0]=='#':
        return True
    return False

    
def tokenize(tokens):
    # print(tokens)
    curr_token = ""
    token_list = list()
    l = len(tokens)
    if l<=0:
        return list()
    if l==1:
        token_list.append(tokens)
        return token_list
    period = False
    if tokens[l-1] == '.':
        tokens = tokens[0:l-1]
        period = True
    if is_mention(tokens) or is_hashtag(tokens) or is_email(tokens) or is_number(tokens) or is_apos_word(tokens) or is_url(tokens):
        token_list.append(tokens)
        if period:
            token_list.append('.')
        return token_list
        
    for t in tokens:
        if t == '!' or t=='@' or t=='#' or t=='$' or t=='%' or t=='&' or t=='(' or t==')' or t=='{' or t=='}' or t=='[' or t==']' or t==':' or t==';' or ord(t)==34 or ord(t)==39 or t=='?' or t=='<' or t=='>' or t==',' or t=='-':
            if curr_token != "":
                l_temp = len(curr_token)
                if curr_token[l_temp-1]=='.':
                    curr_token = curr_token[0:l_temp-1]
                    token_list.append(curr_token)
                    token_list.append('.')
                else:
                    token_list.append(curr_token)
            token_list.append(t)
            curr_token = ""
        else:
            curr_token+=t
    if curr_token!="":
        token_list.append(curr_token)
    if period:
        token_list.append('.')
    return token_list

# line = "The meeting went from 2:00 to 4:00."
# line_s = line.split(' ')
# arr = list()
# for l in line_s:
#     arr.extend(tokenize(l))
# print(" ".join(arr))

for i in range(3,17):
    in_file_name = "../Data_sets/corpus_2_"+str(i)+".txt"
    out_file_name = "../Data_sets/corpus_2_"+str(i)+"_tokenized.txt"
    f = open(out_file_name,"w+")
    # file_name = sys.argv[1]
    with open(in_file_name) as fileobj:
        for line in fileobj:
            l_stripped = line.strip()
            l_splits = l_stripped.split(' ')
            tokens = list()
            for l_split in l_splits:
                l = tokenize(l_split)
                tokens.extend(l)
            #print(" ".join(tokens))
            f.write(" ".join(tokens))
            f.write('\n')
    f.close()