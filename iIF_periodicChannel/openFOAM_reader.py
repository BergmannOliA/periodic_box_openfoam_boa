import numpy as np
import array
# Using readlines()
file1 = open('46.0180696341479774/wallShearStress', 'r')
Lines = file1.readlines()
#big_array = np.array([])
for i in range(30, 542):

    aa = Lines[i]
    cc = aa.replace('(', '')
    cc = cc.replace(')', '')
    #cc = cc.splitlines()
    cc = cc.split()
    #print('cc',cc)
    bb = np.array([1.1,2.2,3.3])
    #print(bb.shape, type(bb),bb[1],bb)
    bb[0] = cc[0]
    bb[1] = cc[1]
    bb[2] = cc[2]
    #bb = bb.transpose()
    #print(bb.shape, type(bb),bb[1],bb)
    #big_array = np.append(big_array,bb)
    #print('i',i)
    if i == 30:
        big_array = bb
        #print(big_array.shape, type(big_array),big_array[1],big_array)

    else:
        big_array = np.column_stack([big_array,bb])
    #print("{:e}".format(bb[1]))

#print(np.mean(big_array[2]))
#print(type(big_array),'big_array',big_array,big_array.shape)
#print(type(big_array[1]),'big_array[1]',big_array[1],big_array[1].shape)
a = big_array
mean_x = np.mean(a[0,:])
mean_y = np.mean(a[1,:])
mean_z = np.mean(a[2,:])

mean = np.mean(a)
dpdx = mean*2/0.02248*(510)
print('dpdx',dpdx)

print(mean_x,mean_y,mean_z)



print(big_array.shape)
with open('outfile.txt','wb') as f:
    for i in range(0,big_array.shape[0]):

        np.savetxt(f, big_array[i])















