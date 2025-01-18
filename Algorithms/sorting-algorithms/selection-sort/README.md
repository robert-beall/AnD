# Selection Sort
Selection sort takes the smallest element of the unsorted portion of a list and swaps it into the first unsorted position of the list. These swaps continue until the entire list is sorted<sup>[1](#sources)</sup>.

- [Selection Sort](#selection-sort)
  - [Algorithm](#algorithm)
    - [Visualization](#visualization)
  - [Performance](#performance)
    - [Memory](#memory)
  - [Sources](#sources)

## Algorithm
1. Given a zero-indexed list `A` of size *n*, find the smallest element in the range `0 -> n`.
2. Swap this smallest element with the value at index `0`. 
3. Increment the swap position and decrement the size of the unsorted range until all elements have been sorted. 

### Visualization
Given list `A`:

|4|17|5|12|2|23|
|-|--|-|--|-|--|

The first swap operation will look like the following:

1. Set the swap position to index 0:
   
|<span style="color:#a17f1a">4|17|5|12|2|23|
|-|--|-|--|-|--|

1. Find the smallest element:
   
|<span style="color:#a17f1a">4|17|5|12|<span style="color:darkgreen">2|23|
|-|--|-|--|-|--|

3. Swap the smallest value into index 0
   
|<span style="color:darkgreen">2|17|5|12|<span style="color:gray">4|23|
|-|--|-|--|-|--|

3. Set the new swap position to index 1 and repeat
   
|2|<span style="color:#a17f1a">17|5|12|<span style="color:gray">4|23|
|-|--|-|--|-|--|

## Performance
Like [bubble sort](/Algorithms/sorting-algorithms/bubble-sort/README.md), selection sort has a time complexity of *O(n<sup>2</sup>)*, making it unsuitable for large datasets<sup>[2](#sources)</sup>. This is because you must loop through *n* elements for each *n* elements to find each swappable value.

Unlike bubble sort, this algorithm is not stable.

### Memory
The algorithm is memory efficient, requiring *O(1)* of space as swaps are performed in place and memory writes are minimal.

## Sources
1. [Geeks for Geeks](https://www.geeksforgeeks.org/selection-sort-algorithm-2/)
2. [Wikipedia](https://en.wikipedia.org/wiki/Selection_sort)