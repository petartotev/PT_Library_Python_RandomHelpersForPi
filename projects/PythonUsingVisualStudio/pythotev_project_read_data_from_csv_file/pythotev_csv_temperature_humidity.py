"""
Project is a beginners' guide to manipulating data extracted from .csv files.
.csv file was generated from [AdventureWorks2019].[Person].[Person]
"""

import matplotlib.pyplot as plt
import csv
  
x = []
y = []
  
with open('C:/Projects/PT_Library_Python_UltimatePythotev/projects/PythonUsingVisualStudio/pythotev_project_read_data_from_csv_file/res/temp_1.csv','r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        x.append(row[0])
        y.append(float(row[1])) # temperature
        #y.append(float(row[2])) # humidity

plt.plot(x, y, color = 'r', linestyle = 'dashed', marker = 'o',label = "temperature")  
#plt.plot(x, y, color = 'b', linestyle = 'dashed', marker = 'o',label = "humidity")  
plt.xticks(rotation = 90)
plt.xlabel('Date')
plt.ylabel('Temperature(°C)')
#plt.ylabel('Humidity(%)')
plt.title('Weather Report', fontsize = 20)
plt.grid()
plt.legend()
plt.show()