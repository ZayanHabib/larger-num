try:
    print("Hello Please Enter Three Numbers And This Program Will Figure Out Which Number Is Larger")
    number1 = int(input("Please Enter Number 1\n:"))
    number2 = int(input("Please Enter Number 2\n:"))
    number3 = int(input("Please Enter Number 3\n:"))
    if number1 == number2 or number1 == number3 or number2 == number3:
        print("Numbers Should not be same")
    else:
        if number1 > number2 and number1 > number3:
            print(f"Number 1 is larger which is {number1}")
        elif number2 > number1 and number2 > number3:
            print(f"Number 2 is larger which is {number2}")
        elif number3 > number1 and number3 > number2:
            print(f"Number 3 is larger which is {number3}")
except Exception as e:
    print(f"Some Error Occurred Which Is : {e}")