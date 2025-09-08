# Can you change self parameter inside a class to something else (say "om"). Try changing self to "slf" or "om" and see the effects.

from random import randint


class Train:
    def __init__(om, trainNo):
        om.trainNo = trainNo

    def book(om, fro, to):
        print(f"Ticket is booked in train no: {om.trainNo} from {fro} to {to}")

    def fare(om, fro, to):
        print(f"Ticket Fare in Train No: {om.trainNo} is {randint(1500,5000)}")

    def status(om):
        print(f"{om.trainNo} is running on time.")


t = Train(12945)
t.book("Surat", "Amritsar")
t.status()
t.fare("Surat", "Amritsar")

# self can be changed to slf or om or anything else but not preffered to do as readibility degrades.
