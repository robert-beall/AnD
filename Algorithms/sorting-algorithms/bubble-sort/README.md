# Bubble Sort
Bubble sort is the simplest sorting algorithm. It uses multiple passes through a list, swapping elements based  on size with each pass. 

Bubble sort, while simple, is inefficient and unsuitable for large datasets. 

- [Bubble Sort](#bubble-sort)
  - [Algorithm](#algorithm)
    - [Visualization](#visualization)
  - [Performance](#performance)
    - [Memory](#memory)
  - [Source](#source)


## Algorithm
1. Given list `A`, make multiple passes through the list until the list is sorted.
2. For each pass, compare two adjacent list elements at a time, swapping the order based on sort criteria. 
3. Once a pass is completed without performing a swap, the list is sorted.

After the first pass, the largest (or smallest depending on sort criteria) will have 'bubbled' to the end of the list. After the second, the second-largest (or smallest) will have bubbled to the second to last slot of the list, and so on and so forth.

### Visualization
Given list `A`:

|2|17|5|12|4|23|
|-|--|-|--|-|--|

The first pass through will look like the following. **<span style="color:#a17f1a">gold</span>** indicates a swap, **<span style="color:darkgreen">green</span>** indicates that the pair is sorted and no swap is necessary.

1. 2 and 17 compared, no swap
   |<span style="color:darkgreen">2|<span style="color:darkgreen">17|5|12|4|23|
    |-|--|-|--|-|--|
2. 17 and 5 compared, swap
   |2|<span style="color:#a17f1a">5|<span style="color:#a17f1a">17|12|4|23|
    |-|--|-|--|-|--|
3. 17 and 12 compared, swap
   |2|5|<span style="color:#a17f1a">12|<span style="color:#a17f1a">17|4|23|
    |-|--|-|--|-|--|
4. 17 and 4 compared, swap
   |2|5|12|<span style="color:#a17f1a">4|<span style="color:#a17f1a">17|23|
    |-|--|-|--|-|--|
4. 17 and 23 compared, no swap
   |2|5|12|4|<span style="color:darkgreen">17|<span style="color:darkgreen">23|
    |-|--|-|--|-|--|

By the end of this first pass, the largest element (`23`) is positioned at the end of the list. Because we performed a swap this pass, at least one more pass is needed to sort the list. 

## Performance
The worst case for bubble sort requires that for a list of length `n`, you perform `n` passes on `n` elements each time. As such, its time complexity is *O(n<sup>2</sup>)*. This makes bubble sort too slow for most practical applications. 

The algorithm is stable, meaning otherwise equal values will retain their order in the list (i.e. if a list has two *3s*, the first 3 will be before the second 3).

### Memory
One small advantage of bubble sort is that it requires no new memory allocation, as all swaps are performed [in-place](https://en.wikipedia.org/wiki/In-place_algorithm).

## Source
1. [Geeks for Geeks](https://www.geeksforgeeks.org/bubble-sort-algorithm/)