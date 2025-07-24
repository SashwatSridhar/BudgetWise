#Libraries:




#get user input
income = float(input("Please enter your monthly income: "))
print("Income is: $" +str(income))

#rule type
print("\nWe will now be using the 50/30/20 Rule. " \
 "\n50% of income is needs(housing, utilities, groceries, transportation, minimum debt payments)," \
 "\n30% to wants (entertainment, dining out, hobbies, subscriptions)," \
 "\n20% to savings and debt repayment")

#implementing the 50/30/20 rule
needs = income*0.50
wants = income*0.3
savings = income*0.2

#printing exact values based on the rule
print("\n here is where your money should be going:" \
 f"\n needs:  ${needs: .2f}"\
 f"\n wants: ${wants: .2f}"\
 f"\n savings: ${savings: .2f}")

#list of keywords in needs, wants, savings
needs_keywords = ["rent", "groceries", "utilities", "transportation"]
wants_keywords = ["entertainment", "dining out", "hobbies", "subscriptions"]
savings_keywords = ["investment", "emergency fund"]

#prompt user to enter their expenses one by one
print("\n please enter your expenses description")
expenses_description = [e for e in input().split(",")] 

print("\n please enter your expenses amounts")
expenses_amounts = [float(e) for e in input().split(",")]


#create an AI model that takes the expenses input and searches for keywords in the list to determine the category
#returns which category the expense belongs to 

#first use rule-based approach
needs_list = []
needs_expenses = 0

wants_list = []
wants_expenses = 0

savings_list = []
savings_expenses = 0

#needs
for i, e in enumerate(expenses_description):
    for keywords in needs_keywords:
        if keywords in e:
            #add in needs list
            needs_list.append(e)
            needs_expenses += expenses_amounts[i]
            break
#wants
for i, e in enumerate(expenses_description):
    for keywords in wants_keywords:
        if keywords in e:
            #add in needs list
            wants_list.append(e)
            wants_expenses += expenses_amounts[i]
            break
#savings
for i, e in enumerate(expenses_description):
    for keywords in savings_keywords:
        if keywords in e:
            #add in needs list
            savings_list.append(e)
            savings_expenses += expenses_amounts[i]
            break

expense_details = " "
for description, amount in zip(expenses_description, expenses_amounts):
    expense_details += (f"{description}: ${amount:.2f}")

needs_details = " "
for description in needs_list:
    index = expenses_description.index(description)
    amount = expenses_amounts[index]
    needs_details += (f"{description}: ${amount:.2f}\n")

wants_details = " "
for description in wants_list:
    index = expenses_description.index(description)
    amount = expenses_amounts[index]
    wants_details += (f"{description}: ${amount:.2f}\n")

savings_details = " "
for description in savings_list:
    index = expenses_description.index(description)
    amount = expenses_amounts[index]
    savings_details += (f"{description}: ${amount:.2f}\n")

#print statements
print("\n===== BUDGET BREAKDOWN =====")

print("\n NEEDS CATEGORY:")
print(f"{needs_details}")
print(f"TOTAL NEEDS: ${needs_expenses:.2f}")

print("\n WANTS CATEGORY:")
print(f"{wants_details}")
print(f"TOTAL WANTS: ${wants_expenses:.2f}")

print("\n SAVINGS CATEGORY:")
print(f"{savings_details}")
print(f"TOTAL SAVINGS: ${savings_expenses:.2f}")

print("\n===== SUMMARY =====")
total_expenses = needs_expenses + wants_expenses + savings_expenses
print(f"Total Expenses: ${total_expenses:.2f}")
print(f"Needs: ${needs_expenses:.2f} ({(needs_expenses/total_expenses*100):.1f}%)")
print(f"Wants: ${wants_expenses:.2f} ({(wants_expenses/total_expenses*100):.1f}%)")
print(f"Savings: ${savings_expenses:.2f} ({(savings_expenses/total_expenses*100):.1f}%)")

#use naives bayes

#use random forest


