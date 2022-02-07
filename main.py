"""
Calculating correlation between average degrees on fist day in a year and the yield of crop
author: Alex Olivier Michaud
"""
import pandas as pd
import matplotlib.pyplot as plt

vynos_1998_2019 = [4.21, 4.65, 4.21, 4.85, 4.56, 4.07, 5.84, 5.05, 4.49, 4.86, 5.77,
                   5.24, 4.99, 5.69, 4.32, 5.67, 6.51, 6.36, 6.50, 5.67, 6.39, 5.73]    #list of yield
teploty_1998_2019 = [-0.5, -0.6, -6.7, -4.65, -9.4, -8.55, -1.8, 2.03, -0.63, 4.20,
                     -1.6, -5.6, 3, -2.4, 0.3, 0.5, 2.4, -2.8, -3.4, -4.7, 1.5, 3.9]    #list of degrees
vynos = pd.Series([4.21, 4.65, 4.21, 4.85, 4.56, 4.07, 5.84, 5.05, 4.49, 4.86, 5.77,
                   5.24, 4.99, 5.69, 4.32, 5.67, 6.51, 6.36, 6.50, 5.67, 6.39, 5.73])   #list of yield using pandas
teploty = pd.Series([-0.5, -0.6, -6.7, -4.65, -9.4, -8.55, -1.8, 2.03, -0.63, 4.20,
                     -1.6, -5.6, 3, -2.4, 0.3, 0.5, 2.4, -2.8, -3.4, -4.7, 1.5, 3.9])   #list of degrees using pandas

data = {"teploty": [-0.5, -0.6, -6.7, -4.65, -9.4, -8.55, -1.8, 2.03, -0.63, 4.20,
                     -1.6, -5.6, 3, -2.4, 0.3, 0.5, 2.4, -2.8, -3.4, -4.7, 1.5, 3.9],
        "vynos": [4.21, 4.65, 4.21, 4.85, 4.56, 4.07, 5.84, 5.05, 4.49, 4.86, 5.77,
                   5.24, 4.99, 5.69, 4.32, 5.67, 6.51, 6.36, 6.50, 5.67, 6.39, 5.73]        #degrees and yield in one dict
}
dataframe = pd.DataFrame(data, columns=["teploty", "vynos"])    #making pandas dataframe from data
print(dataframe)    #printing dataframe + corellation under it
print(dataframe.corr()) #--> https://datatofish.com/correlation-matrix-pandas/

dataframe_vynos = vynos.corr(teploty) #-->https://realpython.com/numpy-scipy-pandas-correlation-python/#example-pandas-correlation-calculation
dataframe_teploty = teploty.corr(vynos)     #calculation of degrees and yield correlation
plt.matshow(dataframe.corr()) #--> https://stackoverflow.com/questions/29432629/plot-correlation-matrix-using-pandas
plt.show()      #making and showing graf between 

