def int_check():
    try:
        speed = int(input("Enter the amount over the speed limit"))
        if speed == 0:
            raise ValueError
        return True
    except ValueError:
        print("Invalid")
        return False


print("#############")
name = input("Enter name of speeder: ").title()
while int_check is not True:
    pass
