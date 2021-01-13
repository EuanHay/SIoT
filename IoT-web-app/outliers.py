import numpy as np
import pandas as pd
from get_data import get_sleep_data


def detect_outlier(data_1):
    outliers = []
    threshold = 3
    mean_1 = np.mean(data_1)
    std_1 = np.std(data_1)

    for y in data_1:
        z_score = (y - mean_1) / std_1
        if np.abs(z_score) > threshold:
            outliers.append(y)
    return outliers

def get_outliers(array):
    x_accel = array[1]
    y_accel = array[2]
    z_accel = array[3]
    internal_mic = array[4]
    external_mic = array[5]

    x = detect_outlier(x_accel)
    y = detect_outlier(y_accel)
    z = detect_outlier(z_accel)
    restlessness = len(x) + len(y) + len(z)

    internal_disturbances = len(detect_outlier(internal_mic))
    external_disturbances = len(detect_outlier(external_mic))

    return [restlessness, internal_disturbances, external_disturbances]
