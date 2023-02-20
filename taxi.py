drivers_name = input("What is the drivers name:")
total_cost = 0
trips_taken = 0
total_minutes = 0
while True:
    start_trip = input("Do you want to start a new trip\n"
                       "(Y)es or (N)o: ").lower()
    if start_trip[0] == "y":
        try:
            minutes = int(input("How much time did the trip take in minutes: "))
            cost = (minutes * 2) + 10
            total_cost += cost
            trips_taken += 1
            total_minutes += minutes
        except:
            print("Invalid answer")
    elif start_trip[0] == "n":
        print(f"Drivers name: {drivers_name}\n"
              f"Total time: {total_minutes}\n"
              f"Average time for each trip: {total_minutes / trips_taken}\n"
              f"Total cost: {total_cost}\n"
              f"Average cost all trips: {total_cost / trips_taken}")
        exit(20)

    else:
        print("Invalid option")
