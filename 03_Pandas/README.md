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

---

## Progress

Pandas Library Learning :  █░░░░░░░░░░░ 05%
