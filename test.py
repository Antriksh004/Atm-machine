import csv
fileName = "accountHolders.csv"



def addingFieldName():
    with open(fileName, mode ='a', newline="") as csvFile:
        csvWriter = csv.writer(csvFile,delimiter=',')
        csvWriter.writerow(["AccountNo","PIN"])
    

def register():
    with open(fileName, mode ='a', newline="") as csvFile:
        csvWriter = csv.writer(csvFile,delimiter=',')
        accountNo = input("enter your ACCOUNT NO")
        pin = input("enter your PIN")
        
        csvWriter.writerow([accountNo,pin])
        print("registration successful")


def checkUser():
    accountNo = input("enter your ACCOUNT NO")
    pin = input("enter your PIN")
    # bankBalance = int(input("enter your bank balance"))
    
    fileName = "accountHolders.csv"
    
    with open(fileName, mode='r') as csvFile:
        csvReader = csv.reader(csvFile, delimiter = ",")
        for row in csvReader:
            if row == [accountNo,pin]:
                print("you are Logged in")
                return True
    print("please try again")
    return False
# in case you want to register user just uncomment the line below
# for i in range(4):
#     register()

def main():
    print("WELCOME TO THE BANK OF BADLAPUR")
    query = int(input("please press 1 to enter the account details ..."))
    if query == 1:
        
        if checkUser() == True:
            
            amount = int(input("Availabe denominations are 100 200 500 \n enter the amount to withdraw : "))
            if(amount%100 == 0 or amount%200 == 0 or amount%500 == 0):
                print("your transaction amount is ",amount)
                check1 = int(input("press 1 to proceed for transation:"))
                if check1 == 1:
                    print("Transation was successful \n Thank you for using this ATM")
            else:
                print("the notes of the given money cannot be provided")      
                
        else:
            print("the details you entered are not correct")

main()           
        
    

        

    
