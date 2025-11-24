#Wlecome Message
print("Welcome to my Python program!")

#Ask user for sales account
sales = input("How much money did you make this month?")

#Convertiing sales into float
try: 
    sales = float(sales)
except ValueError:
    print("Please enter a valid number for sales.")
    exit()

#Calculate Progress
goal = 10000.0
progress = (sales / goal) * 100

#Display final message
print(f"You have achieved {progress} % of your sales goal this month!")