import csv

with open("Day54Totals.csv") as file:
    
    reader = csv.DictReader(file)
    total  = 0.0
    for row in reader: 
        total_per_day = float(row["Cost"]) * int(row["Quantity"])
        print(f"Cost: ${row['Cost']}   Quantity: {row['Quantity']}   Total: {total_per_day}")
        total += total_per_day
    print()
    print()
    print(f"Total: ${round(total,2)}")
