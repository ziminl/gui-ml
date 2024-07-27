import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

height = [100,110,120,130,140]
foot_size = [200,210,220,230,240]
print(len(foot_size), len(height))

plt.scatter(foot_size, height)
plt.xlabel('footsize')
plt.ylabel('height')
plt.show

#np conv 
x = np.array(foot_size)
#print(x) -> [200 210 220 230 240]
y = np.array(height)

#least squares
a = np.sum((y-np.mean(y))*(x-np.mean(x))) #a(acceleration)
a = a/np.sum((x-np.mean(x))**2)
b = np.mean(y) - a*np.mean(x)
print('a(acceleration)',a,'b(yaxis)',b)


