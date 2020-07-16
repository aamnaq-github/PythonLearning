file = open("Employees.txt", "a")
file.write("Kelly - Customer Services\n")
file.close()
file = open("Employees.txt", "r")
for line in file.readlines():
    print(line)

file.close()
