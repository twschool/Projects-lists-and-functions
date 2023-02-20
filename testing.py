staff_data = {"Alice Wonder": 6, "Simon White": 0, "John Johnathon": 4}
sorted_data_list = sorted(staff_data)
sorted_data = {}

for item in sorted_data_list:
    print(f"{item}:\t {staff_data.get(item)}")

# Who needs to format when you have \t

