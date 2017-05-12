import matplotlib.pyplot as plt
import numpy as np
import urllib
import matplotlib.dates as mdates
#import csv
import datetime as dt




#Line Chart
"""
fig = plt.figure()
ax1 = plt.subplot2grid((1, 1), (0, 0))

x = [1, 2, 3]
y = [5, 7, 4]
x2 = [1, 2, 3]
y2 = [10, 14, 12]
plt.plot(x, y, label="First Line")
plt.plot(x2, y2, label="Second Line")
plt.plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 4])
"""

#Bar Chart
x = [6, 2, 3, 4, 5]
y = [6, 7, 8, 4, 4]
x2 = [6, 3, 5, 7, 9]
y2 = [7, 8, 4, 4, 4]
plt.bar(x, y, label = "Injuries", color = "r")
plt.bar(x2, y2, label = "Deaths", color = "k")
#pylab.xlim([1960, 2010])
plt.xticks([0.5, 2, 4, 6, 8, 10, 10.5], ['1960', '1970', '1980', '1990', '2000', '2010'])

"""Histogram
gun_Deaths = [23, 67, 87, 56, 89, 112, 32, 65, 98, 89, 90, 1, 34, 54, 54, 45, 35, 68, 80, 75, 73, 93, 123, 129, 114, 26, 94, 50]
gun_Injuries = [34, 96, 25, 2, 113, 97, 35, 28, 84, 37, 74, 12, 99, 126, 88, 98, 33, 47, 55, 50, 18, 23, 67, 76, 56, 21, 34, 94]
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]
plt.hist(gun_Deaths, bins, histtype = "bar", rwidth = 0.5, label = "Deaths", color = "k")
plt.hist(gun_Injuries, bins, histtype = "bar", rwidth = 0.5, label = "Injuries", color = "r", alpha = 0.87)
"""

"""Scatter Plot
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [9, 2, 5, 7,  8, 4, 10, 6, 9, 3]
x2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y2 = [3, 4, 8, 9,  10, 3, 5, 8, 2, 1]
plt.scatter(x, y, label = "Deaths", color = "k", marker = "x", s = 100)
plt.scatter(x2, y2, label = "Injuries", color = "r", marker = "x", s = 100)
"""

"""Stack Plot
days =  [1, 2, 3, 4, 5]
sleep = [2, 3, 4, 3, 2]
eat =   [7, 8, 6, 11, 7]
work =  [7, 8, 7, 2, 2]
play =  [8, 5, 7, 8, 13]
plt.plot([],[], color = "c", label = "Eat", linewidth = 5)
plt.plot([],[], color = "r", label = "Work", linewidth = 5)
plt.plot([],[], color = "k", label = "Play", linewidth = 5)
plt.stackplot(days, sleep, eat, work, play, colors = ["m", "c", "r", "k"])
"""

"""Pie Chart
days =        [1, 2, 3, 4, 5]
elderly =     [2, 3, 4, 3, 2]
toddlers =    [7, 8, 6, 11, 7]
youngAdults = [7, 8, 7, 2, 2]
adults =      [8, 5, 7, 8, 13]
slices =      [7, 2, 2, 13]
activities =  ["Elderly", "Toddlers", "Young Adults", "Adults"]
cols = ["m", "c", "r", "grey"]
plt.pie(slices,
        labels=activities,
        colors = cols,
        startangle = 90,
        shadow = True,
        explode = (0, 0.1, 0, 0),
        autopct = "%1.1f%%")
"""


""" Read from file. Didn't get this working. Need to import csv for it
x = []
y = []
with open("GunData.txt", "r") as csvfile:
    plots =  csv.reader(csvfile, delimiter',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x, y, label = "Loaded from file!")
"""

""" Read data from a text file with numpy
x, y = np.loadtxt("GunData.txt", delimiter=",", unpack = True)
plt.plot(x, y, label = "Loaded from file!")
"""

""" Pulls data from the web. Not finished
def graph_data(stock):

    stock_price_url = "https://chartapi.finance.yahoo.com/instrument/1.0/"+stock+"/chartdata;type=quote;range=10y/csv"
    source_code = urllib.request.urlopen(stock_price_url).read().decode()
    stock_data = []
    split_source = source_code.split("\n")
"""

plt.xlabel("Year") #Remove this for pie chart
plt.ylabel("Number of Incidents") #Remove this for pie chart
plt.title("Gun Incidents\n by Year")
plt.legend() #Remove this for pie chart
plt.show()



