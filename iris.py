# Michael O'Regan 02.04.2018
# Program to analyse the Iris Data Set

# https://matplotlib.org/users/pyplot_tutorial.html
import numpy as np
import matplotlib.pyplot as plt

with open("data/irisdataset.csv") as f:
    for line in f:
        print(('{:^5}'.format(line.split(',')[0])), ('{:^5}'.format(line.split(',')[1])), ('{:^5}'.format(line.split(',')[2])), ('{:^5}'.format(line.split(',')[3])))

data = np.genfromtxt("data/irisdataset.csv", delimiter=',')

col1 = data[:,0]
print(col1)

mincol1 = np.amin(data[:,0])
maxcol1 = np.amax(data[:,0])
meancol1 = np.mean(data[:,0])
mediancol1 = np.median(data[:,0])
print("The minimum sepal length value is", mincol1)
print("The maximum sepal length value is", maxcol1)
print("The mean sepal length value is", meancol1)
print("The median sepal length value is", mediancol1)

plt.hist(col1)
plt.show()

col2 = data[:,1]
print(col2)

mincol2 = np.amin(data[:,1])
maxcol2 = np.amax(data[:,1])
meancol2 = np.mean(data[:,1])
mediancol2 = np.median(data[:,1])
print("The minimum sepal width value is", mincol2)
print("The maximum sepal width value is", maxcol2)
print("The mean sepal width value is", meancol2)
print("The median sepal width value is", mediancol2)

plt.hist(col2)
plt.show()

col3 = data[:,2]
print(col3)

mincol3 = np.amin(data[:,2])
maxcol3 = np.amax(data[:,2])
meancol3 = np.mean(data[:,2])
mediancol3 = np.median(data[:,2])
print("The minimum petal length value is", mincol3)
print("The maximum petal length value is", maxcol3)
print("The mean petal length value is", meancol3)
print("The median petal length value is", mediancol3)

plt.hist(col3)
plt.show()

col4 = data[:,3]
print(col4)

mincol4 = np.amin(data[:,3])
maxcol4 = np.amax(data[:,3])
meancol4 = np.mean(data[:,3])
mediancol4 = np.median(data[:,3])
print("The minimum petal width value is", mincol4)
print("The maximum petal width value is", maxcol4)
print("The mean petal width value is", meancol4)
print("The median petal width value is", mediancol4)

plt.hist(col4)
plt.show()
