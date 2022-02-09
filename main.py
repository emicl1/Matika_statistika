"""
Calculating correlation between average degrees on fist day in a year and the yield of crop
author: Alex Olivier Michaud
"""
import pandas as pd
import matplotlib.pyplot as plt
import Seaborn as sns

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
        "vynos_pšenice": [4.21, 4.65, 4.21, 4.85, 4.56, 4.07, 5.84, 5.05, 4.49, 4.86, 5.77,
                        5.24, 4.99, 5.69, 4.32, 5.67, 6.51, 6.36, 6.50, 5.67, 6.39, 5.73],        #degrees and yield in one dict
        "vynos_ječmen": [3.62, 3.94, 3.29, 3.97, 3.67, 3.76, 4.97, 4.21, 3.59, 3.80, 4.65,
                         4.40, 4.07, 4.87, 4.23, 4.57, 5.61, 5.44, 5.67, 5.23, 4.95, 5.38 ],
        "vynos_kukuřice_siláž": [34.56, 32.52, 33.13, 32.81, 32.39, 27.55, 30.26, 35.69, 32.66, 34.41, 35.33,
                                 38.15, 33.04, 41.79, 40.60, 32.66, 40.37, 29.13, 40.72, 34.84, 29.84, 35.47],
        "vynos_žito": [3.63, 3.67, 3.42, 3.72, 3.37, 3.80, 5.29, 4.19, 3.33, 4.73, 4.83 ,
                       4.63, 3.91, 4.74, 4.81, 4.70, 5.13, 4.91, 4.98, 4.92, 4.74, 5.06]
        }
dataframe = pd.DataFrame(data, columns=["teploty", "vynos_pšenice", "vynos_ječmen", "vynos_kukuřice_siláž", "vynos_žito"])    #making pandas dataframe from data
print(dataframe)    #printing dataframe + corellation under it
correlation = (dataframe.corr()) #--> https://datatofish.com/correlation-matrix-pandas/
print(correlation)
"""
dataframe_vynos = vynos.corr(teploty) #-->https://realpython.com/numpy-scipy-pandas-correlation-python/#example-pandas-correlation-calculation
dataframe_teploty = teploty.corr(vynos)     #calculation of degrees and yield correlation"""
plt.matshow(correlation) #--> https://stackoverflow.com/questions/29432629/plot-correlation-matrix-using-pandas

plt.show()      #making and showing graf between 

