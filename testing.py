total_data = 0
total_absent = 0
while True:
    total_data += 1
    absence = int(input("Absent: "))
    total_absent = total_absent + absence

average = total_absent / total_data
print(average)
