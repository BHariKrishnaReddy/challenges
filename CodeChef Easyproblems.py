#BUYPLS
a,b,x,y=map(int,input().split())
print(a*x+b*y)


#VALTRI
n=int(input())
if n%5==0 or n%6==0:
  print("YES")
else:
  print("NO")


#ISBOHT
n = int(input())
if n%5==0 and n%11==0:
    print("BOTH")
elif n%5==0 or n%11==0:
    print("ONE")
else:
    print("NONE")
    
    
#DIFACTRS
c,fl,n =0,[],int(input())
for i in range(1,n+1):
    if n%i==0:
        c+=1
        fl.append(i)
print(c)
for i in fl:
  print(i,end=" ")


#SECLAR
# cook your dish here
a,b,c=int(input()),int(input()),int(input())

if a>b and a>c:
    if b>c :
        print(b)
    else:
        print(c)

if b>a and b>c:
    if a>c :
        print(a)
    else:
        print(c)

if c>b and c>a:
    if b>a :
        print(b)
    else:
        print(a)

        
        
#reverseMe        
n,s=int(input()),list(map(int,input().split()))
a=s[::-1]
for i in a:
    print(i,end=" ")
