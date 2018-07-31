# Programming and Scripting 2018 Project
## Iris Data Set Analysis

https://en.wikipedia.org/wiki/Iris_flower_data_set

Background:
Ronald Fisher was a British Statistician and biologist.  In 1936 he wrote a paper called The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis.
Fishers Iris Data Set is a set of Data containing 150 pieces of data.  
The data is taken from 3 species of Iris flower.  4 different measurements were taken, the length and the width of the Sepal and the length and the width of the petal.

Through the Python programming language I will try to analyse this data calculating the following:
- The Minimum values of each data measurement set as a whole and as per each species of Iris flower.
- The Maximum values of each data measurement set as a whole and as per each species of Iris flower.
- The Mean values of each data measurement set as a whole and as per each species of Iris flower.

## Sepal Length

![](1%20Col1%20Sepal%20Length.png)

### Whole Dataset

The minimum sepal length value is 4.3
The maximum sepal length value is 7.9
The mean sepal length value is 5.84333333333
The median sepal length value is 5.8
The standard deviation sepal length value is 0.825301291785

### By Flower

![](5%20Col1Setosa%20Sepal%20Length.png)

The minimum setosa sepal length value is 4.3
The maximum setosa sepal length value is 5.8
The mean setosa sepal length value is 5.006
The median setosa sepal length value is 5.0
The standard deviation setosa sepal length value is 0.348946987378

![](6%20Col1%20Versicolor%20Sepal%20Length.png)

The minimum versicolor sepal length value is 4.9
The maximum versicolor sepal length value is 7.0
The mean versicolor sepal length value is 5.936
The median versicolor sepal length value is 5.9
The standard deviation versicolor sepal length value is 0.510983365678

![](7%20Col1%20Verginica%20Sepal%20Length.png)

The minimum virginica sepal length value is 4.9
The maximum virginica sepal length value is 7.9
The mean virginica sepal length value is 6.588
The median virginica sepal length value is 6.5
The standard deviation virginica sepal length value is 0.629488681391

As can be seen by the above values the Sepal Length values are close to the mean especially shown by the standard deviation of the Setosa Iris Flower.

## Sepal Width

![](2%20Col2%20Sepal%20Width.png)

### Whole Dataset

The minimum sepal width value is 2.0
The maximum sepal width value is 4.4
The mean sepal width value is 3.054
The median sepal width value is 3.0
The standard deviation sepal width value is 0.432146580071

### By Flower

![](8%20Col2%20Setosa%20Sepal%20Width.png)

The minimum setosa sepal width value is 2.3
The maximum setosa sepal width value is 4.4
The mean setosa sepal width value is 3.418
The median setosa sepal width value is 3.4
The standard deviation setosa sepal width value is 0.377194909828

![](9%20Col2%20Versicolor%20Sepal%20Width.png)

The minimum versicolor sepal width value is 2.0
The maximum versicolor sepal width value is 3.4
The mean versicolor sepal width value is 2.77
The median versicolor sepal width value is 2.8
The standard deviation versicolor sepal width value is 0.31064449134

![](10%20Col2%20Verginica%20Sepal%20Width.png)

The minimum virginica sepal width value is 2.2
The maximum virginica sepal width value is 3.8
The mean virginica sepal width value is 2.974
The median virginica sepal width value is 3.0
The standard deviation virginica sepal width value is 0.319255383666

The Sepal Width values are even more closely grouped around the mean.  The standard deviation values for Sepal Width are all under .5.

## Petal Length

![](3%20Col3%20Petal%20Length.png)

### Whole Dataset

The minimum petal length value is 1.0
The maximum petal length value is 6.9
The mean petal length value is 3.75866666667
The median petal length value is 4.35
The standard deviation petal length value is 1.75852918341

### By Flower

![](11%20Col3%20Setosa%20Petal%20Length.png)

The minimum setosa petal length value is 1.0
The maximum setosa petal length value is 1.9
The mean setosa petal length value is 1.464
The median setosa petal length value is 1.5
The standard deviation setosa petal length value is 0.171767284429

![](12%20Col3%20Versicolor%20Petal%20Length.png)

The minimum versicolor petal length value is 3.0
The maximum versicolor petal length value is 5.1
The mean versicolor petal length value is 4.26
The median versicolor petal length value is 4.35
The standard deviation versicolor petal length value is 0.465188133985

![](13%20Col3%20Virginica%20Petal%20Length.png)

The minimum virginica petal length value is 4.5
The maximum virginica petal length value is 6.9
The mean virginica petal length value is 5.552
The median virginica petal length value is 5.55
The standard deviation virginica petal length value is 0.546347874527

Petal Length is where we see the highest standard deviation meaning that this is where there is the greatest dispersal, spread betweeen the measurements.  The measurement are very different per flower also.  The flowers are like the steps of a stairs on this measurement with very little overlap.  The Setosa is by far the smallest ranging between 1 and 1.9, the versicolor jumps then to between 3 and 5.1.  The verginica is by far the largest with a slight overlap with the versicolor.  Verginica ranging between 4.5 and 6.9.

However looking at each flower individually we can see that this is also where the standard deviation is showing the us the measurement are very clusterd around the mean.

## Petal Width

![](4%20Col4%20Petal%20Width.png)

### Whole Dataset

The minimum petal width value is 0.1
The maximum petal width value is 2.5
The mean petal width value is 1.19866666667
The median petal width value is 1.3
The standard deviation petal width value is 0.760612618588

### By Flower

![](14%20Col4%20Setosa%20Petal%20Width.png)

The minimum setosa petal width value is 0.1
The maximum setosa petal width value is 0.6
The mean setosa petal width value is 0.244
The median setosa petal width value is 0.2
The standard deviation setosa petal width value is 0.106131993291

![](15%20Col4%20Versicolor%20Petal%20Width.png)

The minimum versicolor petal width value is 1.0
The maximum versicolor petal width value is 1.8
The mean versicolor petal width value is 1.326
The median versicolor petal width value is 1.3
The standard deviation versicolor petal width value is 0.195765165441

The minimum virginica petal width value is 1.4
The maximum virginica petal width value is 2.5
The mean virginica petal width value is 2.026
The median virginica petal width value is 2.0
The standard deviation virginica petal width value is 0.271889683512

Petal Width is again showing us a higher standard deviation.  The measurement are very different per flower also.  The flowers are again like the steps of a stairs on this measurement with very little overlap.  The Setosa is by far the smallest ranging between .1 and .6, the versicolor jumps then to between 1 and 1.8.  The verginica is by far the largest with a slight overlap with the versicolor.  Verginica ranging between 1.4 and 2.5.

However looking at each flower individually we can see that this is also where the standard deviation is showing the us the measurement are very clusterd around the mean.
