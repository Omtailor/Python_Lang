# Write a class Train which has methods to book a ticket, get status of no of seats and fare information of train running

from random import randint


class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")

    def fare(self, fro, to):
        print(f"Ticket Fare in Train No: {self.trainNo} is {randint(1500,5000)}")

    def status(self):
        print(f"{self.trainNo} is running on time.")


t = Train(12945)
t.book("Surat", "Amritsar")
t.status()
t.fare("Surat", "Amritsar")
