# Monthly Carpool Expense Splitter
# Members: Alli, Rupert, Geu
# Features:
# - Calculates monthly carpool expenses, divides cost among passengers
# - Shows percentage breakdown of total expenses
# - Shows per-passenger peso breakdown (fuel, fee, maintenance)
# - Tracks multiple months and displays average monthly cost per passenger

def CalculateTotal(fuel_cost, driving_fee, maintenance_cost):
    """Adds all costs"""
    return fuel_cost + driving_fee + maintenance_cost

def DisplayResults(total, passengers, fuel_cost, driving_fee, maintenance_cost):
    """Displays total cost, each passenger's share, and breakdowns"""
    # Percentages of total expenses
    fuel_percent = (fuel_cost / total) * 100
    fee_percent = (driving_fee / total) * 100
    maintenance_percent = (maintenance_cost / total) * 100

    # Each passenger's total share
    share = total / passengers

    # Per-passenger breakdown in pesos
    passenger_fuel = fuel_cost / passengers
    passenger_fee = driving_fee / passengers
    passenger_maintenance = maintenance_cost / passengers

    print(f"\nTotal Monthly Cost: ₱{total:.2f}")
    print(f"Each Passenger Pays: ₱{share:.2f}")
    print(f"  ↳ Fuel: ₱{passenger_fuel:.2f}  |  Fee: ₱{passenger_fee:.2f}  |  Maintenance: ₱{passenger_maintenance:.2f}")
    print(f"Percentage of total expenses:")
    print(f"  Fuel: {fuel_percent:.1f}%  |  Fee: {fee_percent:.1f}%  |  Maintenance: {maintenance_percent:.1f}%")
    
    return share  # return per-passenger cost for averaging later

# Store monthly per-passenger costs for averaging
monthly_passenger_costs = []

while True:
    try:
        total_people = int(input("Enter total number of people (driver + passengers): "))
        passengers = total_people - 1
        if passengers <= 0:
            print("Invalid number of passengers. Must have at least 1 passenger. Try again.")
            continue

        fuel_cost = float(input("Enter monthly fuel cost: "))
        driving_fee = float(input("Enter monthly driving fee: "))
        maintenance_cost = float(input("Enter monthly maintenance cost: "))

        total = CalculateTotal(fuel_cost, driving_fee, maintenance_cost)
        per_passenger = DisplayResults(total, passengers, fuel_cost, driving_fee, maintenance_cost)
        
        # Store this month's per-passenger cost
        monthly_passenger_costs.append(per_passenger)

        repeat = input("\nCalculate another month? (yes/no): ").lower()
        if repeat != "yes":
            # Show average across all months
            if monthly_passenger_costs:
                avg_cost = sum(monthly_passenger_costs) / len(monthly_passenger_costs)
                print(f"\n--- Summary over {len(monthly_passenger_costs)} month(s) ---")
                print(f"Average monthly cost per passenger: ₱{avg_cost:.2f}")
            print("Thank you for using Smart Monthly Carpool Expense Splitter!")
            break

    except ValueError:
        print("Invalid input. Please enter numbers only.")
