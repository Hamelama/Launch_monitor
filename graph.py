import csv
import matplotlib.pyplot as plt
import numpy as np
from shutil import copy
testnr = '0';
copy('velocity_values.csv', 'Measurements/velocity_values' + testnr +'.csv')

speed_values = []
dataPoints = []

with open('velocity_values.csv') as csvfile:
    csvReader = csv.reader(csvfile)
    
    print(next(csvReader))
    i = 0
    for row in csvReader:
        # the first element in the row, row[0] is velocity
        value = float(row[0])
        # Om ni får för många värden, filtrera bort under en viss fart
        if value not in speed_values:
            speed_values.append(float(row[0]))    
        
        


for i in range(0, len(speed_values)):
    nr = str(i+1)
    dataPoints.append('$v_{' + nr + '}$')
        
measured_speeds = speed_values
measure_no = dataPoints

plt.xticks(np.arange(0, len(dataPoints)+1, step=1))
plt.ylabel('Speed (mph)')
plt.title('Test number ' + str(testnr))
plt.bar(measure_no, measured_speeds)
plt.show()


#plt.plot(dataPoints, speed_values, 'o')

##plt.xlabel('Speed point')
##plt.ylabel('Speed (mph)')
##plt.title('Test - ' + str(testnr))
##plt.savefig('Grafer/Test_' + str(testnr))
##plt.show()

max_speed = max(speed_values)


cells = []
cells.append(["Maximum Speed", str(round(max_speed, 2)) + " mph"])
table = plt.table(cellText=cells, cellLoc='right', loc = "center")
table.scale(1,6)
table.set_fontsize(24)


plt.axis('off') # No axes are needed for a table
plt.title("Results", fontdict = {'fontsize': 24}, y=0.7)
plt.show()
