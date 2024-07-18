class Vehicle:
    def __init__(self, reg_num, vehicle_type, owner):
        self.registration_number = reg_num
        self.type = vehicle_type
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner

    def __str__(self):
        return f"Vehicle({self.registration_number}, {self.type}, {self.owner})"

def input_vehicle():
    reg_num = input("Enter registration number: ")
    vehicle_type = input("Enter vehicle type: ")
    owner = input("Enter owner's name: ")
    return Vehicle(reg_num, vehicle_type, owner)

def display_vehicles(vehicles):
    for vehicle in vehicles:
        print(vehicle)

if __name__ == "__main__":
    vehicles = []

    while True:
        print("\nMenu:")
        print("1. Add a new vehicle")
        print("2. Update vehicle owner")
        print("3. Display all vehicles")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            vehicle = input_vehicle()
            vehicles.append(vehicle)
        elif choice == '2':
            reg_num = input("Enter the registration number of the vehicle to update: ")
            new_owner = input("Enter the new owner's name: ")
            found = False
            for vehicle in vehicles:
                if vehicle.registration_number == reg_num:
                    vehicle.update_owner(new_owner)
                    found = True
                    print(f"Updated owner of vehicle {reg_num} to {new_owner}.")
                    break
            if not found:
                print(f"No vehicle found with registration number {reg_num}.")
        elif choice == '3':
            if vehicles:
                print("\nList of vehicles:")
                display_vehicles(vehicles)
            else:
                print("No vehicles to display.")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

