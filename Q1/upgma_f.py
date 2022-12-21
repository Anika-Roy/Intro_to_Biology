inpt=[[0],[1],[2],[3],[4],[5],[6],[7],[8],[9]]

size=len(inpt)

dct = {}
for i in range(size+1):
    dct['lst_%s' % i] = []

file=open('Ndistance.txt','r')
Lines = file.readlines()

#print(Lines)

# print(Lines)
for x in Lines:
    if x=='\n':
        continue
    industry = x.split(",")
    #print(industry)
    row=[]
    for j in range(size):
        val=float(industry[j])
        row.append(val)
    dct['lst_%s' % size].append(row)

#print(dct['lst_%s' % size])

#upgma begins...
#iterating for minimum
for iter in range(size,1,-1):
    I=0
    J=0
    min=200
    for i in range(iter-1):
        for j in range(i+1,iter):
            if dct['lst_%s' % iter][i][j]<min:
                min=dct['lst_%s' % iter][i][j]
                I=i
                J=j
    for x in inpt[J]:
        inpt[I].append(x)
    inpt.pop(J)

    for i in range(iter-1):
        row=[]
        for j in range(iter-1):
            if i>=j:
                val=0
            else:
                sum=0
                count=0
                for a in inpt[i]:
                    for b in inpt[j]:
                        sum=sum+dct['lst_%s' % size][a][b]+dct['lst_%s' % size][b][a]
                        count+=1
                val=sum/count
            row.append(val)

        dct['lst_%s' % (iter-1)].append(row)

    print(inpt,min)
    # print(dct['lst_%s' % (iter-1)])
