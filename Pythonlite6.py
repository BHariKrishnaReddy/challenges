class City:
	def __init__(self,c,s,cn,cb,avlcb,v,avlvb):
		self.city_id=c
		self.state_name=s
		self.city_name=cn
		self.covidbeds=cb
		self.avlblcovbeds=avlcb
		self.vetilbeds=v
		self.avlblventilbeds=avlvb

class CovBedAnalysis:
	def __init__(self,an,cl):
		self.analysis_name=an
		self.city_list=cl

	def get_StateWiseAvalblBedStats(self):
		l=[]
		for i in self.city_list:
			l.append(i.state_name)
		l=set(l)
		l=sorted(l)
		res=[]
		for i in l:
			k=[]
			acb=0
			avb=0
			for j in self.city_list:
				if i==j.state_name:
					acb+=j.avlblcovbeds
					avb+=j.avlblventilbeds
			k.append(i)
			k.append(acb)
			k.append(avb)
			res.append(k)
		return res

	def get_CitisWithMoreThanAvgOccpiedbeds(self,state):
		res2=[]
		temp=0
		cvb=0
		veb=0
		for i in self.city_list:
			if state==i.state_name:
				temp+=1
				cvb+=i.covidbeds-i.avlblcovbeds
				veb+=i.vetilbeds-i.avlblventilbeds
		if(temp > 0):
		    avg1=cvb//temp
		    avg2=veb//temp
		for i in self.city_list:
			if state==i.state_name:
				k=[]
				cb=i.covidbeds-i.avlblcovbeds
				vb=i.vetilbeds-i.avlblventilbeds
				if(avg1<cb and avg2<vb):
					k.append(i.city_name)
					k.append(cb)
					k.append(vb)
					res2.append(tuple(k))
		return res2
		
if __name__ == '__main__':
	count=int(input())
	l=[]
	for i in range(count):
		c=int(input())
		s=input()
		cn=input()
		cb=int(input())
		avlblcb=int(input())
		v=int(input())
		avlvb=int(input())
		l.append(City(c,s,cn,cb,avlblcb,v,avlvb))
	c=CovBedAnalysis("covid",l)
	state=input()
	res1=c.get_StateWiseAvalblBedStats()
	for i in range(len(res1)):
		for j in range(len(res1[i])):
			print(res1[i][j],end=" ")
		print("")
	res2=c.get_CitisWithMoreThanAvgOccpiedbeds(state)
	if(len(res2)>0):
		for i in range(len(res2)):
			for j in range(len(res2[i])):
				print(res2[i][j],end=" ")
		print("")
	else:
		print("No city available")
