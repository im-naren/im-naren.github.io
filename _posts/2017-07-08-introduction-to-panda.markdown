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
---


```python
# Importing the library
import pandas as pd
```


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



```python
# dtypes properties shows the data types of each column in the DataFrame
dataset.dtypes
```




    Country       object
    Age          float64
    Salary       float64
    Purchased     object
    dtype: object




```python
# describe method shows basic statistics about the dataset's numeric columns
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




```python
# columns.values gives the column names in the DataFrame
dataset.columns.values
```




    array(['Country', 'Age', 'Salary', 'Purchased'], dtype=object)




```python
# index.values gives the list of row indices
dataset.index.values
```




    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])




```python
# head method shows first n rows from the DataFrame, default value of n is 5
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
# tail method shows last n rows from the DataFrame, default value of n is 5
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




```python

```


```python

```
