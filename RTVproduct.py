# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
class RTVProduct:
    def __init__(self,sku_Nbr,quantity,return_Reason,ship_To_Rlc_Flg,rtv_stat_code):
        self.sku_Nbr=sku_Nbr
        self.quantity=quantity
        self.return_Reason=return_Reason
        self.ship_To_Rlc_Flg=ship_To_Rlc_Flg
        self.rtv_stat_code=rtv_stat_code
    def assign_status(self):
        y=self.return_Reason.upper().lower()
        if (y=="manufacturer defect" or "manufacturerdefect") and self.ship_To_Rlc_Flg=="True":
            self.rtv_stat_code=100
        else:
            self.rtv_stat_code=500
            

class Store:
    def __init__(self,name,rtv_list):
        self.name=name
        self.rtv_list=rtv_list

    def fetchRtvProduct(self,quantity):
        maxquantity=0
        rl=[]
        for i in self.rtv_list:
            i.assign_status()
        for i in self.rtv_list:
            if i.rtv_stat_code==500 and i.quantity>quantity:
                if i.quantity>maxquantity:
                    maxquantity=i.quantity
                    x=i
        if maxquantity==0:
            return None
        else:
            
            rl.append(x.sku_Nbr)
            rl.append(maxquantity)
            rl.append(x.ship_To_Rlc_Flg)
            return rl
        
        2
if __name__ == "__main__":
    count=int(input())
    l=[]
    for i in range(count):
        sku_Nbr=int(input())
        quantity=int(input())
        return_Reason=input()
        ship_To_Rlc_Flg=input()
        rtv_stat_code="None"
        l.append(RTVProduct(sku_Nbr,quantity,return_Reason,ship_To_Rlc_Flg,rtv_stat_code))
    q=int(input())
    st=Store("ABC",l)  
    res1=st.fetchRtvProduct(q)
  
    if res1==None:
        print ("No RTVProduct Found")
        
    else:
        print(*res1)
    
    
