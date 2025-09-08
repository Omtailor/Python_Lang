# Write a program whether student has passed or failed if it requires 33% in each subject to pass
# and 40% overall to pass.

m1 = int(input("Enter marks of subject 1: "))
m2 = int(input("Enter marks of subject 2: "))
m3 = int(input("Enter marks of subject 3: "))
m4 = int(input("Enter marks of subject 4: "))

if m1 < 33 or m2 < 33 or m3 < 33 or m4 < 33:
    print(
        "Sorry, you falied since you didn't scored above or equal to 33 in all subjects"
    )
else:
    percentage = (m1 + m2 + m3 + m4) / 4
    if percentage >= 40:
        print("Congratulations, You Passed!")
    else:
        print("Sorry, You Failed :)")
