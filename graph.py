import csv
import matplotlib.pyplot as plt

speed_values = []
dataPoints = []

with open('velocity_values.csv') as csvfile:
    csvReader = csv.reader(csvfile)
    i = 0
    for row in csvReader:
        # the first element in the row, row[0] is velocity
        speed_values.append(float(row[0]))
        
        dataPoints.append(i)
        i = i + 1

        
plt.plot(dataPoints, speed_values)

plt.xlabel('Data points')
plt.ylabel('Speed (mph)')
plt.title('Test 1 - Simulated golf club, Range 0.7m - 1.3m')

plt.show()

max_speed = max(speed_values)


cells = []
cells.append(["Maximum Speed", str(round(max_speed, 2)) + " mph"])
table = plt.table(cellText=cells, cellLoc='right', loc = "center")
table.scale(1,6)
table.set_fontsize(24)


plt.axis('off') # No axes are needed for a table
plt.title("Results", fontdict = {'fontsize': 24}, y=0.7)
plt.show()
