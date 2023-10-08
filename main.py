import csv
import pandas as pd
fileName = "accountHolders.csv"



def addField(accountNo, balance):
    with open('AccountBalance.csv', mode ='a', newline="") as csvFile:
        csvWriter = csv.writer(csvFile,delimiter=',')
        csvWriter.writerow([accountNo,balance])

    

def register():
    with open(fileName, mode ='a', newline="") as csvFile:
        csvWriter = csv.writer(csvFile,delimiter=',')
        accountNo = input("enter your ACCOUNT NO")
        pin = input("enter your PIN")
        
        csvWriter.writerow([accountNo,pin])
        print("registration successful")


def checkUser(accountNo,pin):
    for i in range(3):

        with open(fileName, mode='r') as csvFile:
            csvReader = csv.reader(csvFile, delimiter = ",")
            for row in csvReader:
                
                if row == [accountNo,pin]:
                    
                    print("you are Logged in")
                    return True
                
                    
            
        print("please try again")
        accountNo = input("enter your ACCOUNT NO")
        pin = input("enter your PIN")

        
    print("you have attempted to enter the information 3 times")
    return
    
def checkBalance(accountNo):
    
    with open("AccountBalance.csv", mode='r') as csvFile:
        csvReader = csv.reader(csvFile, delimiter = ",")
        for row in csvReader:
            if row[0] == accountNo:
                return int(row[1])
            else :
                pass
            

    
def updateBalance(accountNo, balance):
    df = pd.read_csv("AccountBalance.csv")
    
    # Use the correct column names
    new_val = df["AccountNo"] == accountNo
    b = df.index[new_val]
    
    new_output = b.tolist()
    print(new_output)
  
    df.loc[new_output, 'AccountBalance'] = balance

    df.to_csv("AccountBalance.csv", index=False)
    
    print("updated successfully") 


    

                    
        
# in case you want to register user just uncomment the line below
# for i in range(4):
#     register()

def main():
    print("WELCOME TO THE BANK OF BADLAPUR")
    query = int(input("please press 1 to enter the account details ..."))
    if query == 1:
        accountNo = input("enter your ACCOUNT NO")
        pin = input("enter your PIN")
        
        if checkUser(accountNo, pin) == True:
            balance = checkBalance(accountNo)
            
            amount = int(input("Availabe denominations are 100 200 500 \n enter the amount to withdraw : "))
            if(amount <= balance):
                
                if(amount%100 == 0 or amount%200 == 0 or amount%500 == 0):
                    print("your transaction amount is ",amount)
                    check1 = input("type yes to proceed for transation:")
                    if check1 == "yes" or check1 == "YES":
                        print("Transation was successful \n Thank you for using this ATM")
                        balance_left = balance - amount
                        
                        req = input("type yes to see your balance")
                        if req == "yes" or req == "YES":
                            print("accountNo",accountNo)
                            print("balance left:",balance_left)
                            updateBalance(int(accountNo),balance_left)
                            
                else:
                    print("the notes of the given money cannot be provided") 
            
            else:
                print("insufficient balance")
        else:
            return
                        
    
                         
                

main()


          
        
    

        

    
