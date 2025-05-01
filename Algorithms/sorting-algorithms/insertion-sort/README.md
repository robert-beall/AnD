# Insertion Sort
Insertion sort iteratively inserts elements from an 'unsorted' list into the correct position of the 'sorted' list.

- [Insertion Sort](#insertion-sort)
  - [Algorithm](#algorithm)
    - [Visualization](#visualization)
  - [Performance](#performance)
    - [Best Case](#best-case)
    - [Worst and Average Cases](#worst-and-average-cases)
  - [Source](#source)


## Algorithm
1. Given list 'A' of *n* elements, place the element in index *0* in the 'sorted' portion of the list.
2. Take the element at index *1* and sort it into the correct position relative to index *0* (before or after depending on value).
3. Repeat for indices *2* through *n*.

### Visualization
Given list `A`:

|2|1|5|12|4|23|
|-|--|-|--|-|--|

1. Assume the element at index *0* is sorted.

|<span style="color:darkgreen">2</span>|1|5|12|4|23|
|-|--|-|--|-|--|

2. Take the element at index *1* and place it in the correct position relative to the *sorted* element at index *0*.

|<span style="color:darkgreen">2</span>|<span style="color:#a17f1a">1|5|12|4|23|
|-|--|-|--|-|--|

3. Because *1 < 2*, the element at index *1* swaps with the element at index *0*.

|<span style="color:darkgreen">1</span>|<span style="color:darkgreen">2|5|12|4|23|
|-|--|-|--|-|--|

Repeat for indices *2 - n*.

## Performance
The performance of insertion sort can be divided into best, worst, and average case scenarios.

### Best Case
In the best case, the list is already sorted or nearly sorted, yielding a near linear *O(n)* runtime. Each subsequent element only has to be compared with the right-most sorted element.

### Worst and Average Cases
The worst case scenario is a list sorted in reverse-order, yielding a quadratic runtime *O(n<sup>2</sup>*).

The average case is also quadratic, making the algorithm unsuitable for large datasets. That being said, insertion sort is one of the fastest algorithms for small lists.

## Source
1. [Geeks for Geeks](https://www.geeksforgeeks.org/insertion-sort-algorithm/)
2. [Wikipedia](https://en.wikipedia.org/wiki/Insertion_sort)