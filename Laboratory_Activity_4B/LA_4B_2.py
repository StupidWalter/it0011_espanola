import csv

currency_csv = open('Laboratory_Activity_4B\\currency.csv', 'r')
currency_dictionary_cname = {}
currency_dictionary_rate = {}

csv_reader = csv.reader(currency_csv)
next(csv_reader)
for row in csv_reader:
    currency_dictionary_cname[row[0]] = row[1]
    currency_dictionary_rate[row[0]] = float(row[2])
currency_csv.close()

v_amount = float(input("How much dollar do you have? "))
v_currency = input("What currency do you want to have? ").upper()

if v_currency in currency_dictionary_cname:
    converted_amount = v_amount * currency_dictionary_rate[v_currency]
    print("Dollar:",v_currency, "USD")
    print(currency_dictionary_cname[v_currency], ": ", converted_amount, sep="")
else:
    print("Currency code inputted not found in the dictionary")



