day = int(input("Enter a day of the week > "))
if day in range(6, 8):
    print("Yes! Have a nice weekend!")
elif day in range(1, 6):
    print("No! Working")
else:
    print("Wrong input!")
