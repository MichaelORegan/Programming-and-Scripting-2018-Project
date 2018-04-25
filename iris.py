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

# column 1 sepal length
col1 = data[:,0]
print(col1)

mincol1 = np.amin(data[:,0])
maxcol1 = np.amax(data[:,0])
meancol1 = np.mean(data[:,0])
mediancol1 = np.median(data[:,0])
stddevcol1 = np.std(data[:,0])

print("The minimum sepal length value is", mincol1)
print("The maximum sepal length value is", maxcol1)
print("The mean sepal length value is", meancol1)
print("The median sepal length value is", mediancol1)
print("The standard deviation sepal length value is", stddevcol1)

plt.hist(col1)
plt.show()

# column 2 sepal width

col2 = data[:,1]
print(col2)

mincol2 = np.amin(data[:,1])
maxcol2 = np.amax(data[:,1])
meancol2 = np.mean(data[:,1])
mediancol2 = np.median(data[:,1])
stddevcol2 = np.std(data[:,1])

print("The minimum sepal width value is", mincol2)
print("The maximum sepal width value is", maxcol2)
print("The mean sepal width value is", meancol2)
print("The median sepal width value is", mediancol2)
print("The standard deviation sepal width value is", stddevcol2)

plt.hist(col2)
plt.show()

# column 3 petal length

col3 = data[:,2]
print(col3)

mincol3 = np.amin(data[:,2])
maxcol3 = np.amax(data[:,2])
meancol3 = np.mean(data[:,2])
mediancol3 = np.median(data[:,2])
stddevcol3 = np.std(data[:,2])

print("The minimum petal length value is", mincol3)
print("The maximum petal length value is", maxcol3)
print("The mean petal length value is", meancol3)
print("The median petal length value is", mediancol3)
print("The standard deviation petal length value is", stddevcol3)

plt.hist(col3)
plt.show()

# column 4 petal width

col4 = data[:,3]
print(col4)

mincol4 = np.amin(data[:,3])
maxcol4 = np.amax(data[:,3])
meancol4 = np.mean(data[:,3])
mediancol4 = np.median(data[:,3])
stddevcol4 = np.std(data[:,3])

print("The minimum petal width value is", mincol4)
print("The maximum petal width value is", maxcol4)
print("The mean petal width value is", meancol4)
print("The median petal width value is", mediancol4)
print("The standard deviation petal width value is", stddevcol4)

plt.hist(col4)
plt.show()

# Looking at the Iris data set as per Iris species
# column 1 sepal length

col1setosa = col1[0:50]
# it took me some time to figure out how to just take the 50 from column 1, the ',' in taking column 1 from the data threw me
print(col1setosa)

mincol1setosa = np.amin(col1setosa)
maxcol1setosa = np.amax(col1setosa)
meancol1setosa = np.mean(col1setosa)
mediancol1setosa = np.median(col1setosa)
stddevcol1setosa = np.std(col1setosa)

print("The minimum setosa sepal length value is", mincol1setosa)
print("The maximum setosa sepal length value is", maxcol1setosa)
print("The mean setosa sepal length value is", meancol1setosa)
print("The median setosa sepal length value is", mediancol1setosa)
print("The standard deviation setosa sepal length value is", stddevcol1setosa)

plt.hist(col1setosa)
plt.show()

col1versicolor = col1[50:100]
print(col1versicolor)

mincol1versicolor = np.amin(col1versicolor)
maxcol1versicolor = np.amax(col1versicolor)
meancol1versicolor = np.mean(col1versicolor)
mediancol1versicolor = np.median(col1versicolor)
stddevcol1versicolor = np.std(col1versicolor)

print("The minimum versicolor sepal length value is", mincol1versicolor)
print("The maximum versicolor sepal length value is", maxcol1versicolor)
print("The mean versicolor sepal length value is", meancol1versicolor)
print("The median versicolor sepal length value is", mediancol1versicolor)
print("The standard deviation versicolor sepal length value is", stddevcol1versicolor)

plt.hist(col1versicolor)
plt.show()

col1virginica = col1[100:151]
print(col1virginica)

mincol1virginica = np.amin(col1virginica)
maxcol1virginica = np.amax(col1virginica)
meancol1virginica = np.mean(col1virginica)
mediancol1virginica = np.median(col1virginica)
stddevcol1virginica = np.std(col1virginica)

print("The minimum virginica sepal length value is", mincol1virginica)
print("The maximum virginica sepal length value is", maxcol1virginica)
print("The mean virginica sepal length value is", meancol1virginica)
print("The median virginica sepal length value is", mediancol1virginica)
print("The standard deviation virginica sepal length value is", stddevcol1virginica)

plt.hist(col1virginica)
plt.show()

# column 2 sepal width

col2setosa = col2[0:50]
print(col2setosa)

mincol2setosa = np.amin(col2setosa)
maxcol2setosa = np.amax(col2setosa)
meancol2setosa = np.mean(col2setosa)
mediancol2setosa = np.median(col2setosa)
stddevcol2setosa = np.std(col2setosa)

print("The minimum setosa sepal width value is", mincol2setosa)
print("The maximum setosa sepal width value is", maxcol2setosa)
print("The mean setosa sepal width value is", meancol2setosa)
print("The median setosa sepal width value is", mediancol2setosa)
print("The standard deviation setosa sepal width value is", stddevcol2setosa)

plt.hist(col2setosa)
plt.show()

col2versicolor = col2[50:100]
print(col2versicolor)

mincol2versicolor = np.amin(col2versicolor)
maxcol2versicolor = np.amax(col2versicolor)
meancol2versicolor = np.mean(col2versicolor)
mediancol2versicolor = np.median(col2versicolor)
stddevcol2versicolor = np.std(col2versicolor)

print("The minimum versicolor sepal width value is", mincol2versicolor)
print("The maximum versicolor sepal width value is", maxcol2versicolor)
print("The mean versicolor sepal width value is", meancol2versicolor)
print("The median versicolor sepal width value is", mediancol2versicolor)
print("The standard deviation versicolor sepal width value is", stddevcol2versicolor)

plt.hist(col2versicolor)
plt.show()

col2virginica = col2[100:151]
print(col2virginica)

mincol2virginica = np.amin(col2virginica)
maxcol2virginica = np.amax(col2virginica)
meancol2virginica = np.mean(col2virginica)
mediancol2virginica = np.median(col2virginica)
stddevcol2virginica = np.std(col2virginica)

print("The minimum virginica sepal width value is", mincol2virginica)
print("The maximum virginica sepal width value is", maxcol2virginica)
print("The mean virginica sepal width value is", meancol2virginica)
print("The median virginica sepal width value is", mediancol2virginica)
print("The standard deviation virginica sepal width value is", stddevcol2virginica)

plt.hist(col2virginica)
plt.show()

# column 3 petal length

col3setosa = col3[0:50]
print(col3setosa)

mincol3setosa = np.amin(col3setosa)
maxcol3setosa = np.amax(col3setosa)
meancol3setosa = np.mean(col3setosa)
mediancol3setosa = np.median(col3setosa)
stddevcol3setosa = np.std(col3setosa)

print("The minimum setosa petal length value is", mincol3setosa)
print("The maximum setosa petal length value is", maxcol3setosa)
print("The mean setosa petal length value is", meancol3setosa)
print("The median setosa petal length value is", mediancol3setosa)
print("The standard deviation setosa petal length value is", stddevcol3setosa)

plt.hist(col3setosa)
plt.show()

col3versicolor = col3[50:100]
print(col3versicolor)

mincol3versicolor = np.amin(col3versicolor)
maxcol3versicolor = np.amax(col3versicolor)
meancol3versicolor = np.mean(col3versicolor)
mediancol3versicolor = np.median(col3versicolor)
stddevcol3versicolor = np.std(col3versicolor)

print("The minimum versicolor petal length value is", mincol3versicolor)
print("The maximum versicolor petal length value is", maxcol3versicolor)
print("The mean versicolor petal length value is", meancol3versicolor)
print("The median versicolor petal length value is", mediancol3versicolor)
print("The standard deviation versicolor petal length value is", stddevcol3versicolor)

plt.hist(col3versicolor)
plt.show()

col3virginica = col3[100:151]
print(col3virginica)

mincol3virginica = np.amin(col3virginica)
maxcol3virginica = np.amax(col3virginica)
meancol3virginica = np.mean(col3virginica)
mediancol3virginica = np.median(col3virginica)
stddevcol3virginica = np.std(col3virginica)

print("The minimum virginica petal length value is", mincol3virginica)
print("The maximum virginica petal length value is", maxcol3virginica)
print("The mean virginica petal length value is", meancol3virginica)
print("The median virginica petal length value is", mediancol3virginica)
print("The standard deviation virginica petal length value is", stddevcol3virginica)

plt.hist(col3virginica)
plt.show()

# column 4 petal width

col4setosa = col4[0:50]
print(col4setosa)

mincol4setosa = np.amin(col4setosa)
maxcol4setosa = np.amax(col4setosa)
meancol4setosa = np.mean(col4setosa)
mediancol4setosa = np.median(col4setosa)
stddevcol4setosa = np.std(col4setosa)

print("The minimum setosa petal width value is", mincol4setosa)
print("The maximum setosa petal width value is", maxcol4setosa)
print("The mean setosa petal width value is", meancol4setosa)
print("The median setosa petal width value is", mediancol4setosa)
print("The standard deviation setosa petal width value is", stddevcol4setosa)

plt.hist(col4setosa)
plt.show()

col4versicolor = col4[50:100]
print(col4versicolor)

mincol4versicolor = np.amin(col4versicolor)
maxcol4versicolor = np.amax(col4versicolor)
meancol4versicolor = np.mean(col4versicolor)
mediancol4versicolor = np.median(col4versicolor)
stddevcol4versicolor = np.std(col4versicolor)

print("The minimum versicolor petal width value is", mincol4versicolor)
print("The maximum versicolor petal width value is", maxcol4versicolor)
print("The mean versicolor petal width value is", meancol4versicolor)
print("The median versicolor petal width value is", mediancol4versicolor)
print("The standard deviation versicolor petal width value is", stddevcol4versicolor)

plt.hist(col4versicolor)
plt.show()

col4virginica = col4[100:151]
print(col4virginica)

mincol4virginica = np.amin(col4virginica)
maxcol4virginica = np.amax(col4virginica)
meancol4virginica = np.mean(col4virginica)
mediancol4virginica = np.median(col4virginica)
stddevcol4virginica = np.std(col4virginica)

print("The minimum virginica petal width value is", mincol4virginica)
print("The maximum virginica petal width value is", maxcol4virginica)
print("The mean virginica petal width value is", meancol4virginica)
print("The median virginica petal width value is", mediancol4virginica)
print("The standard deviation virginica petal width value is", stddevcol4virginica)

plt.hist(col4virginica)
plt.show()
