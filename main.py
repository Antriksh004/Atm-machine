import csv
# fields = ["AccountNo","PIN","BankBalance"]

# values = [[1040433,9807,17000],
#           [7204033,6807,18090],
#           [9244933,9867,17000],
#           [3044403,9897,19000],
#           [6204409,6007,18000],
#           [9044303,9667,17090]]
filename = "accountHolders.csv"
with open(filename,'r') as csvfile:
    # csvwriter = csv.writer(csvfile)
    # csvwriter.writerow(fields)
    # csvwriter.writerows(values)
    csvReader = csv.reader(csvfile,delimiter=',')
    # a = int(input("enter the account no. :"))
    # b = int(input("enter your PIN :"))
    for row in enumerate(csvReader):
        # if a == row[1] and b == row[1]:
        #     print("the user is valid")
        # else:
        lst = row[1]
        # if a == lst[0] and b == lst[1]:
        #     print("access approved")
        # else:
        #     print("denied")
        print(lst[1])
        