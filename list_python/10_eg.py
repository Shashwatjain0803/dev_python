# deep copy and shallow copy

# In deep copy the original ;ist will not  affected
import copy
l1 = [[20,30],[40,50],[60,70]]
print(len(l1))

l2 = copy.deepcopy(l1)
l1[0][0] = 600
print(l2)
print(l1)

#in shallow copy the orignal list will be affected


l1 = [[10,20],[30,40],[50,60]]
print(len(l1))
l2 = copy.copy(l1)
l1[1][1] = 500
print(l1)
print(l2)