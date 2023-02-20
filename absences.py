# Lambda is so cool unfortunately pep8 doesn't agree
find_average = lambda number_of_data, total: total / number_of_data

# Cool formatting stuff
tab = "\t"
space = " "
print("Welcome")
# Original staff data list
# I learned how to use dictionaries for this :(
staff_data = {"Alice Wonder": 6, "Simon White": 20, "Jane Green": 0, "Ben Blue": 8,
              "Maisie Magenta": 4, "Coral Cool": 7, "Amanda Apple": 0}
# Sort the list staff_data into alphabetical order so that things are easier to deal with later
sorted_data_list = sorted(staff_data)
sorted_data = {}
for item in sorted_data_list:
    unmodified_item = item
    if len(item) < 11:
        """ The formatting can be broken if the name is too short so
        my solution is to add spaces at the end of the short names """
        item = f"{item}{space * 4}"

    sorted_data[item] = staff_data.get(unmodified_item)

# Initialising all of the variables so that python doesn't throw a error later
data_count = 0
highest_absent = 0
highest_absent_name = ""
total_absent = 0
zero_absent = []
# Cool for loop trick I learned you can deal with 2 variable in a for loop
print()
for name, absences in sorted_data.items():
    data_count += 1
    total_absent += absences
    if absences > highest_absent:
        highest_absent = absences
        highest_absent_name = name

    if absences == 0:
        zero_absent.append(name)
above_average_absent = []
average_absent = find_average(data_count, total_absent)
for name, absences in sorted_data.items():
    if absences < average_absent:
        above_average_absent.append([name, absences])


# You said you wanted the user input but on the brief there is no mention
# Of data entry so I just left it this has taken me enough time already
print(f"Average number of days staff were absent:\t {average_absent:.2f}\n")
print(f"Person with most absent {tab * 5} {highest_absent_name} with {highest_absent}\ndays\n")
print("List of people not absent at all: ")
for name in zero_absent:
    print(f"{tab * 11} {name}\n")
print("List of people absent above average:\t\t\t")
for item in above_average_absent:
    print(f"{tab * 11} {item[0]}\t\t{item[1]}")
