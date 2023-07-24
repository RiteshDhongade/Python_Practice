#Get the loan details
money_owned = float(input("How much money do you owe, in dollors?\n")) #$50000
apr = float(input("What is the annual percentage rate?\n")) #3
payment = float(input("What will your monthly payment be, in dollors?\n")) #1000
months = int(input("How many months do you want to see results for?\n"))  #24
# Divide apr with 100 to get percent anf then by 12 to get per month rate.
monthly_rate = apr/100/12

for i in range(months):
    #Add interest
    interest_paid = money_owned*monthly_rate
    money_owned = money_owned + interest_paid

    if money_owned - payment < 0:
        print("The last payment is ",money_owned)
        print("You paid off the loan in ", i+1,"months")
        break
    #make Payment
    money_owned = money_owned - payment

    # Print the result after this month
    print("Paid", payment, "of which", interest_paid, "was interest.",end='')
    print("Now I owe", money_owned)