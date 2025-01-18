# Array
A collection of elements of the same memory size. Each element is identified by at least one index or key<sup>[2](https://dev.to/m__mdy__m/understanding-array-data-structures-8do)</sup>.

## How Data is Stored
In an array, the position of each element can be calculated from its index tuple (i.e. `arr[0], arr2[0][1]...`) using a mathematical formula<sup>[1](https://en.wikipedia.org/wiki/Array_(data_structure))</sup>. 

### Example
Given an array of ten elements, each a 32bit (4 byte) integer: 

```
let arr = [40, 21, 52, 62, 47, 54, 96, 70, 8, 92, 17];
```

This array will have indices *1-9*. As such, each element of the array might be stored at memory addresses `2000, 2004, 2008...`. 


|2000|2004|2008|2012|2016|2020|2024|2028|2032|2036|2040|
|----|----|----|----|----|----|----|----|----|----|----|
|40|21|52|62|47|54|96|70|8|92|17|

Each element can be accessed by the following equation:

```
base_address + (index * element_size);
```

For the above example, if we wanted to access the fifth element (i = 4), we would do `2000 + (4 x 4) = 2016`.

The memory address of the first element is called the **base address**<sup>[1](https://en.wikipedia.org/wiki/Array_(data_structure))</sup>.

## Sources
1. [Array (Wikipedia)](https://en.wikipedia.org/wiki/Array_(data_structure))
2. [Understanding Array Data Structures](https://dev.to/m__mdy__m/understanding-array-data-structures-8do)