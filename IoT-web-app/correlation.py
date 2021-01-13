import pandas as pd
import numpy as np

def histogram_intersection(a, b):
    v = np.minimum(a, b).sum().round(decimals=1)
    return v
def check_correlation(data1, data2):
    series1 = pd.Series(data1)
    series2 = pd.Series(data2)
    correlation = series1.corr(series2, method='pearson')
    return correlation
s1 = pd.Series([.2, .0, .6, .2])
s2 = pd.Series([.3, .6, .0, .1])
test1 = pd.Series([94, 77, 202, 94, 62, 118, 201])
test2 = pd.Series([0.9614494450000003, -0.768485426902771, -0.917514443397522, -2.0241364240646362, -2.038912057876587, -2.1486033179999997, 1.9097046850000003])

test = test1.corr(test2, method='pearson')

