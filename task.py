from abc import ABC, abstractmethod

class HotelOffering(ABC):
    def __init__(self, name, base_price):
        self._name = name
        self._base_price = base_price  

    @abstractmethod
    def calculate_item_cost(self):
        pass

    @abstractmethod
    def display_details(self):
        pass

    
    def get_price(self):
        return self._base_price

    def set_price(self, new_price):
        if new_price < 0:
            print("Invalid price. Must be non-negative.")
        else:
            self._base_price = new_price

class HotelRoom(HotelOffering):
    def __init__(self, name, base_price, bed_size, smoking_allowed=False):
        super().__init__(name, base_price)
        self.bed_size = bed_size
        self.smoking_allowed = smoking_allowed

    def calculate_item_cost(self):
        
        return self.get_price() * 1.15

    def display_details(self):
        return f"Room: {self._name} | Bed: {self.bed_size} | Smoking: {self.smoking_allowed} | Rate: ${self.get_price():.2f}"


class SpaService(HotelOffering):
    def __init__(self, name, base_price, duration_minutes):
        super().__init__(name, base_price)
        self.duration_minutes = duration_minutes

    def calculate_item_cost(self):
      
        return self.get_price() * 1.20

    def display_details(self):
        return f"Spa Service: {self._name} | Duration: {self.duration_minutes} mins | Fee: ${self.get_price():.2f}"

class CustomerReservation:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"✅ Added: {item._name}")

    def view_reservation(self):
        if not self.items:
            print("Reservation is empty.")
        else:
            print("\n--- Current Reservation ---")
            for i, item in enumerate(self.items, 1):
                print(f"[{i}] {item.display_details()}")
            print("---------------------------\n")

    def print_final_bill(self):
        print("\n====== Hotel Folio ======")
        total = 0
        for item in self.items:
            cost = item.calculate_item_cost()
            print(f"{item._name}: ${cost:.2f}")
            total += cost
        print("-------------------------")
        print(f"TOTAL DUE: ${total:.2f}")
        print("=========================\n")



def main():
   
    offerings = {
        "R1": HotelRoom("Deluxe King Room", 200, "King", False),
        "R2": HotelRoom("Queen Room", 150, "Queen", True),
        "S1": SpaService("Full Body Massage", 100, 60),
        "S2": SpaService("Facial Treatment", 80, 45),
    }

    reservation = CustomerReservation()

    while True:
        print("\n🏨 Smart Hotel Booking System")
        print("[1] View Hotel Offerings")
        print("[2] Add to Reservation")
        print("[3] View Reservation")
        print("[4] Print Final Bill")
        print("[5] Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            print("\n--- Hotel Offerings ---")
            for oid, item in offerings.items():
                print(f"ID: {oid} | {item.display_details()}")
            print("-----------------------\n")

        elif choice == "2":
            oid = input("Enter Offering ID: ").strip()
            if oid in offerings:
                reservation.add_item(offerings[oid])
            else:
                print("Invalid ID. Please try again.")

        elif choice == "3":
            reservation.view_reservation()

        elif choice == "4":
            reservation.print_final_bill()

        elif choice == "5":
            print(" Thank you for visiting. Goodbye!")
            break

        else:
            print("Invalid input. Please enter a number between 1–5.")


if __name__ == "__main__":
    main()
