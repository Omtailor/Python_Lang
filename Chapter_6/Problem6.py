# Input marks of 5 students and calculate his grade

marks1 = int(input("Enter marks of Subject 1: "))
marks2 = int(input("Enter marks of Subject 2: "))
marks3 = int(input("Enter marks of Subject 3: "))
marks4 = int(input("Enter marks of Subject 4: "))
marks5 = int(input("Enter marks of Subject 5: "))

total = marks1 + marks2 + marks3 + marks4 + marks5

percentage = total / 5

if percentage >= 90 and percentage <= 100:
    print("Grade: Exceptional")
elif percentage >= 80 and percentage < 90:
    print("Grade: A")
elif percentage >= 70 and percentage < 80:
    print("Grade: B")
elif percentage >= 60 and percentage < 70:
    print("Grade: C")
elif percentage >= 50 and percentage < 60:
    print("Grade: D")
else:
    print("Grade: F")
