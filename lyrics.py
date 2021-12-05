import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

file1 = open("MyWords.txt", "r")
words = file1.read()
list1= words.split()
# print Counter(list1).keys()
# print Counter(list1).values()

x_labels=np.array(Counter(list1).keys())
y_axis = np.array(Counter(list1).values())

w=10
nitems = len(y_axis)
x_axis = np.arange(0, nitems*w, w)

fig, ax = plt.subplots(1)
ax.bar(x_axis, y_axis, width = w, align = 'center' )
ax.set_xticks(x_axis)
ax.set_xticklabels(x_labels, rotation = 90)
plt.tick_params(axis='x', which='major', labelsize=10)
plt.show()

file1.close()
