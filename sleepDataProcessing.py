import csv
from datetime import datetime

file = './data/07_sleep_data'

time = []
x_accel = []
y_accel = []
z_accel = []
bed_mic = []
window_mic = []
cancelled_sound = []
with open(file + '.csv', 'r', encoding='utf-8', newline='') as csv_file:
    sleep_data_reader = csv.reader(csv_file, delimiter=',', quotechar='|')
    for row in sleep_data_reader:
        if row[4] != '100' or row[5] != '100':
            unixTime = float(row[0])
            #readableTime = (datetime.utcfromtimestamp(unixTime).strftime('%Y-%m-%d %H:%M:%S'))
            time.append(unixTime)
            x_accel.append(row[1])
            y_accel.append(row[2])
            z_accel.append(row[3])
            bed_mic.append(row[4])
            window_mic.append(row[5])
            cancelled_sound.append(int(row[4])-int(row[5]))

with open(file + '_processed.csv', 'w', encoding='utf-8', newline='') as csv_file:
        csv_write = csv.writer(csv_file, delimiter=',', quotechar='”', quoting=csv.QUOTE_MINIMAL)
        for i in range(len(time)):
            csv_write.writerow([time[i], x_accel[i], y_accel[i], z_accel[i], bed_mic[i], window_mic[i], cancelled_sound[i]])
