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
