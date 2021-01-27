def check_prime(key):
	res=0
	for i in range(2,key//2):
		if(key%i==0):
			res+=1
	if res==0:
		return 1
	else:
		return 0

def prime_composite_list(inp):
	prime=[]
	comp=[]
	res=[]
	for i in range(len(inp)):
		if(check_prime(inp[i])):
			prime.append(inp[i])
		else:
			comp.append(inp[i])
	res.append(prime)
	res.append(comp)
	return res
	
if __name__ ==”__main__”:
	inp=[]
	count=int(input())
	for i in range(count):
		inp.append(int(input()))
	print(check_prime(inp[1]))
	result=prime_composite_list(inp)
	print(result)Copied!
