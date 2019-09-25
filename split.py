file_objs = list()
for i in range(0,20):
    file_name = "../Data_sets/corpus_2_"+str(i)+".txt"
    file_objs.append(open(file_name,"w+"))
curr_fi = 0
i=0
with open("../Data_sets/corpus2.txt") as fileobj:
    for line in fileobj:
        file_objs[curr_fi].write(line)
        file_objs[curr_fi].write("\n")
        i+=1
        if i>=5000000:
            file_objs[curr_fi].close()
            curr_fi+=1
            i=0
        print(curr_fi)
        print(i)
file_objs[curr_fi].close()
# for i in range(0,20):
#     file_objs[i].close()
# # print(i)