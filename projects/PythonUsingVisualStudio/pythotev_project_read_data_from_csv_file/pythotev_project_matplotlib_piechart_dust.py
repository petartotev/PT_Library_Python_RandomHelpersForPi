"""
matplotlib pie wind direction
"""

import matplotlib.pyplot as plt
import csv

c = []

with open('C:/Projects/PT_Library_Python_UltimatePythotev/projects/PythonUsingVisualStudio/pythotev_project_read_data_from_csv_file/res/dust.csv','r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        c.append(row[2]) # temperature

#explode = (0.05, 0.04, 0.03, 0.02, 0.01, 0.00)
colors=['lime', 'yellow', 'gold', 'orangered', 'red', 'darkred']
aqi = ['G', 'M', 'UfSG', 'U', 'VU', 'H']
aqi_explicit = ['Good', 'Moderate', 'Unhealthy for Sensitive Groups', 'Unhealthy', 'Very Unhealthy', 'Hazardous']
quantity = [c.count('G'), c.count('M'), c.count('UfSG'), c.count('U'), c.count('VU'), c.count('H')]

for i in reversed(range(len(quantity))):
    if quantity[i] == 0:
        print(i)
        del aqi[i]
        del aqi_explicit[i]
        del quantity[i]
        del colors[i]

fig1, ax1 = plt.subplots()
ax1.pie(quantity, labels=aqi_explicit, autopct='%1.1f%%', shadow=True, startangle=90, textprops={'fontsize': 12}, colors=colors)
#ax1.pie(quantity, labels=aqi, autopct='%1.1f%%', shadow=True, startangle=90, explode=explode)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title('2023-04 | Dust AQI', fontsize = 15, y=1.05)
plt.grid()
plt.legend()

plt.show()
