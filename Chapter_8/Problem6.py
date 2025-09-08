# Write  program to convert inches to cms

def inch_to_cms(inch):
    cms = (inch*2.54)
    return cms

inch = float(input("Enter number of inches: "))
x = inch_to_cms(inch)
print(f"{inch} inch is equivalent to {x} cms")