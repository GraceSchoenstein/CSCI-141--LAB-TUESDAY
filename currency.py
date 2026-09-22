choice = input("Choose to convert to 1. EUR 2. GBP 3. CNY 4. INR : ")

amount = input("Enter dollar amount to exchange:  ")

dollars = float(amount.replace("$", ""))


if choice == "1":
    currency = "EUR"
    rate = 1.08
elif choice == "2":
    currency = "GBP"
    rate = 1.21
elif choice == "3":
    currency = CNY 
    rate =  0.15
else:
    currency = "INR"
    rate = 0.012

after_fees = dollars * .95

converted = round(after_fees / rate)

print(f"After fees you will receive {currency} {converted}")

#input makes you type something in

