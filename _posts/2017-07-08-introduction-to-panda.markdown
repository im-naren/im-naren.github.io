---
layout: single
title:  "Introduction To Pandas"
date:   2017-07-08 16:10:44 +0530
categories: machine-learning
tags:
    - python
    - machine-learning
    - data-science
    - coding
    - data-structure
header:
    teaser: /assets/site-images/thumb-python.jpg
---

**Pandas** is one of the widely used Python libraries for working with data. it is built on libraries like Matplotlib and NumPy. Pandas is great for data manipulation, data analysis, and data visualization.

In this tutorial we will see how pandas makes life really easy for a data analysis. Pandas can read and write data from and to CSV files or even databases easily.

#### Data Structures in Pandas

**Series**

A series is a one-dimensional object, like an array, list or could be understood as a column in table. similar to the array or list index each element in a series is assigned with a labeled index. By default, each item is given an numerical index label from 0 to N, where N is the length of the Series minus one.

*How to create Series*
The basic method to create a Series is to call `.Series()`


```python
# import pandas
import pandas as pd

# create a Series with an arbitrary list
X1 = pd.Series([7, 'develbyte', 3.14, 'Happy Learnning'])
X1
```




    0                  7
    1          develbyte
    2               3.14
    3    Happy Learnning
    dtype: object



*Note:-* when the Series contains elements of multiple different datatypes the dtype of the series will be the higher datatype

`int32 > int64 > flot64 >.....>object`  


```python
X2 = pd.Series([7, 5, 4, 3])
print(X2)

X3 = pd.Series([7, 5, 4., 3.])
print(X3)
```

    0    7
    1    5
    2    4
    3    3
    dtype: int64
    0    7.0
    1    5.0
    2    4.0
    3    3.0
    dtype: float64


*creating a series with index*
index of the series elements can also be changes by simply passing a list of indexes,
the list of elements and the list of indexes should be of same length or you will end up with error


```python
X1 = pd.Series([7, 'develbyte', 3.14, 'Happy Learnning'],
              index=['A', 'B', 'C', 'D'])

print(X1)
```

    A                  7
    B          develbyte
    C               3.14
    D    Happy Learnning
    dtype: object


**DataFrame**

DataFrame is a two-dimensional labeled data structures with columns of same or different data types. Similar to tables in a database the DataFrame can hold multiple columns with multiple data types. You can also think of a DataFrame as a group of Series objects that share an index.

*How to import Data in Dataframe*


```python
# Importing the dataset
dataset = pd.read_csv('../data/data.csv')
dataset
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Country</th>
      <th>Age</th>
      <th>Salary</th>
      <th>Purchased</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>France</td>
      <td>44.0</td>
      <td>72000.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Spain</td>
      <td>27.0</td>
      <td>48000.0</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Germany</td>
      <td>30.0</td>
      <td>54000.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Spain</td>
      <td>38.0</td>
      <td>61000.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Germany</td>
      <td>40.0</td>
      <td>NaN</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>5</th>
      <td>France</td>
      <td>35.0</td>
      <td>58000.0</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Spain</td>
      <td>NaN</td>
      <td>52000.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>7</th>
      <td>France</td>
      <td>48.0</td>
      <td>79000.0</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Germany</td>
      <td>50.0</td>
      <td>83000.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>9</th>
      <td>France</td>
      <td>37.0</td>
      <td>67000.0</td>
      <td>Yes</td>
    </tr>
  </tbody>
</table>
</div>



**How to inspect Data in Dataframe**

* Very first information what we would like to know in a dataframe are
        - number of columns
        - number of records
        - attribute names
        - datatype of each attribute    
we can get all these information by calling just one function `info()` it will give Concise summary of a DataFrame


```python
dataset.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 10 entries, 0 to 9
    Data columns (total 4 columns):
    Country      10 non-null object
    Age          9 non-null float64
    Salary       9 non-null float64
    Purchased    10 non-null object
    dtypes: float64(2), object(2)
    memory usage: 392.0+ bytes


we can also use `dtypes` to get the datatypes of each attribute


```python
dataset.dtypes
```




    Country       object
    Age          float64
    Salary       float64
    Purchased     object
    dtype: object



for just geting the column names in a dataframe use `dataset.columns`


```python
# columns.values gives the column names in the DataFrame
dataset.columns.values
```




    array(['Country', 'Age', 'Salary', 'Purchased'], dtype=object)



similarly for index values


```python
# index.values gives the list of row indices
dataset.index.values
```




    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])



* Probably the most useful function for inspecting a data set in a DataFrame is `describe()` it will return basic statistics about the dataset's numeric columns


```python
dataset.describe()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Salary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>9.000000</td>
      <td>9.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>38.777778</td>
      <td>63777.777778</td>
    </tr>
    <tr>
      <th>std</th>
      <td>7.693793</td>
      <td>12265.579662</td>
    </tr>
    <tr>
      <th>min</th>
      <td>27.000000</td>
      <td>48000.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>35.000000</td>
      <td>54000.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>38.000000</td>
      <td>61000.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>44.000000</td>
      <td>72000.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>50.000000</td>
      <td>83000.000000</td>
    </tr>
  </tbody>
</table>
</div>



*  For take a look at the actual data `head()` and `tail()` are the most useful function
        - head method shows first n rows from the DataFrame, default value of n is 5
        - tail method shows last n rows from the DataFrame, default value of n is 5


```python
dataset.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Country</th>
      <th>Age</th>
      <th>Salary</th>
      <th>Purchased</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>France</td>
      <td>44.0</td>
      <td>72000.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Spain</td>
      <td>27.0</td>
      <td>48000.0</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Germany</td>
      <td>30.0</td>
      <td>54000.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Spain</td>
      <td>38.0</td>
      <td>61000.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Germany</td>
      <td>40.0</td>
      <td>NaN</td>
      <td>Yes</td>
    </tr>
  </tbody>
</table>
</div>




```python
dataset.tail()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Country</th>
      <th>Age</th>
      <th>Salary</th>
      <th>Purchased</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>5</th>
      <td>France</td>
      <td>35.0</td>
      <td>58000.0</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Spain</td>
      <td>NaN</td>
      <td>52000.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>7</th>
      <td>France</td>
      <td>48.0</td>
      <td>79000.0</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Germany</td>
      <td>50.0</td>
      <td>83000.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>9</th>
      <td>France</td>
      <td>37.0</td>
      <td>67000.0</td>
      <td>Yes</td>
    </tr>
  </tbody>
</table>
</div>



#### Select and Index in DataFrames
There are three main options in pandas, which allows us to access the data in DataFrame, these are based on index and location of the rows and column, these options could be confusing for beginners but its quit simple once understood.

The selection methods are:

- Selecting data by row numbers called integer-location based indexing/selection (`.iloc`)

    `dataset.iloc[<row selection>, <column selection>]`


- Selecting data by label or by a conditional statement (`.loc`)

    `dataset.loc[<row selection>, <column selection>]`


- Selecting in a hybrid approach(`.ix`)

    `dataset.ix[<row selection>, <column selection>]`


*Single selections using iloc and DataFrame*

*Rows:*


```python
R1 = dataset.iloc[0] # first row of data frame - Note a Series data type output.
R2 = dataset.iloc[1] # second row of data frame
R3 = dataset.iloc[-1] # last row of data frame
print ("---------------------------------------")
print (R1)
print ("---------------------------------------")
print (R2)
print ("---------------------------------------")
print (R3)
```

    ---------------------------------------
    Country      France
    Age              44
    Salary        72000
    Purchased        No
    Name: 0, dtype: object
    ---------------------------------------
    Country      Spain
    Age             27
    Salary       48000
    Purchased      Yes
    Name: 1, dtype: object
    ---------------------------------------
    Country      France
    Age              37
    Salary        67000
    Purchased       Yes
    Name: 9, dtype: object


*Columns:*


```python
C1 = dataset.iloc[:,0] # first column of data frame (first_name)
C2 = dataset.iloc[:,1] # second column of data frame (last_name)
C3 = dataset.iloc[:,-1] # last column of data frame (id)
print ("---------------------------------------")
print (C1)
print ("---------------------------------------")
print (C2)
print ("---------------------------------------")
print (C3)
```

    ---------------------------------------
    0     France
    1      Spain
    2    Germany
    3      Spain
    4    Germany
    5     France
    6      Spain
    7     France
    8    Germany
    9     France
    Name: Country, dtype: object
    ---------------------------------------
    0    44.0
    1    27.0
    2    30.0
    3    38.0
    4    40.0
    5    35.0
    6     NaN
    7    48.0
    8    50.0
    9    37.0
    Name: Age, dtype: float64
    ---------------------------------------
    0     No
    1    Yes
    2     No
    3     No
    4    Yes
    5    Yes
    6     No
    7    Yes
    8     No
    9    Yes
    Name: Purchased, dtype: object


Multiple row and column selections using `iloc` and `DataFrame`


```python
MR1 = dataset.iloc[0:5] # first five rows of dataframe
MR2 = dataset.iloc[:, 0:2] # first two columns of data frame with all rows
MR3 = dataset.iloc[[0, 3, 6, 9], [0, 3]] # 1st, 4th, 7th, 9th row + 1st 3th 4th columns.
MR4 = dataset.iloc[0:5, 1:3] # first 5 rows and 4th, 5th columns of data frame.

print ("---------------------------------------")
print (MR1)
print ("---------------------------------------")
print (MR2)
print ("---------------------------------------")
print (MR3)
print ("---------------------------------------")
print (MR4)
```

    ---------------------------------------
       Country   Age   Salary Purchased
    0   France  44.0  72000.0        No
    1    Spain  27.0  48000.0       Yes
    2  Germany  30.0  54000.0        No
    3    Spain  38.0  61000.0        No
    4  Germany  40.0      NaN       Yes
    ---------------------------------------
       Country   Age
    0   France  44.0
    1    Spain  27.0
    2  Germany  30.0
    3    Spain  38.0
    4  Germany  40.0
    5   France  35.0
    6    Spain   NaN
    7   France  48.0
    8  Germany  50.0
    9   France  37.0
    ---------------------------------------
      Country Purchased
    0  France        No
    3   Spain        No
    6   Spain        No
    9  France       Yes
    ---------------------------------------
        Age   Salary
    0  44.0  72000.0
    1  27.0  48000.0
    2  30.0  54000.0
    3  38.0  61000.0
    4  40.0      NaN


`.iloc` returns a Pandas Series when one only row or Column is selected



```python
print(".iloc returns a Pandas Series when one only row or Column is selected")
print(type(dataset.iloc[0]))
print(type(dataset.iloc[:,1]))
```

    .iloc returns a Pandas Series when one only row or Column is selected
    <class 'pandas.core.series.Series'>
    <class 'pandas.core.series.Series'>


`.iloc` returns a Pandas DataFrame when multiple rows or Columns are selected


```python
print("\n .iloc returns a Pandas DataFrame when multiple rows or Columns are selected")
print(type(dataset.iloc[0:2]))
print(type(dataset.iloc[:,1:3]))
print(type(dataset.iloc[1:2, 3:6]))
```


     .iloc returns a Pandas DataFrame when multiple rows or Columns are selected
    <class 'pandas.core.frame.DataFrame'>
    <class 'pandas.core.frame.DataFrame'>
    <class 'pandas.core.frame.DataFrame'>


`.iloc` returns a Pandas Series when multiple rows are selected with only one column


```python
print("\n .iloc returns a Pandas Series when multiple rows are selected with only one column")
print(type(dataset.iloc[1:2, 3]))
```


     .iloc returns a Pandas Series when multiple rows are selected with only one column
    <class 'pandas.core.series.Series'>


above output could easily converted to Pandas `DataFrame` by passing a single-valued list as column index


```python
print("\n Above output could easly converted to Pandas DataFrame by passing a single-valued list as column index")
print(type(dataset.iloc[1:2, [3]]))
```


     Above output could easily converted to Pandas DataFrame by passing a single-valued list as column index
    <class 'pandas.core.frame.DataFrame'>


**some more fun with `iloc`**


```python
X = dataset.iloc[:, :-1]
Y = dataset.iloc[:, 3]

print ("---------------------------------------")
print(type(X))
print(X)
print ("---------------------------------------")
print(type(Y))
print(Y)
```

    ---------------------------------------
    <class 'pandas.core.frame.DataFrame'>
       Country   Age   Salary
    0   France  44.0  72000.0
    1    Spain  27.0  48000.0
    2  Germany  30.0  54000.0
    3    Spain  38.0  61000.0
    4  Germany  40.0      NaN
    5   France  35.0  58000.0
    6    Spain   NaN  52000.0
    7   France  48.0  79000.0
    8  Germany  50.0  83000.0
    9   France  37.0  67000.0
    ---------------------------------------
    <class 'pandas.core.series.Series'>
    0     No
    1    Yes
    2     No
    3     No
    4    Yes
    5    Yes
    6     No
    7    Yes
    8     No
    9    Yes
    Name: Purchased, dtype: object


Selecting pandas data using `loc`:-
The Pandas `loc` indexer can be used with DataFrames in two different scenarios:

     a.) Selecting rows by label/index
     b.) Selecting rows with a Boolean/conditional lookup

The `loc` indexer is used with the same syntax as `iloc: data.loc[<row selection>, <column selection>]`

Index can be in a DataFrame by using `set_index()` method


```python
dataset.set_index("Country", inplace=True)
dataset
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Salary</th>
      <th>Purchased</th>
    </tr>
    <tr>
      <th>Country</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>France</th>
      <td>44.0</td>
      <td>72000.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>Spain</th>
      <td>27.0</td>
      <td>48000.0</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>Germany</th>
      <td>30.0</td>
      <td>54000.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>Spain</th>
      <td>38.0</td>
      <td>61000.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>Germany</th>
      <td>40.0</td>
      <td>NaN</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>France</th>
      <td>35.0</td>
      <td>58000.0</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>Spain</th>
      <td>NaN</td>
      <td>52000.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>France</th>
      <td>48.0</td>
      <td>79000.0</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>Germany</th>
      <td>50.0</td>
      <td>83000.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>France</th>
      <td>37.0</td>
      <td>67000.0</td>
      <td>Yes</td>
    </tr>
  </tbody>
</table>
</div>




Selecting rows by index


```python
dataset.loc['France']
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Salary</th>
      <th>Purchased</th>
    </tr>
    <tr>
      <th>Country</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>France</th>
      <td>44.0</td>
      <td>72000.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>France</th>
      <td>35.0</td>
      <td>58000.0</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>France</th>
      <td>48.0</td>
      <td>79000.0</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>France</th>
      <td>37.0</td>
      <td>67000.0</td>
      <td>Yes</td>
    </tr>
  </tbody>
</table>
</div>



Selecting rows by label/index


```python
dataset.loc[['France', 'Spain'], ['Age', 'Salary']]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Salary</th>
    </tr>
    <tr>
      <th>Country</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>France</th>
      <td>44.0</td>
      <td>72000.0</td>
    </tr>
    <tr>
      <th>France</th>
      <td>35.0</td>
      <td>58000.0</td>
    </tr>
    <tr>
      <th>France</th>
      <td>48.0</td>
      <td>79000.0</td>
    </tr>
    <tr>
      <th>France</th>
      <td>37.0</td>
      <td>67000.0</td>
    </tr>
    <tr>
      <th>Spain</th>
      <td>27.0</td>
      <td>48000.0</td>
    </tr>
    <tr>
      <th>Spain</th>
      <td>38.0</td>
      <td>61000.0</td>
    </tr>
    <tr>
      <th>Spain</th>
      <td>NaN</td>
      <td>52000.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
dataset.loc[['France', 'Spain'], 'Age':'Purchased']
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Salary</th>
      <th>Purchased</th>
    </tr>
    <tr>
      <th>Country</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>France</th>
      <td>44.0</td>
      <td>72000.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>France</th>
      <td>35.0</td>
      <td>58000.0</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>France</th>
      <td>48.0</td>
      <td>79000.0</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>France</th>
      <td>37.0</td>
      <td>67000.0</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>Spain</th>
      <td>27.0</td>
      <td>48000.0</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>Spain</th>
      <td>38.0</td>
      <td>61000.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>Spain</th>
      <td>NaN</td>
      <td>52000.0</td>
      <td>No</td>
    </tr>
  </tbody>
</table>
</div>



resetting the index and setting a new index


```python
dataset.reset_index(inplace=True)

dataset.set_index('Age', inplace=True)
dataset
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Country</th>
      <th>Salary</th>
      <th>Purchased</th>
    </tr>
    <tr>
      <th>Age</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>44.0</th>
      <td>France</td>
      <td>72000.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>27.0</th>
      <td>Spain</td>
      <td>48000.0</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>30.0</th>
      <td>Germany</td>
      <td>54000.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>38.0</th>
      <td>Spain</td>
      <td>61000.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>40.0</th>
      <td>Germany</td>
      <td>NaN</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>35.0</th>
      <td>France</td>
      <td>58000.0</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>NaN</th>
      <td>Spain</td>
      <td>52000.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>48.0</th>
      <td>France</td>
      <td>79000.0</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>50.0</th>
      <td>Germany</td>
      <td>83000.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>37.0</th>
      <td>France</td>
      <td>67000.0</td>
      <td>Yes</td>
    </tr>
  </tbody>
</table>
</div>



Selecting rows by label/index


```python
dataset.loc[[44.0, 27.0], ['Country', 'Salary']]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Country</th>
      <th>Salary</th>
    </tr>
    <tr>
      <th>Age</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>44.0</th>
      <td>France</td>
      <td>72000.0</td>
    </tr>
    <tr>
      <th>27.0</th>
      <td>Spain</td>
      <td>48000.0</td>
    </tr>
  </tbody>
</table>
</div>



Selecting rows with a Boolean/conditional lookup


```python
dataset.loc[dataset['Country'] == 'France', ['Country', 'Salary']]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Country</th>
      <th>Salary</th>
    </tr>
    <tr>
      <th>Age</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>44.0</th>
      <td>France</td>
      <td>72000.0</td>
    </tr>
    <tr>
      <th>35.0</th>
      <td>France</td>
      <td>58000.0</td>
    </tr>
    <tr>
      <th>48.0</th>
      <td>France</td>
      <td>79000.0</td>
    </tr>
    <tr>
      <th>37.0</th>
      <td>France</td>
      <td>67000.0</td>
    </tr>
  </tbody>
</table>
</div>



Selections can be achieved outside of the main `.loc` for clarity
Form a separate variable with your selections:
like in the example below Select only the True values in `idx` and only the 3 columns specified:


```python
idx = dataset['Country'].apply(lambda x: x.lower() == 'france')
dataset.loc[idx, ['Country', 'Salary']]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Country</th>
      <th>Salary</th>
    </tr>
    <tr>
      <th>Age</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>44.0</th>
      <td>France</td>
      <td>72000.0</td>
    </tr>
    <tr>
      <th>35.0</th>
      <td>France</td>
      <td>58000.0</td>
    </tr>
    <tr>
      <th>48.0</th>
      <td>France</td>
      <td>79000.0</td>
    </tr>
    <tr>
      <th>37.0</th>
      <td>France</td>
      <td>67000.0</td>
    </tr>
  </tbody>
</table>
</div>



Selecting pandas data using `ix`:-

- `ix[]` indexer is a hybrid of `.loc` and `.iloc`,
- `ix` is label based indexer, it behave just like `.loc`, it also supports integer based indexing like `.iloc`
- `ix` indexing works just the same as `.loc` when passed strings


```python
dataset.ix[['Country']] == dataset.loc[['Country']]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Country</th>
      <th>Salary</th>
      <th>Purchased</th>
    </tr>
    <tr>
      <th>Age</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Country</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>



`ix` indexing works the same as `.iloc` when passed integers


```python
dataset.reset_index(inplace=True)
dataset.ix[[2]] == dataset.iloc[[2]]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Country</th>
      <th>Salary</th>
      <th>Purchased</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>



#### Add and Delete in DataFrame

- Adding row in DataFrame

Note:- General recommendation for adding a row is to use `.loc` to insert rows in DataFrame
If you would use `.ix`, you might try to reference a numerically valued index with the index value and accidentally overwrite an existing row of your DataFrame.



```python
dataset.loc[10] = ['India', 27, 65000, 'Yes']
dataset.ix[11] = ['India', 26, 60000, 'Yes']
dataset
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Country</th>
      <th>Salary</th>
      <th>Purchased</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>44</td>
      <td>France</td>
      <td>72000.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>1</th>
      <td>27</td>
      <td>Spain</td>
      <td>48000.0</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>2</th>
      <td>30</td>
      <td>Germany</td>
      <td>54000.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>3</th>
      <td>38</td>
      <td>Spain</td>
      <td>61000.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>4</th>
      <td>40</td>
      <td>Germany</td>
      <td>NaN</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>5</th>
      <td>35</td>
      <td>France</td>
      <td>58000.0</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>6</th>
      <td>NaN</td>
      <td>Spain</td>
      <td>52000.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>7</th>
      <td>48</td>
      <td>France</td>
      <td>79000.0</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>8</th>
      <td>50</td>
      <td>Germany</td>
      <td>83000.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>9</th>
      <td>37</td>
      <td>France</td>
      <td>67000.0</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>10</th>
      <td>India</td>
      <td>27</td>
      <td>65000.0</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>11</th>
      <td>India</td>
      <td>26</td>
      <td>60000.0</td>
      <td>Yes</td>
    </tr>
  </tbody>
</table>
</div>



- Adding column in DataFrame

Columns in DataFrame is basically a series,so adding a column in a DataFrame is as simple as assigning a new column to a DataFrame


```python
column = pd.Series(range(1,13), dtype=float)
column
```




    0      1.0
    1      2.0
    2      3.0
    3      4.0
    4      5.0
    5      6.0
    6      7.0
    7      8.0
    8      9.0
    9     10.0
    10    11.0
    11    12.0
    dtype: float64




```python
#adding column in DataFrame
dataset['id'] = column
dataset
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Country</th>
      <th>Salary</th>
      <th>Purchased</th>
      <th>id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>44</td>
      <td>France</td>
      <td>72000.0</td>
      <td>No</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>27</td>
      <td>Spain</td>
      <td>48000.0</td>
      <td>Yes</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>30</td>
      <td>Germany</td>
      <td>54000.0</td>
      <td>No</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>38</td>
      <td>Spain</td>
      <td>61000.0</td>
      <td>No</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>40</td>
      <td>Germany</td>
      <td>NaN</td>
      <td>Yes</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>35</td>
      <td>France</td>
      <td>58000.0</td>
      <td>Yes</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>NaN</td>
      <td>Spain</td>
      <td>52000.0</td>
      <td>No</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>48</td>
      <td>France</td>
      <td>79000.0</td>
      <td>Yes</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>50</td>
      <td>Germany</td>
      <td>83000.0</td>
      <td>No</td>
      <td>9.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>37</td>
      <td>France</td>
      <td>67000.0</td>
      <td>Yes</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>India</td>
      <td>27</td>
      <td>65000.0</td>
      <td>Yes</td>
      <td>11.0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>India</td>
      <td>26</td>
      <td>60000.0</td>
      <td>Yes</td>
      <td>12.0</td>
    </tr>
  </tbody>
</table>
</div>



- Delete a column from DataFrame by column name


```python
df = dataset.drop('Purchased', axis=1)
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Country</th>
      <th>Salary</th>
      <th>id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>44</td>
      <td>France</td>
      <td>72000.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>27</td>
      <td>Spain</td>
      <td>48000.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>30</td>
      <td>Germany</td>
      <td>54000.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>38</td>
      <td>Spain</td>
      <td>61000.0</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>40</td>
      <td>Germany</td>
      <td>NaN</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>35</td>
      <td>France</td>
      <td>58000.0</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>NaN</td>
      <td>Spain</td>
      <td>52000.0</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>48</td>
      <td>France</td>
      <td>79000.0</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>50</td>
      <td>Germany</td>
      <td>83000.0</td>
      <td>9.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>37</td>
      <td>France</td>
      <td>67000.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>India</td>
      <td>27</td>
      <td>65000.0</td>
      <td>11.0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>India</td>
      <td>26</td>
      <td>60000.0</td>
      <td>12.0</td>
    </tr>
  </tbody>
</table>
</div>



- Delete a column from DataFrame by row index

one thing to be noted here is if the in-place is set to be True the deleting happens the the existing dataframe
by default in-place is False, which creates new DataFrame with deleted rows


```python
dataset.drop(dataset.index[2:7], inplace=True)
dataset
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Country</th>
      <th>Salary</th>
      <th>Purchased</th>
      <th>id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>44</td>
      <td>France</td>
      <td>72000.0</td>
      <td>No</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>27</td>
      <td>Spain</td>
      <td>48000.0</td>
      <td>Yes</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>48</td>
      <td>France</td>
      <td>79000.0</td>
      <td>Yes</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>50</td>
      <td>Germany</td>
      <td>83000.0</td>
      <td>No</td>
      <td>9.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>37</td>
      <td>France</td>
      <td>67000.0</td>
      <td>Yes</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>India</td>
      <td>27</td>
      <td>65000.0</td>
      <td>Yes</td>
      <td>11.0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>India</td>
      <td>26</td>
      <td>60000.0</td>
      <td>Yes</td>
      <td>12.0</td>
    </tr>
  </tbody>
</table>
</div>
