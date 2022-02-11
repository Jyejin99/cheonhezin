import random as rd
rd_list=[]
rd_list2=[]
for a in range(100):
    rd_list2.append(rd.randint(1,9999))
for i in range(100):
    rd_list.append(rd.randint(1,9999))

                   
for i in range(2000,2999):
    for j in range(1,9999):
        for u in rd_list2:
            if u==i:
                for k in rd_list:
                    if k==j:
                        print("010-{0}-{1:0^4}".format(i,j))
