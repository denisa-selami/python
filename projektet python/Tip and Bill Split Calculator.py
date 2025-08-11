print("Welcome to the tip calculator")
bill = float(input("what was the totall bill? $"))
tip = int(input("whaqt percentage tip woud you like to give? 10 12 15"))
people = int(input("how many people would split the bill "))
bill_with_tip = tip / 100 + bill
print(bill_with_tip)
bill_per_person = bill_with_tip / people
final_amount = round(bill_per_person / people)
print(f"Each person should pay $ {final_amount}")

