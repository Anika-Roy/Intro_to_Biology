
import numpy

import blosum as bl

matrix = bl.BLOSUM(62)

file = open("Protein.txt", "r")

Lines = file.readlines()

# print(Lines)

# print(type(Lines[0]))
dict = {}
for i in range(10):
    dict['seq_%s' % i] = ''

total=''

i=0
for x in Lines:
        # print(x[0])
        if ('%s' % x[0]) == '>':
            continue
        elif ('%s' % x[0]) == '\n':
            i+=1
        else:
            x=x.rstrip()
            dict['seq_%s' % i]=dict['seq_%s' % i]+x
            # total+x

    
# print(dct)
for num_1 in range(10):
    for num_2 in range(10):
        if num_1<num_2:
            seq_1 = dict['seq_%s' % num_1]
            seq_2 = dict['seq_%s' % num_2]

            #print(seq_1)
            #print(seq_2)
            (rows, cols) = (len(seq_1), len(seq_2))
            # print(rows,cols)
            weights = []

            for i in range(rows):
                row = []
                for j in range(cols):
                    row.append(matrix[seq_1[i]+seq_2[j]])
                weights.append(row)
            
            values = numpy.zeros((rows+1, cols+1))
            # print(values)

            #initialising lengths
            length= numpy.zeros((rows+1, cols+1))
            for i in range(1,cols+1):
                length[0][i]=i

            #dp
            for i in range(1, (rows+1)):
                length[i][0]=i
                for j in range(1, (cols+1)):
                    list = [[values[i-1][j-1]+weights[i-1][j-1], length[i-1][j-1]], [values[i-1][j]-1, length[i-1][j]],[values[i][j-1]-1,length[i][j-1]]]
                    list.sort()
                    list.reverse()
                    #if i==1 and j==1: print(list)

                    if list[0][0] > list[1][0]:
                        values[i][j] = list[0][0]
                        length[i][j]=list[0][1]+1
                    # if not(list[0][1][0]==i-1 and list[0][1][1]==j-1):
                    #     length+=1

                    elif list[0][0] == list[1][0] and (list[1][0] > list[2][0]):
                        values[i][j] = list[1][0]
                        length[i][j]=list[1][1]+1
                #     values[i][j]=list[0][0]
                #     #length+=1

                    elif list[0][0] == list[1][0] and (list[1][0] == list[2][0]):
                        values[i][j] = list[2][0]
                        length[i][j]=list[2][1]+1
                #     values[i][j]=values[i-1][j-1]+weights[i-1][j-1]

            #print(length)

            print(1/(values[rows][cols]),end=',')

            #print(values[rows][cols],length[rows][cols],end=',')
        else:
            print(0,end=',')
    
    print('\n')



