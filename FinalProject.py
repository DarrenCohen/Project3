import numpy as np
import matplotlib.pyplot as plt

N = 3
ind = np.arange(N)  # the x locations for the groups
width = 0.15       # the width of the bars

fig = plt.figure()
ax = fig.add_subplot(111)

yvals = [4, 9, 2]
rects1 = ax.bar(ind, yvals, width, color='r')
zvals = [1,2,3]
rects2 = ax.bar(ind+width, zvals, width, color='g')
kvals = [11,12,13]
rects3 = ax.bar(ind+width*2, kvals, width, color='b')
xvals = [13,14,4]
rects4 = ax.bar(ind+width*2, xvals, width, color='b')
dvals = [4,8,14]
rects5 = ax.bar(ind+width*2, dvals, width, color='b')

ax.set_ylabel('Scores')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('1970-Jan-4', '1980-Jan-5', '1990-Jan-6', '2000-Jan-6', '2010-Jan-6') )
ax.legend( (rects1[0], rects2[0], rects3[0], rects4[0], rects5[0]), ('Injuries', 'Deaths', 'Toddler Incidents') )

def autolabel(rects):
    for rect in rects:
        h = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*h, '%d'%int(h),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

plt.show()