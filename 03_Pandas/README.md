# Day 01 - Pandas Series Basics and Some Methods


## Topics Covered

* `Pandas_1_series_Introduction_basics.ipynb`
    * Introduction to pandas
        * Why Pandas? 
        * Two primary Data Structures
    * Importing pandas
    * Creating Series

* `Pandas_2_indexing_and_conditions.ipynb`
    * Indexing in Series
        * Single element access
        * Multiple sequential element access
        * Particular group of element access
        * iloc usage problem 
        * solution : usage of loc
        * Difference between iloc and loc & Numeric and label based slicing
    * Dictionary-based Series
    * Conditional Selection (s2>1 --> Gives True and False Series)
    * Logical Operators (& | ~ --> To combine multiple Conditional Selections)
    * Modification in Series



<br>

## Functions & Methods Learned

| Function / Method   | Purpose                  |
| -----------------   | ------------------------ |
| `pd.Series()`       | Create Series object     |
| `s.dtype`           | Check datatype           |
| `s.values`          | Access values            |
| `s.index`           | Access indexes           |
| `s.shape`           | Find dimensions          |
| `s.name`            | Name of Series           |
| `s.size`            | Total number of elements |
| `s.head()`          | Show first rows (By default 5)          |
| `s.tail()`          | Show last rows  (By default 5)          |

<br>


## Key Learnings of the Day

* Series is similar to NumPy array but with indexing.
* Indexing ways : 
    * s[0]
    * s[0:2]  --> start included, stop excluded
    * s.iloc[2]  --> to access indexed element
    * s.iloc[[1,3,4]]  --> To access particular group of elements
        * iloc can't access through string index and can only access numeric index based elements.
    * Numeric based SLICING --> In this stop is excluded from start : stop : step
    * Label based SLICING   --> In this stop is included from start : stop : step
    * Note : <b><i>we use double index means [[]] when we need to pass group of indices to somewhere.. </i></b>
    <br>
* Conditional Selection gives you binary Series of given Series.
* ### Realization

    Initially I thought Python logical operators (`and`, `or`) would work with pandas Series.

    But pandas requires bitwise operators (`&`, `|`) because operations are performed element-wise across the Series.
<br>

## Files Updated

* `Pandas_1_series_Introduction_basics.ipynb`
* `Pandas_2_indexing_and_conditions.ipynb`

<br>
<br>

# Day 02 - Dataframe Basics and Some Methods


## Topics Covered

* `Pandas_3_Dataframe_Introduction_broadcasting.ipynb`
    * Introduction to Dataframe
        * Dictionary to dataframe
    * Showing Dataframe --> `df.head()` & `df.tail()`
    * Indexing in Series
        * iloc & loc
        * Showing Particular column of the dataframe.
    * Drop particular column from dataset.
    * Check information of dataframe
    * Broadcasting 
    * Renaming column
    * Unique values of column and `value_counts()`
    * Add new column



<br>

## Functions & Methods Learned

| Function / Method   | Purpose                  |
| -----------------   | ------------------------ |
| `df.drop(colName, axis=1)`       | Drop Particular column <br> axis = 1 indicates entire column will gone <br>axis = 0 indicates entire row will gone<br> inplace=True means change parmenantly.    |
| `df.info()`           | Check information of dataframe.           |
| `df.describe()`          | Check information of numeric columns            |
| `df.rename(columns = {"old":"new"}, inplace = True)`           | To change particular column name           |
| `df.unique()`           | Find unique values of column          |
| `df.value_counts()`            | To find how many times unique values are occured in dataframe or column.           |

<br>

## Files Updated

* `Pandas_3_Dataframe_Introduction_broadcasting.ipynb`

---

## Progress

Pandas Library Learning :  ██░░░░░░░░░░ 21%
