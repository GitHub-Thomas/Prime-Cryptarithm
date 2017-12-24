"""
ID:wzch_di3
TASK:crypt1
LANG:PYTHON3
"""
fin = open("crypt1.in","r")
fout = open("crypt1.out","w")

def judge(number,use):
    for i in range(0,len(number)):
        if (not number[i] in use):
            return(0)
    return(1)

n = int(fin.readline())
string = fin.readline()

index = -1
use = []
for i in range(1,n):
    index = string.find(" ",index+1,len(string))
    use.append(string[index-1])
use.append(string[index+1])
total = 0
for i in range(100,999):
    for j in range(10,99):
        sum1 = str(i)
        sum2 = str(j)
        sum3 = str(i * (j % 10))
        if (int(sum3) >= 1000):
            continue
        sum4 = str(i * (j // 10))
        if (int(sum4) >= 1000):
            continue
        sum5 = str(i * j)
        if (int(sum5) >= 10000):
            continue
        if ((judge(sum1,use))and(judge(sum2,use))and(judge(sum3,use))and(judge(sum4,use))and(judge(sum5,use))):
            total = total + 1
fout.write(str(total)+'\n')
fin.close()
fout.close()
