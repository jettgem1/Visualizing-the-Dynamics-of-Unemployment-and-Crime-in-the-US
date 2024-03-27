import csv

with open("us-unemployment.csv", newline="") as file:
    data = list(csv.reader(file))

print(data)

with open("us-unemployment-2.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Year", "State/Area", "Rate"])

    for i in range(0, len(data)):
        for j in range(0, len(data[0])):
            if i != 0 and j > 2:
                y = data[0][j]
                s = data[i][1]
                r = data[i][j]
                writer.writerow([y, s, r])
