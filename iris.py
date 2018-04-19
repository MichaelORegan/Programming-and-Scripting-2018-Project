# Michael O'Regan 02.04.2018
# Program to analyse the Iris Data Set

# https://matplotlib.org/users/pyplot_tutorial.html
import numpy as np
import matplotlib.pyplot as plt
# calling data and printing it in columns with spacing
with open("data/irisdataset.csv") as f:
    for line in f:
        print(('{:^5}'.format(line.split(',')[0])), ('{:^5}'.format(line.split(',')[1])), ('{:^5}'.format(line.split(',')[2])), ('{:^5}'.format(line.split(',')[3])))
        
data = np.genfromtxt("data/irisdataset.csv", delimiter=',')
# calling data for analysis
col1 = data[:,0] # calling the first column of data col1
print(col1) # printing col1 to show the data

mincol1 = np.amin(data[:,0]) # minimum value of col1 calling it mincol1
maxcol1 = np.amax(data[:,0]) # maximum value of col1 calling it maxcol1
meancol1 = np.mean(data[:,0]) # mean of col1 calling it meancol1
mediancol1 = np.median(data[:,0]) # median of col1 calling it mediancol1
print("The minimum sepal length value is", mincol1)
print("The maximum sepal length value is", maxcol1)
print("The mean sepal length value is", meancol1)
print("The median sepal length value is", mediancol1)

col2 = data[:,1] # calling the second column of data col2
print(col2) # printing col2 to show the data

mincol2 = np.amin(data[:,1]) # minimum value of col2 calling it mincol2
maxcol2 = np.amax(data[:,1]) # maximum value of col2 calling it maxcol2
meancol2 = np.mean(data[:,1]) # mean of col2 calling it meancol2
mediancol2 = np.median(data[:,1]) # median of col2 calling it mediancol2
print("The minimum sepal width value is", mincol2)
print("The maximum sepal width value is", maxcol2)
print("The mean sepal width value is", meancol2)
print("The median sepal width value is", mediancol2)

col3 = data[:,2] # calling the third column of data col3
print(col3) # printing col3 to show the data

mincol3 = np.amin(data[:,2]) # minimum value of col3 calling it mincol3
maxcol3 = np.amax(data[:,2]) # maximum value of col3 calling it maxcol3
meancol3 = np.mean(data[:,2]) # mean of col3 calling it meancol3
mediancol3 = np.median(data[:,2]) # median of col3 calling it mediancol3
print("The minimum petal length value is", mincol3)
print("The maximum petal length value is", maxcol3)
print("The mean petal length value is", meancol3)
print("The median petal length value is", mediancol3)

col4 = data[:,3] # calling the fourth column of data col4
print(col4) # printing col4 to show the data

mincol4 = np.amin(data[:,3]) # minimum value of col4 calling it mincol4
maxcol4 = np.amax(data[:,3]) # maximum value of col4 calling it maxcol4
meancol4 = np.mean(data[:,3]) # mean of col4 calling it meancol4
mediancol4 = np.median(data[:,3])  # median of col4 calling it mediancol4
print("The minimum petal width value is", mincol4)
print("The maximum petal width value is", maxcol4)
print("The mean petal width value is", meancol4)
print("The median petal width value is", mediancol4)
