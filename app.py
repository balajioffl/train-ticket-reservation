from flask import Flask

app = Flask(__name__)

# creating a class for train details


class Train:
    def __init__(self, train_no, train_name, available_seats):
        self.train_no = train_no
        self.train_name = train_name
        self.available_seats = available_seats
        self.booked_seats = 0

    # method to display all the trains

    def display_AllTrains(self):
        print("\n--- Train Details ---")
        print(f"Train No: {self.train_no}")
        print(f"Train Name: {self.train_name}")
        print(f"Available Seats: {self.available_seats}")
        print(f"Booked Seats: {self.booked_seats}")
        print("---------------------\n")

    # method to book_tickets

    def book_tickets(self, num_tickets):

        # validating tickets if cancel ticket count is less than or equal to zero

        if num_tickets <= 0:
            print("Please enter a valid number of tickets.")
            return

        # validating if tickets booked is exceeding available seats

        if num_tickets <= self.available_seats:
            self.available_seats -= num_tickets
            self.booked_seats += num_tickets
            print(
                f"Your {num_tickets} tickets have been booked! Remaining seats: {self.available_seats}"
            )
        else:
            print(f"Only {self.available_seats} seats are available.")

    # methods to cancel tickets

    def cancel_tickets(self, num_tickets):

        # validating tickets if cancel ticket count is less than or equal to zero

        if num_tickets <= 0:
            print("Please enter a valid number of tickets.")
            return

        # validation added if cancelling tickets without booking

        if self.booked_seats == 0:
            print("Cancellation failed. No tickets have been booked for this train.")
            return

        # validating if cancel ticket count is greater than booked seat count

        if num_tickets > self.booked_seats:
            print(
                f"Cancellation failed. You can only cancel up to {self.booked_seats} tickets."
            )
        else:
            self.available_seats += num_tickets
            self.booked_seats -= num_tickets
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

    # while loop for menu options

    while True:
        print("--- Main Menu ---")
        print("1. View Train Details")
        print("2. Book Tickets")
        print("3. Cancel Tickets")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        # display all trains

        if choice == "1":
            for train in trains:
                train.display_AllTrains()

        # book tickets

        elif choice == "2":
            try:
                train_no = int(input("Enter train number: "))
                found_train = None
                for train in trains:
                    if train.train_no == train_no:
                        found_train = train
                        break

                if found_train:
                    num_tickets = int(input("Enter number of tickets to book: "))
                    found_train.book_tickets(num_tickets)
                else:
                    print("Invalid train number. Booking failed.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        # cancel tickets

        elif choice == "3":
            try:
                train_no = int(input("Enter train number: "))
                found_train = None
                for train in trains:
                    if train.train_no == train_no:
                        found_train = train
                        break

                if found_train:
                    num_tickets = int(input("Enter number of tickets to cancel: "))
                    found_train.cancel_tickets(num_tickets)
                else:
                    print("Invalid train number. Cancellation failed.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        #  exit application

        elif choice == "4":
            print("Exiting application. byee! ")
            break

        # invalid input

        else:
            print("Invalid choice. Please select a number from 1 to 4.")


if __name__ == "__main__":
    main()
