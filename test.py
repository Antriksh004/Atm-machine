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
    
    with open(fileName, mode='r') as csvFile:
        csvReader = csv.reader(csvFile, delimiter = ",")
        for row in csvReader:
            if row == [accountNo,pin]:
                print("you are Logged in")
                return True
            
    print("please try again")
    for i in range(3):
        checkUser()
    print("you have attempted to enter the information 3 times")
                    
        
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
                check1 = input("type yes to proceed for transation:")
                if check1 == "yes" or check1 == "YES":
                    print("Transation was successful \n Thank you for using this ATM")
            else:
                print("the notes of the given money cannot be provided")      
                

main()           
        
    

        

    
