import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv (r'C:\Users\andre\Documents\GitHub\MSE-353-Lab-01\D.csv')   #read the csv file (put 'r' before the path string to address any special characters in the path, such as '\'). Don't forget to put the file name at the end of the path + ".csv"
df.plot(kind='scatter',x='Angle',y='Intensity',s=1,color='red')
plt.savefig('D.png', dpi=300)
plt.show()