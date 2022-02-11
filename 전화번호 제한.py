import random as rd
rd_list=[]
for i in range(100):
    rd_list.append(rd.randint(1,9999))

                   
for i in range(2000,2999):
    for j in range(1,9999):
        for k in rd_list:
            if k==j:
                print("010-{0}-{1:0^4}".format(i,j))
