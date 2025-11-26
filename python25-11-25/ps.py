#to print numbrs in list without using list comprehension
tem=[]
for x in range(1,10):
    tem+=[x]
print(tem)
#list comprehension
res=[x for x in range(1,10)]   #x=1
print(res)
#even
for x in range(1,10):
    if x%2==0:
        print(x)
#list comprehensioneven
res=[]
res=[x for x in range(1,10) if x%2==0]
print(res) #[2,4,6,8]
#list comprehension
res=[]
res=[x for x in range(0,10,2)]
print(res)
#print string along with count in a tuple
h=['mohan','kumar','ravi','sai']  #
tem=[]
for x in h:
    tem.append((x,len(x)))
print(tem)
#list comprehension in tuple
h=['mohan','kumar','ravi','sai']
res=[(x,len(x)) for x in h]
print(res)
#factors of 10
j=10
res=[]
for x in range(1,j):
    if j%x==0:
        res.append(x)
print(res)
#list comprehension in to list factors of 10
n=10
res=[x for x in range(1,n) if n%x==0]
print(res)
# print end with 5 
tem=[]
for x in range(1,30):

    if x%10==5:
        tem.append(x)
print(tem)
#by using list comprehension to print ends with 5
res=[x for x in range(1,30) if x%10==5]
print(res)
# iwant output like this n[[1,2],[3,4],[5,6]]
res=[[x,x+1] for x in range(1,7,2)]
print(res)
# 2d list convert into 1d
h=[[10,20,30],[40,50,60]]
for x in h:
    for y in x:
        print(y)
#2d list convert into 1d
res=[y for x in h for y in x]
print(res)
#palindrom in range of (10,100)
res=[x for x in range(10,100) if str(x)==str(x)[::-1]]
print(res)
#tuple comprehesion
res=(x for x in range(1,11))
for x in res:
    print(x)
" type conversion"
res=tuple(x for x in range(1,11))
print(res[3])

" "
# t=(x for x in range(10))
# print(t[1])
" "
res=tuple((x,ord(x)) for x in "ABCD")
print(res)