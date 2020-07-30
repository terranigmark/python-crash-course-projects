import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename_death_valley = 'data/death_valley_2018_simple.csv'
filename_sitka = 'data/sitka_weather_2018_simple.csv'

with open(filename_death_valley) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # get dates, high, and low temperatures from death valley file
    dv_dates, dv_highs, dv_lows = [], [], []

    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dv_dates.append(current_date)
            dv_highs.append(high)
            dv_lows.append(low)

with open(filename_sitka) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # get high and low temperatures from sitka file
    s_dates, s_highs, s_lows = [], [], []

    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        s_dates.append(current_date)
        s_highs.append(high)
        s_lows.append(low)

# plot the high and low temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dv_dates, dv_highs, c = 'red', alpha = 0.5)
ax.plot(dv_dates, dv_lows, c = 'blue', alpha = 0.5)
ax.plot(s_dates, s_highs, c = 'purple', alpha = 0.5)
ax.plot(s_dates, s_lows, c = 'olive', alpha = 0.5)
ax.fill_between(dv_dates, dv_highs, dv_lows, facecolor = 'green', alpha = 0.1)
ax.fill_between(s_dates, s_highs, s_lows, facecolor = 'plum', alpha = 0.3)

# format plot
title = "Death Valley & Sitka temperatures - 2018"
ax.set_title(title, fontsize = 24)
ax.set_xlabel('', fontsize = 16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize = 16)
ax.tick_params(axis = 'both', which = 'major', labelsize = 16)

plt.show()