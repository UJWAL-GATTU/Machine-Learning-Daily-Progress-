import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# To Display random dates and visualize a graph 
np.random.seed(123456)
ts = pd.DataFrame(np.random.randn(1000),index = pd.date_range("1/1/2000",periods=1000))
ts = ts.cumsum()
ts.plot()
plt.show()

# To Display random dates and visualize a graph with multiple columns
df = pd.DataFrame(np.random.rand(1000,4),index = ts.index,columns=list('ABCD'))
df = df.cumsum()
df.plot()
plt.show()

# To visualize a bar graph for a particular row
df.iloc[5].plot(kind='bar')
plt.show()

# To visualize a bar graph for random values
df2 = pd.DataFrame(np.random.rand(10,4),columns=["A","B","C","D"])
df2.plot(kind='bar')
plt.show()

# To visualize a stacked bar graph for random values
df2.plot.bar(stacked=True)
plt.show()

# To visualize a stacked graph in horizontal  way
df2.plot.barh(stacked=True)
plt.show()

# To Visualize a histogram  
df3 = pd.DataFrame(
    {
        "a" : np.random.randn(1000) + 1,
        "b" : np.random.randn(1000),
        "c" : np.random.randn(1000) - 1
    },
    columns = ["a","b","c"],
)
df3.plot.hist(alpha=0.5)
plt.show()
df3.plot.hist(stacked=True, alpha=0.5)

# Change in orientation of histogram graph
df3["a"].plot.hist(orientation="horizontal", cumulative=True)
plt.show()

# To visualize the difference between the rows in histogram
df3.diff().hist(color="k", alpha=0.5, bins=50)
plt.show()

# To visualize a box plot
df4 = pd.DataFrame(np.random.rand(10, 5), columns=["A", "B", "C", "D", "E"])
df4.plot.box()
plt.show()

# Boxplot can be colorized by passing color keyword. You can pass a dict whose keys are boxes, whiskers, medians and caps. 
# If some keys are missing in the dict, default colors are used for the corresponding artists. Also, boxplot has sym keyword to specify fliers style.

color = {
    "boxes": "DarkGreen",
    "whiskers": "DarkOrange",
    "medians": "DarkBlue",
    "caps": "Gray",
}


df4.plot.box(color=color, sym="r+")
plt.show()

# To visualize a horizontal box plot and change the positions of the boxes
df4.plot.box(vert=False, positions=[1, 4, 5, 6, 8])
plt.show()

# To visualize an area plot
df = pd.DataFrame(np.random.rand(10, 4), columns=["a", "b", "c", "d"])
df.plot.area()
plt.show()

# To visualize an unstacked area plot
df.plot.area(stacked=False)
plt.show()

# To visualize a scatter plot
df4.plot.scatter(x="A", y="B")
plt.show()

# To visualize a scatter plot with color and size arguments
df4.plot.scatter(x="A", y="B", c="C", s=50)
plt.show()

# To visualize a hexagonal binning plot
df = pd.DataFrame(np.random.randn(1000, 2), columns=["a", "b"])
df.plot.hexbin(x="a", y="b", gridsize=25)
plt.show()

# To visualize a pie chart
series = pd.Series(3 * np.random.rand(4), index=["a", "b", "c", "d"], name="series")
series.plot.pie(figsize=(6, 6))
plt.show()

# To visualize a scatter matrix
from pandas.plotting import scatter_matrix
df = pd.DataFrame(np.random.randn(1000, 4), columns=["a", "b", "c", "d"])
scatter_matrix(df, alpha=0.2, figsize=(6, 6), diagonal="kde")
plt.show()

# To visualize a density plot
ser = pd.Series(np.random.randn(1000))
ser.plot.kde()
plt.show()

# To visualize andrews curves
from pandas.plotting import andrews_curves
data = pd.read_csv("C:\\Users\\Gattu Ujwal\\Downloads\\iris.csv")
plt.figure()
andrews_curves(data, "Name")
plt.show()


