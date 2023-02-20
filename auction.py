while True:
    bad_answer = False
    ah_item = input("What is the auction for? ")
    try:
        reserve = int(input("What is the reserve price? "))
        if reserve < 0:
            raise ValueError

    except ValueError:
        bad_answer = True
        print("Invalid answer try again")
    if bad_answer is not True:
        bid = 0
        current_price = 0
        while bid != -1:
            bid = int(input(f"(Current price {current_price})\nYour bid for {ah_item}:"))
            if bid > current_price:
                print("Bid success")
                current_price = bid
            elif bid < current_price:
                print("Your bid was lower than the current price")
        if reserve < current_price:
            print(f"{ah_item} sold successfully at {current_price:.2f}$")
        elif reserve < current_price:
            print(f"{ah_item} didn't meet the {reserve:.2f}$")
