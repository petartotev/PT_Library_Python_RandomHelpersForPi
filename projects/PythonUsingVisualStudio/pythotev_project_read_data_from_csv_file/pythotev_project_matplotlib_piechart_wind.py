"""
matplotlib pie wind direction
"""

import matplotlib.pyplot as plt
import csv

c = []

with open('C:/Projects/PT_Library_Python_UltimatePythotev/projects/PythonUsingVisualStudio/pythotev_project_read_data_from_csv_file/res/wind.csv','r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        c.append(row[4]) # temperature

directions = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']
quantity = [c.count('N'), c.count('NNE'), c.count('NE'), c.count('ENE'), c.count('E'), c.count('ESE'), c.count('SE'), c.count('SSE'),
            c.count('S'), c.count('SSW'), c.count('SW'), c.count('WSW'), c.count('W'), c.count('WNW'), c.count('NW'), c.count('NNW')]

for i in reversed(range(len(quantity))):
    if quantity[i] == 0:
        print(i)
        del quantity[i]
        del directions[i]

#explode = (0.05, 0.04, 0.03, 0.02, 0.01)
colors=['olivedrab', 'rosybrown', 'gray', 'saddlebrown']

fig1, ax1 = plt.subplots()
ax1.pie(quantity, labels=directions, autopct='%1.1f%%', shadow=False, startangle=90, textprops={'fontsize': 12})
#ax1.pie(quantity, labels=directions, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title('Wind direction | 2023-04-26 - 2023-04-29', fontsize = 15, y=1.05)
plt.grid()
plt.legend()

plt.show()