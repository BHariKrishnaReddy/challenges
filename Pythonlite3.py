#Define the find_Novowels function here
def find_Novowels(inp_str):
	res=[] 
	for i in inp_str:
		c=0
		for j in i:
			if(j=='A' or j=='a' or j=='E' or j=='e' or j=='I' or j=='i' or j=='O' or j=='o' or j=='U' or j=='u'):
				break
			else:
				c+=1
		if c==len(i):
			res.append(i)
	return res
 
#Sample main section. 
#Do not remove the below portion of code. 
if __name__=='__main__':
        count=int(input())
        inp_str=[]
        for i in range(count):
                inp_str.append(input())
        output=find_Novowels(inp_str)
        if len(output)!=0:
                print('Strings without vowels:')
                for i in output:
                        print(i)
        else:
                print('No string found')
