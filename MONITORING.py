# monitoring.py
# Smart Monitoring System for Vidyut Project
# Tracks sewage waste across plants and suggests transfers to optimize usage.

def main():
    # Step 1: Define plants (can be dynamic; here, example from report: Panvel=0, Kharghar=1, Vashi=2)
    # Assume order implies proximity (e.g., 0 closest to 1, etc.). Distances could be added later.
    plant_names = ["Panvel", "Kharghar", "Vashi"]  # Add more as needed
    num_plants = len(plant_names)

    # Step 2: Input capacities and loads (in tons/day or similar units)
    capacities = []
    loads = []
    print("Enter data for each plant (capacity and load):")
    for i in range(num_plants):
        cap = float(input(f"{plant_names[i]} Capacity: "))
        load = float(input(f"{plant_names[i]} Load: "))
        capacities.append(cap)
        loads.append(load)

    # Step 3: Calculate balances (load - capacity)
    balances = {plant_names[i]: loads[i] - capacities[i] for i in range(num_plants)}

    # Step 4: Separate surplus (positive balance) and deficit (negative balance)
    surplus = {plant: bal for plant, bal in balances.items() if bal > 0}
    deficit = {plant: -bal for plant, bal in balances.items() if bal < 0}  # Convert to positive need

    # Sort surplus by descending amount (largest first), deficit by descending need
    surplus_sorted = sorted(surplus.items(), key=lambda x: x[1], reverse=True)
    deficit_sorted = sorted(deficit.items(), key=lambda x: x[1], reverse=True)

    # Step 5: Greedy matching - For each deficit, pull from surplus until filled
    transfers = []
    for def_plant, need in deficit_sorted:
        remaining_need = need
        for i in range(len(surplus_sorted)):
            sur_plant, avail = surplus_sorted[i]
            if avail <= 0:
                continue
            transfer_amount = min(remaining_need, avail)
            if transfer_amount > 0:
                transfers.append(f"Transfer {transfer_amount:.2f} units from {sur_plant} to {def_plant}")
                surplus_sorted[i] = (sur_plant, avail - transfer_amount)  # Update remaining surplus
                remaining_need -= transfer_amount
            if remaining_need <= 0:
                break
        if remaining_need > 0:
            transfers.append(f"Warning: {def_plant} still needs {remaining_need:.2f} units (insufficient surplus)")

    # Step 6: Output results
    print("\nBalances:")
    for plant, bal in balances.items():
        status = "Surplus" if bal > 0 else "Deficit" if bal < 0 else "Sufficient"
        print(f"{plant}: Balance = {bal:.2f} ({status})")

    print("\nTransfer Suggestions:")
    if not transfers:
        print("No transfers needed - all plants are balanced.")
    else:
        for msg in transfers:
            print(msg)

if __name__ == "__main__":
    main()