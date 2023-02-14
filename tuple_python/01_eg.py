# tuple

t1 =  ()
print(t1)

t2 = tuple()
print(t2)

t3 = 10,
print(type(t3))

t4 = 10,20,30 , 40 ,50
t5 = (10,20,30,40,50)
print(t4,t5)

t6 = (10,20)
print(t6 * 2)

#t7 = (30,40)
#print(t6*t7)

t1 = ()
print(dir(t1))

# list/tuple #unpacking(*)

*w,x,y,z = 50,40,30,20,10,5,0
print(w)
print(x)
print(y)
print(z)