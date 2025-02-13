from datetime import datetime

date = input("Enter the date (mm/dd/yyyy): ")

if date[2] == "/" and date[5] == "/": 
    formal_date = datetime.strptime(date, "%m/%d/%Y")
    formal_date = formal_date.strftime("%B %d, %Y")
    print("Date Output:", formal_date)
else:
    print("Wrong date format. Please follow the instruction")