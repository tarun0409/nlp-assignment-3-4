# from nltk.tokenize import word_tokenize

# def is_email(token):
#     l = len(token)
#     i = token.find('@')
#     if i!=0 and i!=(l-1) and i>0:
#         return True
#     return False

# def is_punctuation(ch):
#     if ch=='.' or ch==',' or ch=='!' or ch=='?' or ch==':' or ch==';' or ch=='\'' or ch=='\"' or ch=='-' or ch=='(' or ch==')':
#         return True
#     return False

# def is_number(token):
#     l = len(token)
#     for i in range(0,l):
#         n = ord(token[i])
#         if not ((n>=48 and n<=57) or token[i]==',' or token[i]=='.'):
#             return False
#     return True

# def is_url(token):
#     if token.find('https://') > 0 or token.find('http://') > 0 or token.find('www.')>0 or token.find('ww1.')>0 or token.find('ww2.')>0 or token.find('ww3.')>0:
#         return True
#     return False

def tokenize(tokens):
    print(tokens)
    curr_token = ""
    token_list = list()
    l = len(tokens)
    print(tokens[l-1])
    period = False
    if tokens[l-1] == '.':
        tokens = tokens[0:l-1]
        period = True
    print(period)
    for t in tokens:
        if t == '!' or t=='@' or t=='#' or t=='$' or t=='%' or t=='&' or t=='(' or t==')' or t=='{' or t=='}' or t=='[' or t==']' or t==':' or t==';' or ord(t)==34 or ord(t)==39 or t=='?' or t=='<' or t=='>' or t==',':
            if curr_token != "":
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





# tokenized_sents = tokenize('www.com.')
# print(tokenized_sents)
f = open("corpus_3_2.txt","w+")
with open("corpus3.txt") as fileobj:
    for line in fileobj:
        l_stripped = line.strip()
        l = tokenize(l_stripped)
        f.write(" ".join(l))
        f.write('\n')
        break
f.close()