#Loan Calculator
from matplotlib import pyplot
import time

#Collecting information on loans
def get_loan_info():
    loan = {}
    loan["Principal"] = float(input("Enter loan amount: \t"))
    loan["Rate"] = float(input("Enter interest rate (%): \t"))
    loan["Rate"] = loan["Rate"]/100
    loan["Monthly Payment"] = float(input("Enter desired monthly payment : \t"))
    loan["Money Paid"] = 0
    return loan

#Displaying loan information
def show_loan_info(loan, months):
    print("\nLoan Status after ", month_number, "Months:")
    for k, v in loan.items():
        print( k,":", v)

def collect_interest(loan):
    loan["Principal"] =loan["Principal"] + (loan["Principal"]*(loan["Rate"]/12))

def make_monthly_payment(loan):
    loan["Principal"] = (loan["Principal"]-loan["Monthly Payment"])
    if loan["Principal"] > 0:
        loan["Money Paid"] += loan["Monthly Payment"] 
    else :
        loan["Money Paid"] += loan["Monthly Payment"] + loan["Principal"]
        loan["Principal"] = 0        

def summarize_loan(loan, months, initial_principal):
    print("\t\t----Loan Information After ", months, "Months----")
    print("\tInitial loan value = ", initial_principal)
    print("\tPrincipal =", loan["Principal"])
    print("\tInterest Rate = ", 100*loan["Rate"])
    print("\tTotal Paid = ", round(loan["Money Paid"], 2))
    print("\tInterest = ", round((loan["Money Paid"] - initial_principal)), 2)
    print("\n\n")
    time.sleep(2)

def create_graph(loan_data, loan):
    x_values = []
    y_values = []

    for data in loan_data:
        x_values.append(data[0])
        y_values.append(data[1])
        
    pyplot.plot(x_values, y_values)
    pyplot.title(str(100*loan["Rate"]) + "% Interest With $" + str(loan["Monthly Payment"]) + " Monthly Payment")
    pyplot.xlabel("Month Number")
    pyplot.ylabel("Principal of Loan")

    pyplot.show()


print("Welcome to the Loan Calculator.\n")
month_number = 0

loan = get_loan_info()
starting_principal = loan["Principal"]
data_to_plot = []

show_loan_info(loan, month_number)

choose = input("\nPress 'Enter' to begin paying off your loan : \t")

while loan["Principal"] > 0:
    if loan["Principal"] > starting_principal: 
        break
    month_number += 1
    collect_interest(loan)
    make_monthly_payment(loan)
    
    data_to_plot.append((month_number, loan["Principal"]))
        
    show_loan_info(loan, month_number)

print("\n")
if (loan["Principal"]) <= 0 :
    summarize_loan(loan, month_number, starting_principal)
    create_graph(data_to_plot, loan)
else:
    print("Loan can never be paid off. Monthly payment is less than interest collected.")    











