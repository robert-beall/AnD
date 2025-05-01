# Quick Sort
Quick sort is a [divide-and-conquer](https://en.wikipedia.org/wiki/Divide-and-conquer_algorithm#:~:text=A%20divide%2Dand%2Dconquer%20algorithm,solution%20to%20the%20original%20problem.) algorithm that picks a pivot in a list and partitions the array around the pivot such that the pivot is placed in its correct sorted place.

- [Quick Sort](#quick-sort)
  - [Algorithm](#algorithm)
    - [Visualization](#visualization)
  - [How to Choose a Pivot](#how-to-choose-a-pivot)
  - [Partition Algorithms](#partition-algorithms)
    - [Naive Approach](#naive-approach)
  - [Sources](#sources)

## Algorithm
1. **Choose a pivot** in the array (methods for how to choose are covered later)
2. **Partition the array**, rearranging the remaining elements around the pivot. Once this is complete, all elements smaller than the pivot will be to the left and all elements larger will be to the right.
3. **Recursively apply this process**, picking a pivot on each partition of the array.
4. **Base Case:** when an array has only one element, it is considered sorted by default.

### Visualization
Given list `A`:

|2|17|5|12|4|23|8|
|-|--|-|--|-|--|-|

1. Find a pivot:

|2|17|5|<span style="color:green">12|4|23|8|
|-|--|-|--|-|--|-|

2. Partition the array:

|2|5|8|4|<span style="color:green">12|17|23|
|-|-|-|-|-|--|-|

3. Recursively call the process:

|2|5|<span style="color:green">8|4|
|-|-|-|-|

12

|<span style="color:green">17|23|
|-|-|

4. Base case is a single-element array:

|17|
|-|

## How to Choose a Pivot
1. **Always pick the first or last element:** This approach is simple, but ends up in the worst case when a list is already sorted.
2. **Pick a random element:** The advantage of this approach is that there is no given pattern for whether there is a worst case or not.
3. **Pick the median element:** Ideal approach in time complexity (*O(n)*), however it can take longer on average as it adds operational overhead.

## Partition Algorithms
### Naive Approach
## Sources
1. [Geeks For Geeks](https://www.geeksforgeeks.org/quick-sort-algorithm/)