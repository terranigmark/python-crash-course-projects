import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/sitka_weather_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, pcrp = [], []

    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        precipitation = float(row[3])
        dates.append(current_date)
        pcrp.append(precipitation)

# plot the precipitation
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, pcrp, c = 'blue')

# format plot
ax.set_title("Daily PRCP - 2018", fontsize = 24)
ax.set_xlabel('', fontsize = 16)
fig.autofmt_xdate()
ax.set_ylabel("mm", fontsize = 16)
ax.tick_params(axis = 'both', which = 'major', labelsize = 16)

plt.show()