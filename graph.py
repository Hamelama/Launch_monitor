import csv
import matplotlib.pyplot as plt

velocities = []
dataPoints = []

with open('velocity_values.csv') as csvfile:
    csvReader = csv.reader(csvfile)
    i = 0
    for velocity in csvfile:
        velocities.append(float(velocity))
        
        dataPoints.append(i)
        i = i + 1

        
plt.plot(dataPoints, velocities)
plt.show()


max_velocity = max(velocities)
fig, ax  = plt.subplots()

ax.bar([1], [max_velocity], width=0.35,
       tick_label=['Maxhastighet'], align='center')
plt.show()
