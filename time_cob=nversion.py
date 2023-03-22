def to_seconds(houres, minutes, seconds):
    return hours*3600+minutes*60+seconds


print("Welcome to this time converter")

cont = "y"


while (cont.lower() == "y"):
    hours = int(input("Enter the number of hours"))
    minutes = int(input("Enter the number of minutes"))
    Seconds = int(input("enter number of minutes"))

    print("That's {} seconds". format(to_seconds(hours, minutes, seconds)))
    print()
    cont = input("Do you want to do another conversion? [ Y to continue]")
print("Good bye!")
