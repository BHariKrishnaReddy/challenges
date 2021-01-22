class Employee:
    def _init_(self,empid,empname,ageinrole):
        self.empid=empid
        self.empname=empname
        self.ageinrole=ageinrole
        self.status="In Service"
    
   
class Organizaton:
    def _init_(self,emplist):
        self.emplist=emplist
    
   
    def updateEmployeeStatus(self,noofyears):
        for i in self.emplist:
            if i.ageinrole>noofyears:
                i.status="Retirement Due"
        

    def countEmployees(self):
        l=[]
        count=0
        for i in self.emplist:
            if i.status=="Retirement Due":
                count+=1
                l.append(i)
        return count

  
if _name_ == "_main_":
    n=int(input())
    l=[]
    for i in range(n):
        empid=int(input())
        empname=input()
        ageinrole=int(input())
        a=Employee(empid,empname,ageinrole)
        l.append(a)
        
    f=Organizaton(l)
    
    noofyears=int(input())
    
    x=f.updateEmployeeStatus(noofyears)
    y=f.countEmployees()
    
    if y==0:
        print("No employee updated.")
    else:
        print("Count of employee updated=  {}".format(y))
        
    for i in l:
        print(i.empid,i.empname,i.status)
