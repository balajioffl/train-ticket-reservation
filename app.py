from flask import Flask

app = Flask(__name__)

# creating a class for train details


class Train:
    def __init__(self, train_no, train_name, available_seats):
        self.train_no = train_no
        self.train_name = train_name
        self.available_seats = available_seats

    # method to display all the trains

    def display_AllTrains(self):
        print("\n--- Train Details ---")
        print(f"Train No: {self.train_no}")
        print(f"Train Name: {self.train_name}")
        print(f"Available Seats: {self.available_seats}")
        print("---------------------\n")

    # method to book_tickets

    def book_tickets(self, num_tickets):
        if num_tickets <= 0:
            print("Please enter a valid number of tickets.")

        if num_tickets <= self.available_seats:
            self.available_seats -= num_tickets
            print(
                f"Your {num_tickets} tickets have been booked! Remaining seats: {self.available_seats}"
            )
        else:
            print(f"only {self.available_seats} seats are available.")

    # methods to cancel tickets

    def cancel_tickets(self, num_tickets):
        if num_tickets <= 0:
            print("Please enter a valid number of tickets.")
        else:
            self.available_seats += num_tickets
            print(
                f"Your {num_tickets} tickets have been cancelled. Total available seats: {self.available_seats}"
            )


def main():

    # Create a list of four train objects

    trains = [
        Train(9094, "Trichy Express", 60),
        Train(1234, "Madurai Express", 100),
        Train(5678, "Chennai Express", 50),
        Train(4321, "Kovai Express", 75),
    ]

    while True:
        print("--- Main Menu ---")
        print("1. View Train Details")
        print("2. Book Tickets")
        print("3. Cancel Tickets")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            for train in trains:
                train.display_AllTrains()

        elif choice == "2":
            try:
                train_no = int(input("Enter train number: "))
                for train in trains:
                    if train.train_no == train_no:
                        num_tickets = int(input("Enter number of tickets to book: "))
                        train.book_tickets(num_tickets)
                        break
                else:
                    print("Invalid train number. Booking failed.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == "3":
            try:
                train_no = int(input("Enter train number: "))
                for train in trains:
                    if train.train_no == train_no:
                        num_tickets = int(input("Enter number of tickets to cancel: "))
                        train.cancel_tickets(num_tickets)
                        break
                else:
                    print("Invalid train number. Cancellation failed.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == "4":
            print("Exiting application. byee! ")
            break

        else:
            print("Invalid choice. Please select a number from 1 to 4.")


if __name__ == "__main__":
    main()
