# Michael O'Regan 02.04.2018
# Program to analyse the Iris Data Set

# https://matplotlib.org/users/pyplot_tutorial.html
import numpy as np
import matplotlib.pyplot as plt

with open("data/irisdataset.csv") as f:
    for line in f:
        print(('{:^5}'.format(line.split(',')[0])), ('{:^5}'.format(line.split(',')[1])), ('{:^5}'.format(line.split(',')[2])), ('{:^5}'.format(line.split(',')[3])))

data = np.genfromtxt("data/irisdataset.csv", delimiter=',')

# looking at the Iris data set as a whole

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

# Looking at the Iris data set as per Iris species

col1setosa = col1[0:50]
# it took me some time to figure out how to just take the 50 from column 1, the ',' in taking column 1 from the data threw me
print(col1setosa)

mincol1setosa = np.amin(col1setosa)
maxcol1setosa = np.amax(col1setosa)
meancol1setosa = np.mean(col1setosa)
mediancol1setosa = np.median(col1setosa)

print("The minimum setosa sepal length value is", mincol1setosa)
print("The maximum setosa sepal length value is", maxcol1setosa)
print("The mean setosa sepal length value is", meancol1setosa)
print("The median setosa sepal length value is", mediancol1setosa)

plt.hist(col1setosa)
plt.show()

col1versicolor = col1[50:100]
print(col1versicolor)

mincol1versicolor = np.amin(col1versicolor)
maxcol1versicolor = np.amax(col1versicolor)
meancol1versicolor = np.mean(col1versicolor)
mediancol1versicolor = np.median(col1versicolor)

print("The minimum versicolor sepal length value is", mincol1versicolor)
print("The maximum versicolor sepal length value is", maxcol1versicolor)
print("The mean versicolor sepal length value is", meancol1versicolor)
print("The median versicolor sepal length value is", mediancol1versicolor)

plt.hist(col1versicolor)
plt.show()

col1virginica = col1[100:151]
print(col1virginica)

mincol1virginica = np.amin(col1virginica)
maxcol1virginica = np.amax(col1virginica)
meancol1virginica = np.mean(col1virginica)
mediancol1virginica = np.median(col1virginica)

print("The minimum virginica sepal length value is", mincol1virginica)
print("The maximum virginica sepal length value is", maxcol1virginica)
print("The mean virginica sepal length value is", meancol1virginica)
print("The median virginica sepal length value is", mediancol1virginica)

plt.hist(col1virginica)
plt.show()
