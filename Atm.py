import random

balance=random.randint(9000,100000)

class Atm:
   def  __init__(self,pin,accNo):
       self.pin=pin;
       self.accNo=accNo
       
       print("The Acc no is",accNo)
       
   def withdrawl(self,amt,balance):
       
            self.balance=balance
            self.amt=amt
       
            print("you withdrew rupees ",amt)
            print("balance left ",(balance-amt),"rupees")
            
   def Enquiry(self,balance) :
       
        self.balance=balance
        print("the amount in your bank is:",balance," rupees")
        
def main():
   
    no=input("the account no:")
    pin=input("the pin:")
    atm=Atm(pin,no)
    a=int(input("for withdrawl press 1,for enquiry press 2  :"));
    
    if(a==1) :
        amt=int(input("enter the amt"))
        print("the amt is",amt)
        atm.withdrawl(amt,balance)
    elif(a==2) :
        atm.Enquiry(balance)
    else :
        print("wrong input restart")
    
main()
        