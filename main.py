# Monthly Carpool Expense Splitter
# Members: Alli, Rupert, Geu
# Description: Calculates monthly carpool expenses, divides cost among passengers, and shows percentage breakdown.

def CalculateTotal(fuel_cost, driving_fee, maintenance_cost):
  # Adds all costs
   return fuel_cost + driving_fee + maintenance_cost
  
def DisplayResults(total, passengers, fuel_cost,driving_fee, maintenance_cost):
  # Calculates percentages
    fuel_percent = (fuel_cost / total) * 100
    fee_percent = (driving_fee / total) * 100
    maintenance_percent = (maintenance_cost / total) * 100
    share = total / passengers
    print(f"\nTotal Monthly Cost: ₱{total}")
    print(f"Each Passenger Pays: ₱{share:.2f}")
    print(f"Fuel: {fuel_percent:.1f}% | Fee: {fee_percent:.1f}% | Maintenance: {maintenance_percent:.1f}%")

while True:
  try:
    total_people = int(input("Enter total number of people (driver + passengers): "))
    passengers = total_people - 1
    if passengers <= 0:
      print("Invalid number of passengers. Try again.")
      continue

    fuel_cost = float(input("Enter monthly fuel cost: "))
    driving_fee = float(input("Enter monthly driving fee: "))
    maintenance_cost = float(input("Enter monthly maintenance cost: "))

     total = CalculateTotal(fuel_cost, driving_fee, maintenance_cost)
     DisplayResults(total, passengers, fuel_cost, driving_fee, maintenance_cost)

     repeat = input("\nCalculate another month? (yes/no): ").lower()
     if repeat != "yes":
       print("Thank you for using Smart Monthly Carpool Expense Splitter!")
            break

except ValueError:
    print("Invalid input. Please enter numbers only.")
